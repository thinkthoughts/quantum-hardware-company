# JSON → Markdown Pipeline for `control-stack`

This pipeline generates both documentation and results summaries from JSON summary files.

## Files generated

For each notebook slug:

- `docs/<slug>.md`
- `results/<slug>_summary.md`

## Expected inputs

Put JSON summaries here:

```text
control-stack/results/<slug>_summary.json
```

Examples:

```text
control-stack/results/drift_compensation_summary.json
control-stack/results/kalman_drift_filter_summary.json
control-stack/results/joint_state_kalman_summary.json
control-stack/results/coupled_drift_mpc_summary.json
```

## Run

From repo root:

```bash
python control-stack/scripts/generate_control_stack_markdown.py
```

Or from inside `control-stack/`:

```bash
python scripts/generate_control_stack_markdown.py
```

## Figure path convention

Markdown image links use:

```text
../figures/<slug>/<figure_filename>.png
```

Notebook 09 currently follows the existing folder convention:

```text
../figures/fast_drift_mpc/09_coupled_drift_mpc_*.png
```

## Naming convention

Docs:

```text
docs/drift_compensation.md
docs/kalman_drift_filter.md
docs/control_policy_comparison.md
docs/velocity_state_kalman.md
docs/joint_state_kalman.md
docs/predictive_control.md
docs/constrained_mpc.md
docs/fast_drift_mpc.md
docs/coupled_drift_mpc.md
```

Results:

```text
results/drift_compensation_summary.md
results/kalman_drift_filter_summary.md
results/control_policy_comparison_summary.md
results/velocity_state_kalman_summary.md
results/joint_state_kalman_summary.md
results/predictive_control_summary.md
results/constrained_mpc_summary.md
results/fast_drift_mpc_summary.md
results/coupled_drift_mpc_summary.md
```
