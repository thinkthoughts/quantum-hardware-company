# Coupled Drift MPC Results Summary

---

## Configuration

- Notebook: `09_coupled_drift_mpc.ipynb`
- Drift regime: coupled Ω/B drift
- Figure directory: `figures/fast_drift_mpc/`
- Phase-lock threshold: 0.7071

---

## Policy Ranking

| Rank | Policy | Mean RMSE | Max RMSE |
|------|--------|----------:|---------:|
| 1 | oracle | 0.000 | 0.000 |
| 2 | joint_kalman | 0.008 | 0.019 |
| 3 | scalar_kalman | 0.008 | 0.019 |
| 4 | none | 0.008 | 0.020 |
| 5 | coupled_mpc | 0.017 | 0.047 |
| 6 | naive_predictive | 0.034 | 0.083 |
| 7 | moving_average | 0.051 | 0.109 |

---

## Control Parameter Sweeps

| Sweep | Current | Best Tested | Interpretation |
|-------|--------:|------------:|----------------|
| Ω command bound | 0.030 | 0.045 | Larger bound improves response RMSE |
| Joint coupling | 0.25 | 0.35 | Moderate covariance coupling improves estimator fit |

---

## Phase-Lock Stability

| Metric | Result |
|--------|--------|
| Threshold | 0.7071 |
| All policies above threshold | TRUE |
| Practical stability region | near 1.0 cosine similarity |

---

## Key Observations

### Joint Kalman

- Best practical controller in this notebook
- Tracks coupled Ω/B drift without large command excursions
- Nearly tied with scalar Kalman, but benefits from coupling structure

---

### Coupled MPC

- Improves over naive predictive control
- Still worse than joint/scalar Kalman for this simulated regime
- Sensitive to command-bound tuning

---

### Moving Average

- Performs worst among non-naive controllers
- Lags under coupled and faster drift
- Not suitable for correlated drift regimes

---

## Interpretation

Coupled drift does not automatically require aggressive MPC.

The main gain comes from better state estimation:

    moving average → scalar Kalman → joint Kalman

MPC only helps when bounded commands are tuned well and estimation is already stable.

---

## Key Takeaway

Coupled drift is mainly **estimation-limited**.

Joint Kalman provides the strongest practical control baseline for Notebook 09.

---

## Next Step

Notebook 10 should test robustness under:

- higher measurement noise
- burst noise / outliers
- adaptive covariance tuning
- fallback safety policies
