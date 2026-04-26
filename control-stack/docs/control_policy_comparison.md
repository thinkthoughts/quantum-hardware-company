# Control Policy Comparison (Control Stack)

Policy-level comparison of no control, moving average, Kalman, predictive Kalman, and oracle baselines.

---

## Pipeline

drift model → policy controller → response simulation → policy ranking

---

## Key Results

- Stabilizes calibration drift.
- Reduces response-level error.
- Preserves CGCS phase-lock stability.

---

## Figures

### Parameter RMSE

![Parameter RMSE](../figures/control_policy_comparison/03_control_policy_comparison_parameter_rmse.png)

Parameter-level RMSE separates weak control from estimator-aware policies.

---

### Response-level error

![Response-level error](../figures/control_policy_comparison/03_control_policy_comparison_response_rmse_comparison.png)

Kalman control minimizes response error among practical policies.

---

### Policy ranking

![Policy ranking](../figures/control_policy_comparison/03_control_policy_comparison_policy_ranking_summary.png)

Ranking summarizes mean and worst-case response error.

---

### CGCS phase-lock stability

![CGCS phase-lock stability](../figures/control_policy_comparison/03_control_policy_comparison_cgcs_stability_comparison.png)

All policies remain above threshold, with Kalman policies closest to unity.

---

### Ω estimator comparison

![Ω estimator comparison](../figures/control_policy_comparison/03_control_policy_comparison_omega_estimator_comparison.png)

Kalman estimation removes moving-average lag.

---

### Offset estimator comparison

![Offset estimator comparison](../figures/control_policy_comparison/03_control_policy_comparison_offset_estimator_comparison.png)

Offset estimates show the lag/noise tradeoff across policies.

---

### Worst-case block comparison

![Worst-case block comparison](../figures/control_policy_comparison/03_control_policy_comparison_worst_case_block_comparison.png)

Worst-case response confirms practical control-policy differences.

---

## Interpretation

Estimator quality and command constraints determine closed-loop response stability.

## Key Takeaway

Control performance is limited by estimator structure as much as controller design.

## Next Step

→ `04_velocity_state_kalman.ipynb`
