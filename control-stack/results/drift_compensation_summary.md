# Drift Compensation Results

---

## Error Reduction

| Metric | Uncompensated | Compensated | Reduction |
|--------|--------------|-------------|-----------|
| Omega RMSE | 0.0429 | 0.0197 | **-54%** |
| Offset RMSE | 0.0334 | 0.00394 | **-88%** |
| Response RMSE | 0.0769 | 0.0302 | **-61%** |

---

## Phase-lock Stability

| Metric | Value |
|--------|------|
| Min phase-lock (uncompensated) | 0.978 |
| Min phase-lock (compensated) | 0.993 |
| Mean phase-lock (uncompensated) | 0.991 |
| Mean phase-lock (compensated) | 0.998 |
| Phase-lock threshold | 0.707 |
| All compensated blocks phase-locked | **TRUE** |

---

## Control Behavior

- Estimator: moving average
- Window size: 4
- Best tested window: *(see notebook output)*
- Drift tracking: smooth with minor lag

---

## Drift Characteristics

- Ω (frequency): oscillatory + moderate noise
- B (offset): slow monotonic drift
- Control performs best on low-frequency components

---

## Interpretation

Closed-loop drift compensation:

- stabilizes both parameters and observable response
- significantly reduces accumulated calibration error
- maintains phase-lock across all calibration blocks

The system remains well above the stability threshold throughout operation.

---

## Key Insight

Calibration alone is insufficient under drift.

Adding feedback control converts:

open-loop calibration → closed-loop stabilization

---

## Next Step

Upgrade estimator:

→ `02_kalman_drift_filter.ipynb`

Goal:

- reduce lag
- improve tracking of faster drift
- enable predictive compensation
