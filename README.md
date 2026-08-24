# ELEPHANT — EFMW Zoo #26

**Extended Longitudinal Episodic Persistence, History And Narrative Tracking**

ELEPHANT is a candidate EFMW-inspired framework for testing whether a system preserves important facts, commitments, event order, provenance, and uncertainty across long interactions.

## Core question

> Does the system still remember what actually happened, in the right order, with the right confidence, after many transformations and intervening events?

ELEPHANT is not a simple retrieval benchmark. It evaluates temporal continuity, contradiction handling, memory compression, provenance retention, and resistance to narrative drift.

## Key outputs

- episodic retention score
- temporal-order accuracy
- provenance retention
- contradiction recovery
- commitment persistence
- uncertainty preservation
- narrative-drift score

## Repository contents

- `theory.md`
- `architecture.md`
- `memory_model.md`
- `limitations.md`
- `elephant.py`
- `benchmark.py`
- `ablations.py`
- `test_elephant.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_elephant.py
```

## Zoo position

MAGPIE #24 tracks grounding and provenance.

WOLF #25 detects weak distributed precursor signals.

**ELEPHANT #26 asks whether the system preserves its own history accurately enough for later reasoning to remain trustworthy.**
