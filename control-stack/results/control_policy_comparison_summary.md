# Control Policy Comparison Results

---

## Error Metrics

| Policy | Omega RMSE | Offset RMSE | Response RMSE (mean) | Response RMSE (max) |
|--------|------------|-------------|----------------------|---------------------|
| Oracle | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Kalman | 0.00194 | 0.00343 | 0.00448 | 0.00808 |
| Predictive Kalman | 0.01476 | 0.00515 | 0.02274 | 0.05638 |
| Moving Average | 0.01974 | 0.00394 | 0.03021 | 0.07000 |
| None | 0.04290 | 0.03339 | 0.07714 | 0.13957 |

---

## Phase-lock Stability

| Policy | Min | Mean | Max Angle (deg) | All Phase-Locked |
|--------|-----|------|-----------------|------------------|
| Oracle | 1.000 | 1.000 | ~0.0 | TRUE |
| Kalman | 0.99993 | 0.99998 | 0.69° | TRUE |
| Predictive Kalman | 0.99549 | 0.99895 | 5.44° | TRUE |
| Moving Average | 0.99304 | 0.99813 | 6.76° | TRUE |
| None | 0.97774 | 0.99138 | 12.11° | TRUE |

Phase-lock threshold: **0.707**

All policies remain stable, but margin varies.

---

## Policy Ranking

Best → worst (by response RMSE):

1. Oracle
2. Kalman
3. Predictive Kalman
4. Moving Average
5. No Control

---

## Control Behavior

- Moving average:
  - smooth but lagged
  - poor tracking of oscillatory drift

- Kalman:
  - optimal balance of noise rejection and responsiveness
  - best overall performance

- Predictive Kalman:
  - limited predictive capability
  - lacks dynamic state modeling

- Oracle:
  - perfect tracking (reference only)

---

## Drift Characteristics

- Ω (frequency):
  - oscillatory + noise
  - requires responsive estimator

- B (offset):
  - slow monotonic drift
  - easier to track

---

## Interpretation

Control policy selection:

- significantly reduces parameter error
- directly improves observable quantum response
- determines robustness to worst-case drift

Kalman filtering provides the best practical solution under current assumptions.

---

## Key Insight

Adding estimation is not enough.

**Optimal control requires both estimation and appropriate system modeling.**

---

## Next Step

Upgrade predictive model:

→ `04_velocity_state_kalman.ipynb`

Goal:

- incorporate drift velocity
- improve prediction accuracy
- approach oracle-level performance
