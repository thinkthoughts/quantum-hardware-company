# Velocity-State Kalman Results

---

## Error Reduction

| Policy | Omega RMSE | Offset RMSE | Response RMSE (mean) | Response RMSE (max) |
|--------|------------|-------------|----------------------|--------------------|
| oracle | 0.0000 | ~0.0000 | ~0.0000 | ~0.0000 |
| scalar_kalman | 0.00194 | 0.00343 | **0.00448** | **0.00808** |
| velocity_filtered | 0.00194 | 0.00487 | 0.00546 | 0.01072 |
| velocity_predictive | 0.00956 | 0.00736 | 0.01691 | 0.03875 |
| moving_average | 0.01974 | 0.00394 | 0.03021 | 0.07000 |
| none | 0.04290 | 0.03339 | 0.07714 | 0.13957 |

---

## Phase-lock Stability

| Policy | Min | Mean | Max Angle (deg) | Phase-locked |
|--------|-----|------|----------------|-------------|
| oracle | ~1.000 | 1.000 | ~0.000 | TRUE |
| scalar_kalman | 0.99993 | 0.99998 | 0.69 | TRUE |
| velocity_filtered | 0.99993 | 0.99997 | 0.70 | TRUE |
| velocity_predictive | 0.99794 | 0.99954 | 3.68 | TRUE |
| moving_average | 0.99304 | 0.99813 | 6.76 | TRUE |
| none | 0.97774 | 0.99138 | 12.11 | TRUE |

Phase-lock threshold: 0.707

All policies remain above stability threshold.

---

## Control Behavior

- Scalar Kalman:
  - best overall performance
  - robust to model mismatch

- Velocity-filtered:
  - slightly worse than scalar
  - provides drift-rate observability

- Velocity-predictive:
  - higher error due to model mismatch
  - sensitive to process model assumptions

---

## Drift Characteristics

- Ω (frequency):
  - oscillatory drift
  - strong variation in drift rate

- B (offset):
  - slow monotonic drift
  - low-frequency dominant

Velocity-state model reveals:

- multi-timescale behavior
- non-constant drift dynamics

---

## Velocity Tuning

- current q_vel = 2e-4
- best q_vel ≈ 1e-2

Interpretation:

- higher process noise improves tracking
- system deviates from constant-velocity assumption

---

## Interpretation

Velocity-state Kalman:

- improves interpretability of drift
- enables estimation of drift rate
- maintains strong stability

But:

- predictive control degrades under model mismatch
- scalar filtering remains optimal for this system

---

## Key Insight

Adding state complexity does not guarantee improved control.

Performance depends on:

- correctness of system model
- balance between process noise and measurement noise

Velocity modeling is useful for:

- understanding system dynamics
- preparing for higher-order control

---

## Next Step

Recommended upgrades:

- joint-state Kalman (Ω + B)
- acceleration-based model
- residual modeling

Goal:

- improve predictive accuracy
- reduce response error
- maintain phase-lock stability
