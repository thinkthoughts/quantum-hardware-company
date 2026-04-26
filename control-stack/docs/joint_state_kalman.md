# Joint-State Kalman Control (Control Stack)

Joint-state Kalman filtering for coupled Ω and B drift estimation.

---

## Pipeline

coupled state estimate → covariance-aware update → joint correction → response stabilization

---

## Key Results

- Stabilizes calibration drift.
- Reduces response-level error.
- Preserves CGCS phase-lock stability.

---

## Figures

### Worst-case block comparison

![Worst-case block comparison](../figures/joint_state_kalman/05_joint_state_kalman_worst_case_block_comparison.png)

Joint Kalman aligns closely with oracle in the worst-case block.

---

### Ω error comparison

![Ω error comparison](../figures/joint_state_kalman/05_joint_state_kalman_omega_error_comparison.png)

Joint Kalman suppresses oscillatory Ω error.

---

### B error comparison

![B error comparison](../figures/joint_state_kalman/05_joint_state_kalman_offset_error_comparison.png)

Joint Kalman stabilizes offset drift with near-scalar performance.

---

### Readout offset estimation

![Readout offset estimation](../figures/joint_state_kalman/05_joint_state_kalman_offset_estimator_comparison.png)

Measurement noise is reduced while the offset trend is preserved.

---

### Rabi frequency estimation

![Rabi frequency estimation](../figures/joint_state_kalman/05_joint_state_kalman_omega_estimator_comparison.png)

Joint and independent Kalman estimates overlap closely.

---

### Response-level error comparison

![Response-level error comparison](../figures/joint_state_kalman/05_joint_state_kalman_response_rmse_comparison.png)

Joint Kalman consistently minimizes practical response RMSE.

---

### Policy ranking

![Policy ranking](../figures/joint_state_kalman/05_joint_state_kalman_policy_ranking_summary.png)

Joint Kalman is the best practical method, with scalar Kalman nearly tied.

---

### Coupling sweep

![Coupling sweep](../figures/joint_state_kalman/05_joint_state_kalman_coupling_sweep.png)

Moderate covariance coupling improves estimator fit.

---

### Covariance diagnostics

![Covariance diagnostics](../figures/joint_state_kalman/05_joint_state_kalman_covariance_diagnostics.png)

Posterior covariance diagnostics expose estimator coupling behavior.

---

### CGCS phase-lock stability

![CGCS phase-lock stability](../figures/joint_state_kalman/05_joint_state_kalman_cgcs_stability_comparison.png)

All policies remain well above the 45° threshold.

---

## Interpretation

Estimator quality and command constraints determine closed-loop response stability.

## Key Takeaway

Control performance is limited by estimator structure as much as controller design.

## Next Step

→ `06_predictive_control.ipynb`
