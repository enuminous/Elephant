# ELEPHANT Architecture

## Pipeline

1. Event Ingestor
2. Importance Assigner
3. Temporal Index
4. Provenance Graph
5. Commitment Ledger
6. Contradiction Resolver
7. Memory Compressor
8. Recall Engine
9. Drift Auditor

## Ingestion requirements

Every meaningful event should preserve:
- timestamp/order
- actor/source
- content
- confidence
- provenance
- relation to earlier events

## Compression

Compression may summarize multiple events, but summaries must retain pointers to underlying episodes.

A valid compressed memory is therefore:

`summary + lineage`

not:

`summary alone`

## Recall output

ELEPHANT recall should return both the present-state answer and the path that produced it.

## Integration

MAGPIE can audit evidence lineage inside ELEPHANT.

WOLF can consume ELEPHANT-maintained history to detect slowly accumulating precursor structure.

Future Zoo frameworks may use ELEPHANT as the persistent longitudinal substrate.
