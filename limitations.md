# Limitations and Falsification

ELEPHANT is an experimental framework.

## Limitations

- Event importance weighting can bias retention.
- Compression may preserve pointers while still losing semantic nuance.
- Temporal ambiguity can make strict ordering impossible.
- Human-entered corrections may themselves be wrong.
- Provenance can be present but unreliable.
- Long-memory benchmarks can reward memorization rather than useful reasoning.

## Falsification criteria

ELEPHANT's central hypothesis is weakened if:

1. Simple vector retrieval with recency ranking matches performance.
2. Provenance retention does not improve downstream correctness.
3. Explicit contradiction handling adds no measurable value.
4. Temporal-order structures do not improve long-delay tasks.
5. Performance gains vanish on held-out histories.
6. Compression with lineage performs no better than flat summaries.

## Claim boundary

ELEPHANT measures memory integrity under a specified representation and benchmark. It does not establish human-like autobiographical memory or consciousness.
