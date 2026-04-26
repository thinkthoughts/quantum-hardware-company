# Joint-State Kalman Control (Notebook 05)

This notebook extends velocity-state estimation (Notebook 04) to a **joint-state Kalman filter** that models **coupled drift between Ω (Rabi frequency) and B (readout offset)**.

---

## Model

State vector:

    x = [Ω, B]^T

Process covariance:

    Q = [[q_Ω, q_cross],
         [q_cross, q_B]]

This introduces **cross-coupling between parameters**.

---

## Joint-State Control: Worst-Case Block

![joint worst case](../figures/joint_state_kalman/05_joint_state_kalman_worst_case_block_comparison.png)

- All Kalman variants track target closely  
- Joint Kalman aligns nearly with oracle  
- Moving average shows lag  
- No control deviates significantly  

---

## Ω (Rabi Frequency) Error Comparison

![omega error](../figures/joint_state_kalman/05_joint_state_kalman_omega_error_comparison.png)

- Joint Kalman suppresses oscillatory error  
- Independent scalar performs similarly but slightly noisier  
- Moving average lags phase  

---

## B (Offset) Error Comparison

![b error](../figures/joint_state_kalman/05_joint_state_kalman_offset_error_comparison.png)

- Joint Kalman stabilizes offset drift  
- Independent scalar nearly identical  
- Moving average underfits local variations  

---

## Readout Offset Estimation

![readout offset](../figures/joint_state_kalman/05_joint_state_kalman_offset_estimator_comparison.png)

- Joint Kalman produces smoother tracking  
- Measurement noise clearly reduced vs raw signal  

---

## Rabi Frequency Estimation

![rabi estimate](../figures/joint_state_kalman/05_joint_state_kalman_omega_estimator_comparison.png)

- Joint and independent Kalman overlap closely  
- Moving average shows lag bias  

---

## Response-Level Error Comparison

![response error](../figures/joint_state_kalman/05_joint_state_kalman_response_rmse_comparison.png)

- Joint Kalman consistently minimizes RMSE  
- Significant improvement vs moving average  
- Large gap vs no control  

---

## Policy Ranking

![policy ranking](../figures/joint_state_kalman/05_joint_state_kalman_policy_ranking_summary.png)

- Oracle = perfect reference  
- Joint Kalman = best practical method  
- Independent scalar nearly tied  
- Moving average and none much worse  

---

## Coupling Sweep

![coupling sweep](../figures/joint_state_kalman/05_joint_state_kalman_coupling_sweep.png)

- Optimal coupling ≈ 0.35  
- True Ω–B correlation ≈ 0  
- Indicates estimator benefits from **measurement coupling**  

---

## Phase-Lock Stability (CGCS)

![phase lock](../figures/joint_state_kalman/05_joint_state_kalman_cgcs_stability_comparison.png)

All methods satisfy:

    cos(θ) ≥ 1 / √(1² + 1²) ≈ 0.7071

Joint Kalman stays closest to:

    cos(θ) ≈ 1

---

## Key Takeaways

- Joint Kalman improves stability and RMSE  
- Gains over independent scalar are small but consistent  
- Optimal coupling emerges even without physical correlation  
- Control performance depends on **estimator structure**, not just dynamics  

---

## Next Step

Notebook 06:

- Add **predictive control (MPC-lite)**  
- Use joint-state forecasts to reduce lag and improve tracking  
