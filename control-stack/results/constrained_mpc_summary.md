# Constrained MPC Results Summary

---

## Configuration

Blocks: 48  
Moving average window: 4  

MPC:
- horizon (naive): 5
- horizon (constrained): 1

Constraints:
- εΩ = 0.006
- εB = 0.003

Regularization:
- λ = 25.0

---

## Optimal Parameters

Constraint sweep:
- best εΩ ≈ 0.001

Regularization:
- best λ ≈ 100

---

## Policy Ranking

| Policy           | Mean RMSE | Max RMSE |
|-----------------|----------|----------|
| oracle          | ~0       | ~0       |
| joint_kalman    | 0.00449  | 0.01134  |
| constrained_mpc | 0.01160  | 0.01848  |
| moving_average  | 0.03275  | 0.06887  |
| naive_mpc       | 0.07214  | 0.15111  |
| none            | 0.08509  | 0.14491  |

---

## Phase-Lock (CGCS)

All policies satisfy:

    cos(θ) ≥ 0.7071

Constrained MPC:

- stable
- slightly degraded vs Kalman
- far better than naive MPC

---

## Key Observations

### Naive vs Constrained MPC

- naive MPC unstable (overshoot)
- constrained MPC stabilizes control

---

### Control Insight

Prediction introduces noise unless bounded.

    unconstrained prediction → instability  
    constrained prediction → usable control  

---

## Conclusion

Constrained MPC:

- improves predictive control stability
- reduces oscillations
- does not outperform Kalman filtering

---

## Next

Notebook 08:

- fast drift regimes
- identify where MPC > Kalman
