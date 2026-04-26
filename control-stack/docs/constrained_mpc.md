# Constrained MPC (Control Stack)

Command-bounded MPC for stabilizing predictive control updates.

---

## Pipeline

joint estimate → bounded predictive command → constrained update → stable response

---

## Key Results

- Stabilizes calibration drift.
- Reduces response-level error.
- Preserves CGCS phase-lock stability.

---

## Figures

### Response-level error comparison

![Response-level error comparison](../figures/constrained_mpc/07_constrained_mpc_response_rmse_comparison.png)

Constrained MPC reduces naive predictive overshoot but remains behind joint Kalman.

---

### Policy ranking

![Policy ranking](../figures/constrained_mpc/07_constrained_mpc_policy_ranking_summary.png)

Command bounds improve MPC relative to naive predictive control.

---

### Ω command comparison

![Ω command comparison](../figures/constrained_mpc/07_constrained_mpc_omega_command_comparison.png)

Constraints suppress aggressive Ω command excursions.

---

### B command comparison

![B command comparison](../figures/constrained_mpc/07_constrained_mpc_offset_command_comparison.png)

Bounded B commands remain closer to joint Kalman behavior.

---

### Command-bound sweep

![Command-bound sweep](../figures/constrained_mpc/07_constrained_mpc_command_bound_sweep.png)

Tighter bounds improve response RMSE in this regime.

---

### Regularization sweep

![Regularization sweep](../figures/constrained_mpc/07_constrained_mpc_regularization_sweep.png)

Regularization controls command aggressiveness.

---

### CGCS phase-lock stability

![CGCS phase-lock stability](../figures/constrained_mpc/07_constrained_mpc_cgcs_stability_comparison.png)

Constrained MPC stays phase-locked across all blocks.

---

### Worst-case block comparison

![Worst-case block comparison](../figures/constrained_mpc/07_constrained_mpc_worst_case_block_comparison.png)

Worst-case response improves relative to naive MPC.

---

## Interpretation

Estimator quality and command constraints determine closed-loop response stability.

## Key Takeaway

Control performance is limited by estimator structure as much as controller design.

## Next Step

→ `08_fast_drift_mpc_vs_kalman.ipynb`
