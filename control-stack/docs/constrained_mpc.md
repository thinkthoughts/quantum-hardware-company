# Constrained MPC

This notebook extends predictive control (Notebook 06) by introducing **bounded control updates**:

- ΔΩ, ΔB constraints (ε)
- control regularization (λ)
- short-horizon MPC (H = 1)

---

## Model

State:

    x = [Ω, B]^T

Objective:

    minimize tracking error + λ · Δ-control penalty

Constraints:

    |ΔΩ| ≤ εΩ  
    |ΔB| ≤ εB  

---

## Phase-Lock Stability (CGCS)

![phase lock](../figures/constrained_mpc/07_constrained_mpc_cgcs_stability_comparison.png)

All policies satisfy:

    cos(θ) ≥ 1 / √(1² + 1²) ≈ 0.7071

Constrained MPC remains tightly near 1.

---

## Policy Ranking

![policy ranking](../figures/constrained_mpc/07_constrained_mpc_policy_ranking_summary.png)

- joint_kalman remains best practical method
- constrained_mpc improves over naive_mpc
- naive_mpc unstable under noise

---

## Worst-Case Block

![worst case](../figures/constrained_mpc/07_constrained_mpc_worst_case_block_comparison.png)

- naive MPC overshoots
- constrained MPC stabilizes
- Kalman aligns with oracle

---

## Response-Level Error

![response error](../figures/constrained_mpc/07_constrained_mpc_response_rmse_comparison.png)

- constrained MPC removes large spikes
- still higher RMSE than Kalman

---

## Ω Command Comparison

![omega command](../figures/constrained_mpc/07_constrained_mpc_omega_command_comparison.png)

- naive MPC oscillates
- constrained MPC smooths control
- Kalman remains lowest-noise

---

## B Command Comparison

![b command](../figures/constrained_mpc/07_constrained_mpc_offset_command_comparison.png)

- same structure as Ω
- constraints prevent overshoot

---

## Constraint Sweep (ε)

![constraint sweep](../figures/constrained_mpc/07_constrained_mpc_constraint_sweep.png)

- best εΩ ≈ 0.001
- current εΩ = 0.006 too loose

---

## Regularization Sweep (λ)

![regularization](../figures/constrained_mpc/07_constrained_mpc_regularization_sweep.png)

- best λ ≈ 100
- higher λ improves stability

---

## Key Takeaways

- constraints fix MPC instability
- prediction alone is not enough
- estimator quality dominates performance
