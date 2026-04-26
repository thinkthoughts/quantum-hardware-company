# Predictive Control (Control Stack)

MPC-lite predictive control built on scalar and joint Kalman estimates.

---

## Pipeline

Kalman estimate → short-horizon forecast → command update → response stabilization

---

## Key Results

- Stabilizes calibration drift.
- Reduces response-level error.
- Preserves CGCS phase-lock stability.

---

## Figures

### Response-level error comparison

![Response-level error comparison](../figures/predictive_control/06_predictive_control_response_rmse_comparison.png)

Predictive control can amplify error when forecast horizon and commands are not constrained.

---

### Policy ranking

![Policy ranking](../figures/predictive_control/06_predictive_control_policy_ranking_summary.png)

Joint Kalman remains stronger than naive predictive controllers in this regime.

---

### Ω estimate and command

![Ω estimate and command](../figures/predictive_control/06_predictive_control_omega_tracking.png)

MPC-lite commands can overshoot Ω when prediction is too aggressive.

---

### B estimate and command

![B estimate and command](../figures/predictive_control/06_predictive_control_offset_tracking.png)

B commands show the same estimation/control tradeoff.

---

### Command smoothness

![Command smoothness](../figures/predictive_control/06_predictive_control_command_smoothness.png)

Command smoothness diagnostics reveal aggressive predictive updates.

---

### Horizon sweep

![Horizon sweep](../figures/predictive_control/06_predictive_control_horizon_sweep.png)

Shorter horizons perform best in this synthetic setting.

---

### CGCS phase-lock stability

![CGCS phase-lock stability](../figures/predictive_control/06_predictive_control_cgcs_stability_comparison.png)

All policies remain phase-locked despite prediction overshoot.

---

### Worst-case block comparison

![Worst-case block comparison](../figures/predictive_control/06_predictive_control_worst_case_block_comparison.png)

Worst-case response shows predictive control lag/overshoot effects.

---

## Interpretation

Estimator quality and command constraints determine closed-loop response stability.

## Key Takeaway

Control performance is limited by estimator structure as much as controller design.

## Next Step

→ `07_constrained_mpc.ipynb`
