# 08 — Fast Drift MPC vs Kalman (CGCS Control Stack)

## Overview

This notebook studies **fast drift tracking** in Ω and B parameters under noisy measurement conditions, comparing:

- Moving average
- Scalar Kalman
- Joint Kalman
- Naive predictive
- Fast-drift MPC
- Oracle

Focus: **real-time calibration under rapid drift**

---

## System Model

- Fast sinusoidal drift in Ω
- Drift in B (offset)
- Measurement noise:
  - σ_Ω = 0.004
  - σ_B = 0.006

CGCS phase-lock constraint:

- cosine similarity ≥ 0.707 (45°)

---

## Ω Tracking and Control

![Fast drift Ω tracking](../figures/fast_drift_mpc/08_fast_drift_mpc_omega_tracking.png)

- Kalman methods closely track true Ω
- Moving average lags
- MPC smooths but slightly under-tracks peaks

---

## Response-Level Error

![RMSE comparison](../figures/fast_drift_mpc/08_fast_drift_mpc_response_rmse_comparison.png)

- Kalman achieves lowest error
- MPC reduces spikes vs naive predictive
- Naive predictive shows instability

---

## Policy Ranking

![Policy ranking](../figures/fast_drift_mpc/08_fast_drift_mpc_policy_ranking_summary.png)

| Method            | Mean RMSE |
|------------------|----------:|
| scalar_kalman     | 0.0085 |
| joint_kalman      | 0.0085 |
| fast_drift_mpc    | 0.0375 |
| moving_average    | 0.0416 |
| none              | 0.0932 |
| naive_predictive  | 0.0976 |

---

## MPC Horizon Sweep

![Horizon sweep](../figures/fast_drift_mpc/08_fast_drift_mpc_horizon_sweep.png)

- Best performance at **H = 0**
- Longer horizons degrade under fast drift

---

## CGCS Phase-Lock Stability

![CGCS stability](../figures/fast_drift_mpc/08_fast_drift_mpc_cgcs_stability_comparison.png)

- All methods remain above 45° threshold
- Kalman ≈ perfect alignment
- MPC maintains safe envelope

---

## Worst-Case Block Behavior

![Worst-case block](../figures/fast_drift_mpc/08_fast_drift_mpc_worst_case_block_comparison.png)

- Naive predictive overshoots strongly
- MPC remains bounded
- Kalman tightly tracks

---

## B Drift Tracking

![B tracking](../figures/fast_drift_mpc/08_fast_drift_mpc_offset_tracking.png)

- Joint Kalman captures coupled dynamics
- MPC smooths control
- Moving average lags

---

## Command-Bound Sweep

![Command bound sweep](../figures/fast_drift_mpc/08_fast_drift_mpc_command_bound_sweep.png)

- Larger bounds improve tracking
- Optimal ≈ 0.03

---

## Interpretation

### Kalman Filters
- Best estimators
- Minimal lag
- Highest CGCS alignment

### Fast-Drift MPC
- Constraint-aware control
- Smooth trajectories
- Slightly higher RMSE

### Naive Predictive
- Overshoot + instability
- Worst performer

---

## Takeaways

- Fast drift → **estimation-dominated regime**
- Kalman filtering is optimal baseline
- MPC becomes important when:
  - control bounds matter
  - hardware constraints apply

---

## Repo Context

Sequence:

- 06 → parameter phase diagram  
- 07 → constrained MPC  
- **08 → fast drift regime**

---

## Next

Notebook 09:

- multi-parameter coupling
- CGCS breakdown regimes
- control-estimation co-design
