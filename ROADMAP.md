# Roadmap — quantum-hardware-company

## Principle

Start where physics is measurable.

Calibration and noise define system reality.

---

## Phase 0 — Foundation (Now)

**Goal:** Establish measurable system behavior.

### Start: `calibration/`

Focus areas:

* Rabi oscillations
* Ramsey fringes
* Randomized Benchmarking (RB / IRB)
* Drift tracking

Outputs:

* Fit parameters (Ω, T₁, T₂, detuning)
* Residual structure (not just error bars)
* Stability over time

CGCS framing:

* Constraint → signal > noise
* Phase-lock threshold: cosθ ≥ 1/√(1² + 1²) (≈ 45°)

Deliverable:

* First calibration notebook (publishable-quality)
* Figures + residual analysis

---

## Phase 1 — Noise as Structure

**Goal:** Turn deviations into models.

### Build: `noise-mitigation/`

Focus areas:

* Lindblad noise models
* Effective noise:

  * γ_eff = γ + λγφ
* Filtering + shielding strategies
* Residual structure analysis (non-random noise)

Outputs:

* Parameterized noise models
* Identification of structured vs stochastic error
* Phase-lock survival regions

CGCS framing:

* Systems remain stable when constraints hold (≥ 45°)
* Noise = deviation from constraint, not “random failure”

Deliverable:

* Notebook: noise model + validation
* Visual: phase diagram (stable vs unstable regions)

---

## Phase 2 — Control Emerges from Constraints

**Goal:** Build control informed by real system behavior.

### Then: `control-stack/`

Focus areas:

* Pulse definitions (Rabi, Ramsey, CZ, etc.)
* Sequencing engine
* Experiment loops (calibrate → update → rerun)
* Hardware abstraction layer

Outputs:

* Executable experiment pipelines
* Closed-loop calibration routines

Constraint:

* Control must reflect calibration + noise realities
* No “idealized” control without measured grounding

---

## Phase 3 — Hardware Expression

**Goal:** Connect models to physical implementation.

### Expand into:

* `electrode-geometries/`
* `trap-layouts/`
* `fabrication/`
* `control-electronics/`

Focus:

* Geometry ↔ field ↔ control coupling
* Fabrication tolerances → noise sources
* Electronics → timing + filtering constraints

Outputs:

* Parametric designs
* Simulation ↔ calibration alignment

---

## Phase 4 — System Integration

**Goal:** Full-stack quantum hardware capability.

Integration loop:

calibration → noise → control → hardware → calibration

Outputs:

* Stable operating regimes
* Reproducible gate performance
* Performance benchmarks (fidelity, stability)

---

## Positioning

Comparable systems are developed by organizations like IonQ, where performance advantage comes from:

* Calibration precision
* Noise suppression
* Hardware stability

This repository prioritizes:

* Open, reproducible calibration workflows
* Structured noise understanding
* Constraint-based system design (CGCS)

---

## Guiding Rule

Start where physics shows up.

That is calibration.
