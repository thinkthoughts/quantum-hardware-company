# Fast Drift MPC vs Kalman (Control Stack)

Fast-drift regime comparing estimation and predictive control under rapid Ω and B variation.

---

## Ω Tracking (Fast Drift)

![Omega tracking](../figures/fast_drift_mpc/08_fast_drift_mpc_omega_tracking.png)

Kalman filters track Ω drift closely with minimal lag.  
Moving average lags under rapid changes.  
MPC smooths response but slightly under-tracks peaks.

---

## Response-level error comparison

![Response error](../figures/fast_drift_mpc/08_fast_drift_mpc_response_rmse_comparison.png)

- Kalman achieves lowest RMSE  
- MPC reduces spikes vs naive predictive  
- Naive predictive shows instability  

---

## Control policy ranking

![Policy ranking](../figures/fast_drift_mpc/08_fast_drift_mpc_policy_ranking_summary.png)

Kalman methods dominate in fast drift regime.  
MPC improves over naive predictive but remains higher error than Kalman.

---

## MPC horizon sweep

![Horizon sweep](../figures/fast_drift_mpc/08_fast_drift_mpc_horizon_sweep.png)

Best performance at **H = 0**.  
Longer horizons introduce lag under fast drift.

---

## Command-bound sweep

![Command bound](../figures/fast_drift_mpc/08_fast_drift_mpc_command_bound_sweep.png)

Larger control bounds improve tracking.  
Optimal region ≈ 0.03.

---

## CGCS phase-lock stability

![CGCS stability](../figures/fast_drift_mpc/08_fast_drift_mpc_cgcs_stability_comparison.png)

All methods satisfy:

cos(θ) ≥ 1 / √(1² + 1²) ≈ 0.7071

Kalman remains closest to perfect alignment.  
MPC maintains stability with bounded deviation.

---

## Worst-case block behavior

![Worst case](../figures/fast_drift_mpc/08_fast_drift_mpc_worst_case_block_comparison.png)

Naive predictive overshoots strongly.  
MPC remains bounded.  
Kalman tracks most accurately.

---

## B (offset) tracking

![Offset tracking](../figures/fast_drift_mpc/08_fast_drift_mpc_offset_tracking.png)

Joint Kalman captures coupled drift behavior.  
MPC smooths control trajectory.  
Moving average lags.

---

## Key insight

Fast drift is **estimation-dominated**:

- Kalman filtering is optimal baseline  
- Prediction adds limited benefit  
- MPC improves stability under constraints  

---

## Next

Extend to:

- coupled Ω + B control  
- CGCS boundary breakdown  
- estimator–controller co-design
