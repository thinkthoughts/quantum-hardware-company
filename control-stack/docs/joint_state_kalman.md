# Joint-State Kalman Control (Notebook 05)

This notebook extends velocity-state estimation (Notebook 04) to a **joint-state Kalman filter** that models **coupled drift between Ω (Rabi frequency) and B (readout offset)**.

The goal is to test whether **explicit covariance modeling between parameters** improves control performance beyond independent filtering.

---

## Model

State vector:

    x = [Ω, B]^T

Dynamics:

    x_{k+1} = A x_k + w_k

    A = [[1, 0],
         [0, 1]]

Process noise covariance:

    Q = [[q_Ω, q_cross],
         [q_cross, q_B]]

Measurement model:

    z_k = H x_k + v_k

    H = identity

---

## Key Extension

Unlike independent filters, this model introduces:

    q_cross ≠ 0

which allows **Ω and B estimates to influence each other** through the covariance matrix.

---

## Experimental Setup

- Drift processes:
  - Ω drift: smooth sinusoidal + noise
  - B drift: slow monotonic + noise
- Measurement noise:
  - Ω: low variance
  - B: higher variance

- Compared policies:
  - none (no correction)
  - moving_average
  - independent_scalar Kalman
  - joint Kalman
  - oracle (ground truth)

---

## CGCS Stability Criterion

Phase-lock defined as:

    cos(θ) ≥ 1 / √(1² + 1²)

Numerically:

    cos(θ) ≥ 0.7071

All policies are evaluated against this threshold.

---

## Key Findings

### 1. Joint estimation improves response fidelity

- Joint Kalman slightly outperforms independent scalar filtering
- Improvement is small but consistent across blocks

### 2. Optimal coupling is non-zero

- Best coupling coefficient ≈ 0.35
- True Ω–B correlation ≈ 0

Interpretation:

> Optimal estimation covariance reflects **measurement structure**, not physical correlation.

---

### 3. Drift estimation behavior

- Ω estimation:
  - both filters perform similarly
- B estimation:
  - joint filter slightly smoother and more stable

---

### 4. Control-level impact

- Both Kalman methods:
  - dramatically reduce response error vs baseline
- Joint filter:
  - improves worst-case and mean response RMSE

---

### 5. Phase-lock stability

- All policies remain above CGCS threshold
- Joint Kalman maintains tighter clustering near:

    cos(θ) ≈ 1

---

## Interpretation

Joint-state filtering provides:

- robustness to measurement noise
- implicit correction of cross-parameter estimation errors
- improved downstream control stability

Even when physical coupling is negligible, **estimation coupling improves control performance**.

---

## Next Step

Notebook 06:

- Incorporate **predictive control (MPC-lite)**
- Use Kalman state forecasts to reduce lag and improve tracking
