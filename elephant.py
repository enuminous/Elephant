from dataclasses import dataclass, field
from typing import Optional, Dict, List, Any

@dataclass
class Event:
    id: str
    time: int
    actor: str
    content: str
    provenance: str
    confidence: float = 1.0
    status: str = "active"
    supersedes: Optional[str] = None
    importance: float = 1.0

class ElephantMemory:
    def __init__(self):
        self.events: Dict[str, Event] = {}
        self.order: List[str] = []

    def add_event(self, event: Event):
        if event.supersedes and event.supersedes in self.events:
            self.events[event.supersedes].status = "superseded"
        self.events[event.id] = event
        self.order.append(event.id)
        self.order.sort(key=lambda eid: self.events[eid].time)

    def current_events(self):
        return [self.events[eid] for eid in self.order if self.events[eid].status == "active"]

    def history(self):
        return [self.events[eid] for eid in self.order]

    def lineage(self, event_id: str):
        if event_id not in self.events:
            return []
        out = []
        cur = self.events[event_id]
        seen = set()
        while cur and cur.id not in seen:
            out.append(cur)
            seen.add(cur.id)
            if cur.supersedes and cur.supersedes in self.events:
                cur = self.events[cur.supersedes]
            else:
                cur = None
        return out

    def metrics(self, expected_order=None, expected_status=None, expected_provenance=None):
        retention_num = sum(e.importance for e in self.events.values())
        retention_den = retention_num if retention_num else 1.0
        retention = retention_num / retention_den

        order_score = 1.0
        if expected_order:
            pos = {eid:i for i,eid in enumerate(self.order)}
            total = 0
            correct = 0
            for a,b in expected_order:
                if a in pos and b in pos:
                    total += 1
                    if pos[a] < pos[b]:
                        correct += 1
            order_score = correct/total if total else 1.0

        status_score = 1.0
        if expected_status:
            total = len(expected_status)
            correct = sum(1 for eid,s in expected_status.items()
                          if eid in self.events and self.events[eid].status == s)
            status_score = correct/total if total else 1.0

        provenance_score = 1.0
        if expected_provenance:
            total = len(expected_provenance)
            correct = sum(1 for eid,p in expected_provenance.items()
                          if eid in self.events and self.events[eid].provenance == p)
            provenance_score = correct/total if total else 1.0

        drift = 1.0 - (order_score + status_score + provenance_score)/3.0

        return {
            "retention": retention,
            "order_fidelity": order_score,
            "contradiction_resolution": status_score,
            "provenance_retention": provenance_score,
            "narrative_drift": drift,
        }
