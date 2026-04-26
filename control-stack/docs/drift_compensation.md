# Drift Compensation (Control Stack)

Closed-loop stabilization of quantum calibration parameters under drift.

---

## Pipeline

calibration → drift estimation → control update → stabilized response

---

## Key Results

- Stabilizes calibration drift.
- Reduces response-level error.
- Preserves CGCS phase-lock stability.

---

## Figures

### Response-level error reduction

![Response-level error reduction](../figures/drift_compensation/control_05_response_error_reduction.png)

Compensation reduces response RMSE, keeping measured signals aligned with target behavior.

---

### Frequency (Ω) error reduction

![Frequency (Ω) error reduction](../figures/drift_compensation/control_03_omega_error_reduction.png)

Control reduces frequency drift error amplitude and variance.

---

### Offset (B) error reduction

![Offset (B) error reduction](../figures/drift_compensation/control_04_offset_error_reduction.png)

Offset drift is strongly suppressed, indicating smooth low-frequency drift tracking.

---

### Control command trace

![Control command trace](../figures/drift_compensation/control_02b_command_trace.png)

The estimator produces smooth corrective commands applied to hardware parameters.

---

### CGCS phase-lock stability

![CGCS phase-lock stability](../figures/drift_compensation/control_07_cgcs_stability_comparison.png)

All compensated blocks remain phase-locked and stability margin improves under control.

---

### Window sweep

![Window sweep](../figures/drift_compensation/control_08_window_sweep_response.png)

Shows the tuning tradeoff between fast/noisy and smooth/lagged control.

---

### Improvement summary

![Improvement summary](../figures/drift_compensation/control_09_improvement_summary.png)

Compact view of overall control effectiveness.

---

## Interpretation

Estimator quality and command constraints determine closed-loop response stability.

## Key Takeaway

Control performance is limited by estimator structure as much as controller design.

## Next Step

→ `02_kalman_drift_filter.ipynb`
