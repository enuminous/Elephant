from elephant import ElephantMemory, Event

def build_history():
    m = ElephantMemory()
    m.add_event(Event("e1", 1, "sensor", "Valve B open", "log-1", 0.95))
    m.add_event(Event("e2", 2, "operator", "Pressure nominal", "note-2", 0.80))
    m.add_event(Event("e3", 8, "sensor", "Valve B closed", "log-8", 0.99, supersedes="e1"))
    m.add_event(Event("e4", 12, "analyst", "Pressure reading uncertain", "analysis-12", 0.55))
    m.add_event(Event("e5", 20, "sensor", "Pressure confirmed high", "log-20", 0.98, supersedes="e2"))
    return m

def run():
    m = build_history()
    expected_order = [("e1","e2"),("e2","e3"),("e3","e4"),("e4","e5")]
    expected_status = {"e1":"superseded","e2":"superseded","e3":"active","e4":"active","e5":"active"}
    expected_prov = {"e1":"log-1","e3":"log-8","e5":"log-20"}
    return m.metrics(expected_order, expected_status, expected_prov)

if __name__ == "__main__":
    print(run())
