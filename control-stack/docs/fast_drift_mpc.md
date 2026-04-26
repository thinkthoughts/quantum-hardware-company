# Fast Drift MPC vs Kalman (Control Stack)

Controller robustness under faster Ω/B drift.

---

## Pipeline

fast drift → estimator tracking → bounded MPC comparison → robustness ranking

---

## Key Results

- Stabilizes calibration drift.
- Reduces response-level error.
- Preserves CGCS phase-lock stability.

---

## Figures

### Ω tracking and control command

![Ω tracking and control command](../figures/fast_drift_mpc/08_fast_drift_mpc_omega_tracking.png)

Kalman policies track fast Ω drift more directly than moving average.

---

### B tracking and control command

![B tracking and control command](../figures/fast_drift_mpc/08_fast_drift_mpc_offset_tracking.png)

Fast B drift exposes estimator lag and command sensitivity.

---

### Response-level error comparison

![Response-level error comparison](../figures/fast_drift_mpc/08_fast_drift_mpc_response_rmse_comparison.png)

Naive predictive control becomes unstable under fast drift.

---

### Control policy ranking

![Control policy ranking](../figures/fast_drift_mpc/08_fast_drift_mpc_policy_ranking_summary.png)

Scalar and joint Kalman policies are strongest practical controllers.

---

### MPC horizon sweep

![MPC horizon sweep](../figures/fast_drift_mpc/08_fast_drift_mpc_horizon_sweep.png)

Short prediction horizons perform best under fast drift.

---

### Command-bound sweep

![Command-bound sweep](../figures/fast_drift_mpc/08_fast_drift_mpc_command_bound_sweep.png)

Command bounds shape fast-drift response error.

---

### CGCS phase-lock stability

![CGCS phase-lock stability](../figures/fast_drift_mpc/08_fast_drift_mpc_cgcs_stability_comparison.png)

All policies remain above threshold, though naive predictive is less stable.

---

### Worst-case block comparison

![Worst-case block comparison](../figures/fast_drift_mpc/08_fast_drift_mpc_worst_case_block_comparison.png)

Worst-case block shows tracking differences under fast drift.

---

## Interpretation

Estimator quality and command constraints determine closed-loop response stability.

## Key Takeaway

Control performance is limited by estimator structure as much as controller design.

## Next Step

→ `09_coupled_drift_mpc.ipynb`
