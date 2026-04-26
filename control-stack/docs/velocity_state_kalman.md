# Velocity-State Kalman (Control Stack)

Kalman filtering with drift-rate states for Ω and B control.

---

## Pipeline

measured drift → position/velocity state estimate → bounded control → response stabilization

---

## Key Results

- Stabilizes calibration drift.
- Reduces response-level error.
- Preserves CGCS phase-lock stability.

---

## Figures

### Response-level error comparison

![Response-level error comparison](../figures/velocity_state_kalman/04_velocity_state_kalman_response_rmse_comparison.png)

Velocity-state filtering improves response tracking while exposing prediction tradeoffs.

---

### Policy ranking

![Policy ranking](../figures/velocity_state_kalman/04_velocity_state_kalman_policy_ranking_summary.png)

Scalar Kalman remains strongest; velocity-state filtered control is competitive.

---

### Ω error comparison

![Ω error comparison](../figures/velocity_state_kalman/04_velocity_state_kalman_omega_error_comparison.png)

Velocity-state filtering reduces Ω error but predictive mode can overshoot.

---

### Offset error comparison

![Offset error comparison](../figures/velocity_state_kalman/04_velocity_state_kalman_offset_error_comparison.png)

Offset error remains tightly controlled under Kalman variants.

---

### Ω estimator comparison

![Ω estimator comparison](../figures/velocity_state_kalman/04_velocity_state_kalman_omega_estimator_comparison.png)

Velocity-state estimates capture drift-rate structure.

---

### Offset estimator comparison

![Offset estimator comparison](../figures/velocity_state_kalman/04_velocity_state_kalman_offset_estimator_comparison.png)

Offset tracking remains stable despite noisy measurements.

---

### Drift-rate estimates

![Drift-rate estimates](../figures/velocity_state_kalman/04_velocity_state_kalman_drift_rate_estimates.png)

The velocity-state model exposes estimated drift rates for Ω and B.

---

### Tuning sweep

![Tuning sweep](../figures/velocity_state_kalman/04_velocity_state_kalman_tuning_sweep.png)

Velocity process variance controls responsiveness and noise amplification.

---

### CGCS phase-lock stability

![CGCS phase-lock stability](../figures/velocity_state_kalman/04_velocity_state_kalman_cgcs_stability_comparison.png)

All controlled policies remain phase-locked.

---

### Worst-case block comparison

![Worst-case block comparison](../figures/velocity_state_kalman/04_velocity_state_kalman_worst_case_block_comparison.png)

Worst-case response shows filtered velocity-state control remains aligned.

---

## Interpretation

Estimator quality and command constraints determine closed-loop response stability.

## Key Takeaway

Control performance is limited by estimator structure as much as controller design.

## Next Step

→ `05_joint_state_kalman.ipynb`
