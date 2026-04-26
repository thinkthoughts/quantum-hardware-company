# Fast Drift MPC vs Kalman (Control Stack)

Fast-drift regime comparing estimation and predictive control under rapid Ω and B variation.

---

## Ω Tracking (Fast Drift)

![Omega tracking](../figures/fast_drift_mpc/08_fast_drift_mpc_omega_tracking.png)

Kalman filters track Ω drift closely with minimal lag.  
Moving average lags under rapid changes.  
MPC smooths response but slightly under-tracks peaks.

---

## Response-Level Error Comparison

![Response error](../figures/fast_drift_mpc/08_fast_drift_mpc_response_comparison.png)

- Kalman achieves lowest RMSE  
- MPC reduces spikes vs naive predictive  
- Naive predictive shows instability  

---

## Policy Ranking

![Policy ranking](../figures/fast_drift_mpc/08_fast_drift_mpc_policy_ranking.png)

Kalman methods dominate in fast drift regime.  
MPC improves over naive predictive but remains higher error than Kalman.

---

## Phase-Lock Stability (CGCS)

![CGCS stability](../figures/fast_drift_mpc/08_fast_drift_mpc_cgcs_stability.png)

All methods satisfy:

    cos(θ) ≥ 1 / √(1² + 1²) ≈ 0.7071

Kalman remains closest to perfect alignment.  
MPC maintains stability but with slightly reduced cosine similarity.

---

## Worst-Case Block Behavior

![Worst case](../figures/fast_drift_mpc/08_fast_drift_mpc_response_comparison.png)

Naive predictive overshoots strongly.  
MPC remains bounded under constraints.  
Kalman tracks target most accurately.

---

## B (Offset) Tracking

![Offset tracking](../figures/fast_drift_mpc/08_fast_drift_mpc_offset_tracking.png)

Joint Kalman captures coupled drift behavior.  
MPC smooths control trajectory.  
Moving average lags.

---

## Key Insight

Fast drift is **estimation-dominated**:

- Kalman filtering remains optimal baseline  
- Prediction adds limited benefit  
- Constraints improve stability but not accuracy  

---

## Next Step

Extend to:

- coupled multi-parameter control  
- CGCS breakdown regimes  
- adaptive estimator-control switching
