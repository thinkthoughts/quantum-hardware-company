# Kalman Drift Filter (Control Stack)

State-space drift estimation for Rabi frequency (Ω) and readout offset (B).

---

## Pipeline

calibration → drift measurement → Kalman estimate → compensation → stabilized response

This notebook upgrades the first drift-compensation loop by replacing moving-average smoothing with a Kalman state estimator.

---

## Key Results

Kalman filtering improves:

- Ω drift tracking
- response-level stabilization
- CGCS phase-lock margin
- lag reduction vs moving average

---

## Figures

### Response-level error comparison

![Response error](../figures/kalman_drift_filter/kalman_06_response_error_comparison.png)

Kalman control reduces response RMSE to near-zero across calibration blocks, outperforming moving-average compensation.

---

### Frequency (Ω) estimator comparison

![Omega estimator](../figures/kalman_drift_filter/kalman_01_omega_estimator_comparison.png)

Kalman filtering tracks Ω drift with far less lag than the moving-average estimator.

---

### Offset (B) estimator comparison

![Offset estimator](../figures/kalman_drift_filter/kalman_02_offset_estimator_comparison.png)

Kalman filtering smooths offset measurements while preserving the slow drift trend.

---

### Kalman gain trace

![Kalman gain](../figures/kalman_drift_filter/kalman_03_gain_trace.png)

Kalman gain shows how strongly each parameter update trusts new calibration measurements.

---

### Frequency error comparison

![Omega error](../figures/kalman_drift_filter/kalman_04_omega_error_comparison.png)

Kalman compensation nearly eliminates Ω error relative to target.

---

### Offset error comparison

![Offset error](../figures/kalman_drift_filter/kalman_05_offset_error_comparison.png)

Both moving-average and Kalman control suppress offset drift, with Kalman slightly improving stability.

---

### Example block comparison

![Example block](../figures/kalman_drift_filter/kalman_07_example_block_comparison.png)

A worst-case block shows Kalman compensation closely overlays the target response.

---

### CGCS phase-lock stability

![CGCS stability](../figures/kalman_drift_filter/kalman_08_cgcs_stability_comparison.png)

All Kalman-controlled blocks remain phase-locked with cosine similarity near 1.

---

### Improvement summary

![Improvement summary](../figures/kalman_drift_filter/kalman_09_improvement_summary.png)

Kalman filtering improves Ω, offset, and response-level error reduction relative to moving-average control.

---

### Kalman tuning sweep

![Kalman tuning](../figures/kalman_drift_filter/kalman_10_q_sweep_response.png)

Process-noise tuning shows a near-optimal region for Ω drift responsiveness.

---

## Interpretation

Moving-average control reduces error but introduces lag.

Kalman filtering:

- predicts drift as a latent state
- updates from calibration evidence
- reduces lag
- preserves noise rejection
- stabilizes response-level physics

---

## Limitations

Current filter:

- uses independent 1D filters for Ω and B
- does not model Ω/B covariance
- does not yet use one-step-ahead predictive control

---

## Next Step

Benchmark policies:

→ `03_control_policy_comparison.ipynb`

This will compare:

- no compensation
- moving average
- Kalman
- predictive Kalman
- oracle baseline
