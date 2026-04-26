# Coupled Drift MPC (Control Stack)

Coupled Ω/B drift with covariance-aware estimation and bounded MPC comparison.

---

## Pipeline

coupled drift → joint estimation → bounded control → response stabilization

---

## Key Results

- Stabilizes calibration drift.
- Reduces response-level error.
- Preserves CGCS phase-lock stability.

---

## Figures

### Ω tracking and control command

![Ω tracking and control command](../figures/fast_drift_mpc/09_coupled_drift_mpc_omega_tracking.png)

Joint Kalman and coupled MPC track Ω under correlated drift.

---

### B tracking and control command

![B tracking and control command](../figures/fast_drift_mpc/09_coupled_drift_mpc_offset_tracking.png)

Coupled estimation improves B tracking stability during correlated excursions.

---

### Response-level error comparison

![Response-level error comparison](../figures/fast_drift_mpc/09_coupled_drift_mpc_response_rmse_comparison.png)

Joint Kalman achieves lowest non-oracle error; coupled MPC improves over naive predictive control.

---

### Control policy ranking

![Control policy ranking](../figures/fast_drift_mpc/09_coupled_drift_mpc_policy_ranking_summary.png)

Policy ranking shows estimator quality dominates response-level control performance.

---

### Command-bound sweep

![Command-bound sweep](../figures/fast_drift_mpc/09_coupled_drift_mpc_command_bound_sweep.png)

Increasing allowed ΔΩ reduces RMSE in the tested range.

---

### Joint Kalman coupling sweep

![Joint Kalman coupling sweep](../figures/fast_drift_mpc/09_coupled_drift_mpc_coupling_sweep.png)

Moderate covariance coupling improves estimator fit.

---

### CGCS phase-lock stability

![CGCS phase-lock stability](../figures/fast_drift_mpc/09_coupled_drift_mpc_cgcs_stability.png)

All methods remain above the 45° threshold.

---

### Worst-case block comparison

![Worst-case block comparison](../figures/fast_drift_mpc/09_coupled_drift_mpc_worst_case_block_comparison.png)

Coupled MPC reduces lag and improves alignment in the worst-case block.

---

## Interpretation

Estimator quality and command constraints determine closed-loop response stability.

## Key Takeaway

Control performance is limited by estimator structure as much as controller design.

## Next Step

→ `10_noise_burst_robustness.ipynb`
