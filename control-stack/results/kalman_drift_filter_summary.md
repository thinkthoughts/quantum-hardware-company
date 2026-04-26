# Kalman Drift Filter Results

---

## Error Reduction

| Metric | Uncompensated | Moving Avg | Kalman | Reduction (MA) | Reduction (Kalman) |
|--------|--------------|------------|--------|----------------|--------------------|
| Omega RMSE | 0.0429 | 0.0197 | 0.00194 | **-54%** | **-95.5%** |
| Offset RMSE | 0.0334 | 0.00394 | 0.00343 | **-88.2%** | **-89.7%** |
| Response RMSE | 0.0771 | 0.0302 | 0.00448 | **-60.8%** | **-94.2%** |

---

## Phase-lock Stability

| Metric | Uncomp | Moving Avg | Kalman |
|--------|--------|------------|--------|
| Min phase-lock | 0.978 | 0.993 | **0.99993** |
| Mean phase-lock | 0.991 | 0.998 | **0.99998** |
| Phase-lock threshold | 0.707 | 0.707 | 0.707 |
| All blocks phase-locked | TRUE | TRUE | **TRUE** |

---

## Control Behavior

- Estimator: Kalman filter (independent Ω, B)
- Moving-average window: 4
- Process noise:
  - q_Ω = 8.0e-4
  - q_B = 1.0e-5
- Measurement noise:
  - r_Ω ≈ 3.24e-6
  - r_B ≈ 3.35e-5

Best tuned:

- q_Ω ≈ 1.47e-4

Behavior:

- Ω: fast adaptive tracking
- B: smooth low-noise estimation
- Control commands: stable and low variance

---

## Drift Characteristics

- Ω (frequency): oscillatory + moderate noise → benefits strongly from Kalman prediction
- B (offset): slow drift → already well handled by smoothing
- Kalman advantage: removes lag while preserving smoothing

---

## Interpretation

Kalman filtering:

- models drift as a latent state
- balances prediction vs measurement
- removes estimator lag
- stabilizes response-level physics

Compared to moving average:

- similar noise suppression
- significantly improved tracking
- dramatically lower response error

---

## Key Insight

Moving-average control is reactive.

Kalman control is predictive.

This converts:

open-loop calibration → feedback control → state estimation → predictive stabilization

---

## Outcome

- ~17× reduction in response-level error vs uncompensated
- near-perfect phase-lock across all calibration blocks
- stable control under continuous drift

---

## Next Step

Compare control policies:

→ `03_control_policy_comparison.ipynb`

Goal:

- evaluate predictive Kalman vs filtered Kalman
- compare against moving average and oracle baseline
- identify optimal control strategy
