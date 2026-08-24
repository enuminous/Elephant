import unittest
from elephant import ElephantMemory, Event

class TestElephant(unittest.TestCase):
    def test_supersession_preserves_history(self):
        m = ElephantMemory()
        m.add_event(Event("e1",1,"a","old","p1"))
        m.add_event(Event("e2",2,"a","new","p2",supersedes="e1"))
        self.assertEqual(len(m.history()), 2)
        self.assertEqual(m.events["e1"].status, "superseded")
        self.assertEqual(m.events["e2"].status, "active")

    def test_temporal_order(self):
        m = ElephantMemory()
        m.add_event(Event("e2",2,"a","second","p2"))
        m.add_event(Event("e1",1,"a","first","p1"))
        self.assertEqual([e.id for e in m.history()], ["e1","e2"])

    def test_lineage(self):
        m = ElephantMemory()
        m.add_event(Event("e1",1,"a","old","p1"))
        m.add_event(Event("e2",2,"a","new","p2",supersedes="e1"))
        ids = [e.id for e in m.lineage("e2")]
        self.assertEqual(ids, ["e2","e1"])

if __name__ == "__main__":
    unittest.main()
