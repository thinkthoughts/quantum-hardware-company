# Predictive Control Results Summary

## Configuration

- Blocks: 48
- Moving average window: 4
- MPC horizon: 5

Best horizon (sweep):

    H = 1

---

## Noise Parameters

Process noise:

- q_Ω = 8.0e-04
- q_B = 1.0e-05
- q_cross ≈ 3.13e-05

Measurement noise:

- r_Ω ≈ 3.27e-06
- r_B ≈ 3.35e-05

---

## Phase-Lock Threshold

    cos(θ) ≥ 0.7071

---

## Policy Ranking

| Rank | Policy        | Mean RMSE | Max RMSE |
|------|--------------|----------|----------|
| 1    | oracle        | ~0       | ~0       |
| 2    | joint_kalman  | 0.00449  | 0.01134  |
| 3    | scalar_kalman | 0.00455  | 0.01130  |
| 4    | moving_average| 0.03275  | 0.06887  |
| 5    | mpc_joint     | 0.07214  | 0.15111  |
| 6    | mpc_scalar    | 0.07242  | 0.15115  |
| 7    | none          | 0.08509  | 0.14491  |

---

## Phase-Lock Metrics

| Policy        | Min Cosine | Mean Cosine | Max Angle (deg) |
|--------------|------------|-------------|-----------------|
| joint_kalman  | 0.999915   | 0.999978    | 0.75°           |
| scalar_kalman | 0.999916   | 0.999978    | 0.74°           |
| moving_average| 0.993330   | 0.998072    | 6.62°           |
| mpc_joint     | 0.968398   | 0.990572    | 14.44°          |
| mpc_scalar    | 0.968419   | 0.990507    | 14.44°          |
| none          | 0.972215   | 0.989786    | 13.54°          |

All policies remain above CGCS threshold.

---

## Key Observations

### Kalman vs MPC

- Kalman filtering achieves lowest RMSE
- MPC increases both mean and worst-case error
- Prediction introduces instability

---

### Horizon Effect

- Optimal:

    H = 1

- Larger horizons worsen performance:

    prediction error accumulates

---

### Control Behavior

- MPC commands are less smooth
- Over-correction observed in Ω and B
- Phase distortion increases error

---

### Stability vs Performance

- All methods remain CGCS-stable
- Performance degradation occurs without instability

---

## Conclusion

Predictive control (MPC-lite):

- does not improve performance under current model
- introduces additional error due to imperfect prediction
- confirms that:

> **Accurate estimation is more valuable than naive prediction**

---

## Next Direction

- Constrained MPC (regularization)
- Kalman-consistent prediction model
- Δ-control (relative command updates)
- Adaptive horizon selection
