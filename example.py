from elephant import ElephantMemory, Event

m = ElephantMemory()

m.add_event(Event(
    id="a",
    time=1,
    actor="technician",
    content="Pump temperature normal",
    provenance="inspection-001",
    confidence=0.90
))

m.add_event(Event(
    id="b",
    time=9,
    actor="sensor",
    content="Pump temperature elevated",
    provenance="sensor-009",
    confidence=0.97,
    supersedes="a"
))

print("CURRENT:")
for e in m.current_events():
    print(e)

print("\nHISTORY:")
for e in m.history():
    print(e)

print("\nLINEAGE FOR b:")
for e in m.lineage("b"):
    print(e)
