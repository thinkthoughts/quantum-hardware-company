# Drift Compensation (Control Stack)

Closed-loop stabilization of quantum calibration parameters under drift.

---

## Pipeline

calibration → drift estimation → control update → stabilized response

This notebook demonstrates a minimal control loop:

- measure calibration parameters (Ω, B)
- estimate drift over time
- apply corrective control updates
- stabilize the observed quantum response

---

## Key Results

Closed-loop compensation reduces:

- parameter error (Ω, B)
- response-level error (observable physics)
- drift-induced misalignment

---

## Figures

### Response-level error reduction

![Response error](../figures/drift_compensation/control_05_response_error_reduction.png)

Compensation reduces response RMSE by ~60%, keeping measured signals aligned with target behavior.

---

### Frequency (Ω) error reduction

![Omega error](../figures/drift_compensation/control_03_omega_error_reduction.png)

Control reduces frequency drift error amplitude and variance.

---

### Offset (B) error reduction

![Offset error](../figures/drift_compensation/control_04_offset_error_reduction.png)

Offset drift is strongly suppressed (~88% reduction), indicating smooth low-frequency drift tracking.

---

### Control command trace

![Command trace](../figures/drift_compensation/control_02b_command_trace.png)

The estimator produces smooth corrective commands applied to hardware parameters.

---

### CGCS phase-lock stability

![CGCS stability](../figures/drift_compensation/control_07_cgcs_stability_comparison.png)

- All compensated blocks remain phase-locked
- Stability margin improves under control

---

### Window sweep (controller tuning)

![Window sweep](../figures/drift_compensation/control_08_window_sweep_response.png)

Shows tradeoff:

- small window → fast but noisy
- large window → smooth but lagged

---

### Improvement summary

![Improvement summary](../figures/drift_compensation/control_09_improvement_summary.png)

Compact view of overall control effectiveness.

---

## Interpretation

Drift alone causes gradual degradation of system performance.

Closed-loop control:

- tracks slow parameter drift
- suppresses noise
- stabilizes response-level physics

The system remains within the phase-lock constraint region throughout operation.

---

## Limitations

Current controller:

- uses moving-average estimation
- introduces lag in response to drift
- treats parameters independently (Ω, B)

---

## Next Step

Replace moving-average estimator with a state-space model:

→ `02_kalman_drift_filter.ipynb`

This will:

- reduce lag
- improve noise rejection
- enable predictive control
