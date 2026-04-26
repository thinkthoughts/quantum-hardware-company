# Kalman Drift Filter (Control Stack)

State-space drift filtering for quantum control calibration.

---

## Pipeline

calibration → Kalman estimation → control update → stabilized response

---

## Key Results

- Stabilizes calibration drift.
- Reduces response-level error.
- Preserves CGCS phase-lock stability.

---

## Figures

### Response-level error comparison

![Response-level error comparison](../figures/kalman_drift_filter/02_kalman_drift_filter_response_rmse_comparison.png)

Kalman filtering sharply reduces response-level RMSE relative to moving-average control.

---

### Rabi frequency error comparison

![Rabi frequency error comparison](../figures/kalman_drift_filter/02_kalman_drift_filter_omega_error_comparison.png)

Kalman estimation suppresses Ω error with minimal lag.

---

### Readout offset error comparison

![Readout offset error comparison](../figures/kalman_drift_filter/02_kalman_drift_filter_offset_error_comparison.png)

Kalman filtering stabilizes low-frequency offset drift.

---

### Rabi frequency drift estimator

![Rabi frequency drift estimator](../figures/kalman_drift_filter/02_kalman_drift_filter_omega_estimator_comparison.png)

The Kalman estimate tracks measured Ω drift more closely than the moving average.

---

### Readout offset drift estimator

![Readout offset drift estimator](../figures/kalman_drift_filter/02_kalman_drift_filter_offset_estimator_comparison.png)

The Kalman estimate smooths noisy B measurements while preserving trend.

---

### Kalman gain

![Kalman gain](../figures/kalman_drift_filter/02_kalman_drift_filter_kalman_gain.png)

Gain diagnostics show how measurement updates are weighted.

---

### Tuning sweep

![Tuning sweep](../figures/kalman_drift_filter/02_kalman_drift_filter_tuning_sweep.png)

Process variance tuning identifies stable low-RMSE regimes.

---

### Control improvement

![Control improvement](../figures/kalman_drift_filter/02_kalman_drift_filter_control_improvement.png)

Kalman filtering improves over moving average across key metrics.

---

### CGCS phase-lock stability

![CGCS phase-lock stability](../figures/kalman_drift_filter/02_kalman_drift_filter_cgcs_stability_comparison.png)

All Kalman-controlled blocks remain phase-locked.

---

### Worst-case block comparison

![Worst-case block comparison](../figures/kalman_drift_filter/02_kalman_drift_filter_worst_case_block_comparison.png)

Worst-case response alignment improves under Kalman control.

---

## Interpretation

Estimator quality and command constraints determine closed-loop response stability.

## Key Takeaway

Control performance is limited by estimator structure as much as controller design.

## Next Step

→ `03_control_policy_comparison.ipynb`
