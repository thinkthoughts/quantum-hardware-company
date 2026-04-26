# calibration

Measurement-first layer of quantum-hardware-company.

This directory defines system behavior through experiment, fitting, and residual analysis.

## Principle

Calibration is where hardware becomes real.

All downstream systems (noise mitigation, control stack, hardware design) depend on measured behavior, not assumptions.

## Initial Focus

* Rabi oscillations (frequency + amplitude calibration)
* Ramsey fringes (dephasing + detuning)
* Randomized benchmarking (gate fidelity)
* Drift tracking (stability over time)

## CGCS / Triplet-Phase-Lock framing

* Constraint → signal > noise
* Stability threshold: cosθ ≥ 1/√(1² + 1²)
* Residuals are treated as structure, not discarded error

## First Deliverable

`rabi/rabi_calibration.ipynb`

Includes:

* Synthetic or experimental data
* Sinusoidal fit
* Residual analysis
* Phase-lock interpretation
