# Drift Compensation Results

## Error Reduction

- Omega RMSE: 0.0429 → 0.0197 (**-54%**)
- Offset RMSE: 0.0334 → 0.00394 (**-88%**)
- Response RMSE: 0.0769 → 0.0302 (**-61%**)

## Phase-lock Stability

- Min (uncompensated): 0.978
- Min (compensated): 0.993
- All blocks phase-locked: TRUE

## Control Behavior

- Estimator: moving average (window = 4)
- Best tested window: {from notebook output}
- Drift tracked with low noise but slight lag

## Interpretation

Closed-loop compensation stabilizes response-level physics under drift.

Next step: replace moving average with Kalman filter.
