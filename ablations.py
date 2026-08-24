from elephant import ElephantMemory, Event
from benchmark import build_history

def flat_latest_only():
    # Ablation: discard superseded history entirely.
    m = build_history()
    keep = ElephantMemory()
    for e in m.current_events():
        keep.add_event(e)
    return len(keep.history())

def no_provenance():
    m = build_history()
    for e in m.history():
        e.provenance = "unknown"
    return m.metrics(expected_provenance={"e3":"log-8","e5":"log-20"})

if __name__ == "__main__":
    full = build_history()
    print("full history length:", len(full.history()))
    print("latest-only history length:", flat_latest_only())
    print("no provenance:", no_provenance())
