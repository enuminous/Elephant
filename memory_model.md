# ELEPHANT Memory Model

## Event schema

Each memory item contains:

```json
{
  "id": "e17",
  "time": 17,
  "actor": "operator",
  "content": "Valve B was closed.",
  "provenance": "sensor-log-44",
  "confidence": 0.92,
  "status": "active",
  "supersedes": null
}
```

## Supersession

If `e_21` corrects `e_17`, retain both:

`e_17.status = superseded`

`e_21.supersedes = e_17`

This prevents historical erasure.

## Commitment state

Commitments should be represented separately from episodic statements.

Example:

`commitment = ("do_not_exceed", threshold=0.8, created_at=12, active=True)`

A later event may deactivate or modify it, but should not silently overwrite it.

## Recall query

A query should return:
- current answer
- historical lineage
- confidence
- relevant corrections
- provenance
- unresolved ambiguity

## Drift signature

A characteristic ELEPHANT failure is:

`retrieval_success = high`

while:

`temporal/provenance correctness = low`

This distinguishes memory access from memory integrity.
