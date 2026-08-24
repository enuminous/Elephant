# ELEPHANT Theory

## 1. Problem

Long-running systems often fail not because they cannot retrieve text, but because they lose structure:

- who said what,
- when it happened,
- whether it was corrected,
- what remained uncertain,
- which commitments are still active,
- which statements superseded earlier ones.

ELEPHANT treats memory as a temporal relational object rather than a bag of facts.

## 2. Episodic record

Represent event `e_j` as:

`e_j = (id, t, actor, content, provenance, confidence, status, links)`

where status may include:
- active
- superseded
- contradicted
- retracted
- unresolved

## 3. Longitudinal memory state

At time `t`:

`M_t = {E_t, O_t, P_t, C_t, U_t}`

where:
- `E_t` = retained episodic content
- `O_t` = ordering relations
- `P_t` = provenance graph
- `C_t` = commitments/constraints
- `U_t` = uncertainty state

## 4. Retention

For weighted event importance `a_j`:

`R_t = sum_j a_j * retain(e_j,t) / sum_j a_j`

## 5. Order fidelity

Let `Q` be a set of known pairwise temporal relations.

`O_t = correct_order_relations / |Q|`

## 6. Provenance retention

`P_t = correctly_attributed_claims / evaluated_claims`

## 7. Contradiction recovery

If an earlier statement is later corrected, ELEPHANT tests whether the system preserves both:
- the historical fact that the earlier statement occurred,
- the current fact that it is no longer authoritative.

A contradiction-resolution score may be:

`C_t = resolved_contradictions / total_known_contradictions`

## 8. Uncertainty preservation

A system should not convert remembered uncertainty into certainty merely through repetition.

Let original confidence be `q_0` and recalled confidence be `q_t`.

`U_drift = mean |q_t - q_0|`

where unjustified increases are especially penalized.

## 9. Narrative drift

Define a composite drift measure:

`D_t = w1*(1-R_t) + w2*(1-O_t) + w3*(1-P_t) + w4*(1-C_t) + w5*U_drift`

Lower is better.

## 10. EFMW interpretation

The EFMW-inspired aspect is recursive state continuity across temporal layers. Each new event updates the present without erasing the relational structure of the past.

## 11. Falsifiable prediction

ELEPHANT should outperform simpler memory systems particularly when tasks require:
- long delays,
- superseding updates,
- contradiction repair,
- temporal ordering,
- provenance retention,
- uncertainty preservation.

If simple retrieval plus recency ranking performs equally well, the added architecture has not justified itself.
