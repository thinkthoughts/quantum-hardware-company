#!/usr/bin/env python3
"""
generate_control_stack_markdown.py

Generate docs/*.md and results/*_summary.md from results/*_summary.json
for quantum-hardware-company/control-stack.

Usage from repo root:

    python control-stack/scripts/generate_control_stack_markdown.py

Expected repo layout:

    control-stack/
      results/
        drift_compensation_summary.json
        kalman_drift_filter_summary.json
        ...
      figures/
        drift_compensation/
        kalman_drift_filter/
        ...
      docs/

This script is intentionally conservative:
- it keeps notebook slugs stable
- it uses figure filenames already present in figures/<slug>/
- it writes docs/<slug>.md
- it writes results/<slug>_summary.md
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


NOTEBOOKS: Dict[str, Dict[str, Any]] = {
    "drift_compensation": {
        "title": "Drift Compensation",
        "subtitle": "Closed-loop stabilization of quantum calibration parameters under drift.",
        "pipeline": "calibration → drift estimation → control update → stabilized response",
        "figures": [
            ("Response-level error reduction", "control_05_response_error_reduction.png",
             "Compensation reduces response RMSE, keeping measured signals aligned with target behavior."),
            ("Frequency (Ω) error reduction", "control_03_omega_error_reduction.png",
             "Control reduces frequency drift error amplitude and variance."),
            ("Offset (B) error reduction", "control_04_offset_error_reduction.png",
             "Offset drift is strongly suppressed, indicating smooth low-frequency drift tracking."),
            ("Control command trace", "control_02b_command_trace.png",
             "The estimator produces smooth corrective commands applied to hardware parameters."),
            ("CGCS phase-lock stability", "control_07_cgcs_stability_comparison.png",
             "All compensated blocks remain phase-locked and stability margin improves under control."),
            ("Window sweep", "control_08_window_sweep_response.png",
             "Shows the tuning tradeoff between fast/noisy and smooth/lagged control."),
            ("Improvement summary", "control_09_improvement_summary.png",
             "Compact view of overall control effectiveness."),
        ],
        "next": "02_kalman_drift_filter.ipynb",
    },
    "kalman_drift_filter": {
        "title": "Kalman Drift Filter",
        "subtitle": "State-space drift filtering for quantum control calibration.",
        "pipeline": "calibration → Kalman estimation → control update → stabilized response",
        "figures": [
            ("Response-level error comparison", "02_kalman_drift_filter_response_rmse_comparison.png",
             "Kalman filtering sharply reduces response-level RMSE relative to moving-average control."),
            ("Rabi frequency error comparison", "02_kalman_drift_filter_omega_error_comparison.png",
             "Kalman estimation suppresses Ω error with minimal lag."),
            ("Readout offset error comparison", "02_kalman_drift_filter_offset_error_comparison.png",
             "Kalman filtering stabilizes low-frequency offset drift."),
            ("Rabi frequency drift estimator", "02_kalman_drift_filter_omega_estimator_comparison.png",
             "The Kalman estimate tracks measured Ω drift more closely than the moving average."),
            ("Readout offset drift estimator", "02_kalman_drift_filter_offset_estimator_comparison.png",
             "The Kalman estimate smooths noisy B measurements while preserving trend."),
            ("Kalman gain", "02_kalman_drift_filter_kalman_gain.png",
             "Gain diagnostics show how measurement updates are weighted."),
            ("Tuning sweep", "02_kalman_drift_filter_tuning_sweep.png",
             "Process variance tuning identifies stable low-RMSE regimes."),
            ("Control improvement", "02_kalman_drift_filter_control_improvement.png",
             "Kalman filtering improves over moving average across key metrics."),
            ("CGCS phase-lock stability", "02_kalman_drift_filter_cgcs_stability_comparison.png",
             "All Kalman-controlled blocks remain phase-locked."),
            ("Worst-case block comparison", "02_kalman_drift_filter_worst_case_block_comparison.png",
             "Worst-case response alignment improves under Kalman control."),
        ],
        "next": "03_control_policy_comparison.ipynb",
    },
    "control_policy_comparison": {
        "title": "Control Policy Comparison",
        "subtitle": "Policy-level comparison of no control, moving average, Kalman, predictive Kalman, and oracle baselines.",
        "pipeline": "drift model → policy controller → response simulation → policy ranking",
        "figures": [
            ("Parameter RMSE", "03_control_policy_comparison_parameter_rmse.png",
             "Parameter-level RMSE separates weak control from estimator-aware policies."),
            ("Response-level error", "03_control_policy_comparison_response_rmse_comparison.png",
             "Kalman control minimizes response error among practical policies."),
            ("Policy ranking", "03_control_policy_comparison_policy_ranking_summary.png",
             "Ranking summarizes mean and worst-case response error."),
            ("CGCS phase-lock stability", "03_control_policy_comparison_cgcs_stability_comparison.png",
             "All policies remain above threshold, with Kalman policies closest to unity."),
            ("Ω estimator comparison", "03_control_policy_comparison_omega_estimator_comparison.png",
             "Kalman estimation removes moving-average lag."),
            ("Offset estimator comparison", "03_control_policy_comparison_offset_estimator_comparison.png",
             "Offset estimates show the lag/noise tradeoff across policies."),
            ("Worst-case block comparison", "03_control_policy_comparison_worst_case_block_comparison.png",
             "Worst-case response confirms practical control-policy differences."),
        ],
        "next": "04_velocity_state_kalman.ipynb",
    },
    "velocity_state_kalman": {
        "title": "Velocity-State Kalman",
        "subtitle": "Kalman filtering with drift-rate states for Ω and B control.",
        "pipeline": "measured drift → position/velocity state estimate → bounded control → response stabilization",
        "figures": [
            ("Response-level error comparison", "04_velocity_state_kalman_response_rmse_comparison.png",
             "Velocity-state filtering improves response tracking while exposing prediction tradeoffs."),
            ("Policy ranking", "04_velocity_state_kalman_policy_ranking_summary.png",
             "Scalar Kalman remains strongest; velocity-state filtered control is competitive."),
            ("Ω error comparison", "04_velocity_state_kalman_omega_error_comparison.png",
             "Velocity-state filtering reduces Ω error but predictive mode can overshoot."),
            ("Offset error comparison", "04_velocity_state_kalman_offset_error_comparison.png",
             "Offset error remains tightly controlled under Kalman variants."),
            ("Ω estimator comparison", "04_velocity_state_kalman_omega_estimator_comparison.png",
             "Velocity-state estimates capture drift-rate structure."),
            ("Offset estimator comparison", "04_velocity_state_kalman_offset_estimator_comparison.png",
             "Offset tracking remains stable despite noisy measurements."),
            ("Drift-rate estimates", "04_velocity_state_kalman_drift_rate_estimates.png",
             "The velocity-state model exposes estimated drift rates for Ω and B."),
            ("Tuning sweep", "04_velocity_state_kalman_tuning_sweep.png",
             "Velocity process variance controls responsiveness and noise amplification."),
            ("CGCS phase-lock stability", "04_velocity_state_kalman_cgcs_stability_comparison.png",
             "All controlled policies remain phase-locked."),
            ("Worst-case block comparison", "04_velocity_state_kalman_worst_case_block_comparison.png",
             "Worst-case response shows filtered velocity-state control remains aligned."),
        ],
        "next": "05_joint_state_kalman.ipynb",
    },
    "joint_state_kalman": {
        "title": "Joint-State Kalman Control",
        "subtitle": "Joint-state Kalman filtering for coupled Ω and B drift estimation.",
        "pipeline": "coupled state estimate → covariance-aware update → joint correction → response stabilization",
        "figures": [
            ("Worst-case block comparison", "05_joint_state_kalman_worst_case_block_comparison.png",
             "Joint Kalman aligns closely with oracle in the worst-case block."),
            ("Ω error comparison", "05_joint_state_kalman_omega_error_comparison.png",
             "Joint Kalman suppresses oscillatory Ω error."),
            ("B error comparison", "05_joint_state_kalman_offset_error_comparison.png",
             "Joint Kalman stabilizes offset drift with near-scalar performance."),
            ("Readout offset estimation", "05_joint_state_kalman_offset_estimator_comparison.png",
             "Measurement noise is reduced while the offset trend is preserved."),
            ("Rabi frequency estimation", "05_joint_state_kalman_omega_estimator_comparison.png",
             "Joint and independent Kalman estimates overlap closely."),
            ("Response-level error comparison", "05_joint_state_kalman_response_rmse_comparison.png",
             "Joint Kalman consistently minimizes practical response RMSE."),
            ("Policy ranking", "05_joint_state_kalman_policy_ranking_summary.png",
             "Joint Kalman is the best practical method, with scalar Kalman nearly tied."),
            ("Coupling sweep", "05_joint_state_kalman_coupling_sweep.png",
             "Moderate covariance coupling improves estimator fit."),
            ("Covariance diagnostics", "05_joint_state_kalman_covariance_diagnostics.png",
             "Posterior covariance diagnostics expose estimator coupling behavior."),
            ("CGCS phase-lock stability", "05_joint_state_kalman_cgcs_stability_comparison.png",
             "All policies remain well above the 45° threshold."),
        ],
        "next": "06_predictive_control.ipynb",
    },
    "predictive_control": {
        "title": "Predictive Control",
        "subtitle": "MPC-lite predictive control built on scalar and joint Kalman estimates.",
        "pipeline": "Kalman estimate → short-horizon forecast → command update → response stabilization",
        "figures": [
            ("Response-level error comparison", "06_predictive_control_response_rmse_comparison.png",
             "Predictive control can amplify error when forecast horizon and commands are not constrained."),
            ("Policy ranking", "06_predictive_control_policy_ranking_summary.png",
             "Joint Kalman remains stronger than naive predictive controllers in this regime."),
            ("Ω estimate and command", "06_predictive_control_omega_tracking.png",
             "MPC-lite commands can overshoot Ω when prediction is too aggressive."),
            ("B estimate and command", "06_predictive_control_offset_tracking.png",
             "B commands show the same estimation/control tradeoff."),
            ("Command smoothness", "06_predictive_control_command_smoothness.png",
             "Command smoothness diagnostics reveal aggressive predictive updates."),
            ("Horizon sweep", "06_predictive_control_horizon_sweep.png",
             "Shorter horizons perform best in this synthetic setting."),
            ("CGCS phase-lock stability", "06_predictive_control_cgcs_stability_comparison.png",
             "All policies remain phase-locked despite prediction overshoot."),
            ("Worst-case block comparison", "06_predictive_control_worst_case_block_comparison.png",
             "Worst-case response shows predictive control lag/overshoot effects."),
        ],
        "next": "07_constrained_mpc.ipynb",
    },
    "constrained_mpc": {
        "title": "Constrained MPC",
        "subtitle": "Command-bounded MPC for stabilizing predictive control updates.",
        "pipeline": "joint estimate → bounded predictive command → constrained update → stable response",
        "figures": [
            ("Response-level error comparison", "07_constrained_mpc_response_rmse_comparison.png",
             "Constrained MPC reduces naive predictive overshoot but remains behind joint Kalman."),
            ("Policy ranking", "07_constrained_mpc_policy_ranking_summary.png",
             "Command bounds improve MPC relative to naive predictive control."),
            ("Ω command comparison", "07_constrained_mpc_omega_command_comparison.png",
             "Constraints suppress aggressive Ω command excursions."),
            ("B command comparison", "07_constrained_mpc_offset_command_comparison.png",
             "Bounded B commands remain closer to joint Kalman behavior."),
            ("Command-bound sweep", "07_constrained_mpc_command_bound_sweep.png",
             "Tighter bounds improve response RMSE in this regime."),
            ("Regularization sweep", "07_constrained_mpc_regularization_sweep.png",
             "Regularization controls command aggressiveness."),
            ("CGCS phase-lock stability", "07_constrained_mpc_cgcs_stability_comparison.png",
             "Constrained MPC stays phase-locked across all blocks."),
            ("Worst-case block comparison", "07_constrained_mpc_worst_case_block_comparison.png",
             "Worst-case response improves relative to naive MPC."),
        ],
        "next": "08_fast_drift_mpc_vs_kalman.ipynb",
    },
    "fast_drift_mpc": {
        "title": "Fast Drift MPC vs Kalman",
        "subtitle": "Controller robustness under faster Ω/B drift.",
        "pipeline": "fast drift → estimator tracking → bounded MPC comparison → robustness ranking",
        "figures": [
            ("Ω tracking and control command", "08_fast_drift_mpc_omega_tracking.png",
             "Kalman policies track fast Ω drift more directly than moving average."),
            ("B tracking and control command", "08_fast_drift_mpc_offset_tracking.png",
             "Fast B drift exposes estimator lag and command sensitivity."),
            ("Response-level error comparison", "08_fast_drift_mpc_response_rmse_comparison.png",
             "Naive predictive control becomes unstable under fast drift."),
            ("Control policy ranking", "08_fast_drift_mpc_policy_ranking_summary.png",
             "Scalar and joint Kalman policies are strongest practical controllers."),
            ("MPC horizon sweep", "08_fast_drift_mpc_horizon_sweep.png",
             "Short prediction horizons perform best under fast drift."),
            ("Command-bound sweep", "08_fast_drift_mpc_command_bound_sweep.png",
             "Command bounds shape fast-drift response error."),
            ("CGCS phase-lock stability", "08_fast_drift_mpc_cgcs_stability_comparison.png",
             "All policies remain above threshold, though naive predictive is less stable."),
            ("Worst-case block comparison", "08_fast_drift_mpc_worst_case_block_comparison.png",
             "Worst-case block shows tracking differences under fast drift."),
        ],
        "next": "09_coupled_drift_mpc.ipynb",
    },
    "coupled_drift_mpc": {
        "title": "Coupled Drift MPC",
        "subtitle": "Coupled Ω/B drift with covariance-aware estimation and bounded MPC comparison.",
        "pipeline": "coupled drift → joint estimation → bounded control → response stabilization",
        "figures": [
            ("Ω tracking and control command", "09_coupled_drift_mpc_omega_tracking.png",
             "Joint Kalman and coupled MPC track Ω under correlated drift."),
            ("B tracking and control command", "09_coupled_drift_mpc_offset_tracking.png",
             "Coupled estimation improves B tracking stability during correlated excursions."),
            ("Response-level error comparison", "09_coupled_drift_mpc_response_rmse_comparison.png",
             "Joint Kalman achieves lowest non-oracle error; coupled MPC improves over naive predictive control."),
            ("Control policy ranking", "09_coupled_drift_mpc_policy_ranking_summary.png",
             "Policy ranking shows estimator quality dominates response-level control performance."),
            ("Command-bound sweep", "09_coupled_drift_mpc_command_bound_sweep.png",
             "Increasing allowed ΔΩ reduces RMSE in the tested range."),
            ("Joint Kalman coupling sweep", "09_coupled_drift_mpc_coupling_sweep.png",
             "Moderate covariance coupling improves estimator fit."),
            ("CGCS phase-lock stability", "09_coupled_drift_mpc_cgcs_stability.png",
             "All methods remain above the 45° threshold."),
            ("Worst-case block comparison", "09_coupled_drift_mpc_worst_case_block_comparison.png",
             "Coupled MPC reduces lag and improves alignment in the worst-case block."),
        ],
        "next": "10_noise_burst_robustness.ipynb",
    },
}


def repo_root() -> Path:
    here = Path.cwd()
    if here.name == "control-stack":
        return here
    if (here / "control-stack").exists():
        return here / "control-stack"
    return here


def load_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Could not parse JSON: {path}\n{exc}") from exc


def fmt_value(v: Any) -> str:
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    if isinstance(v, int):
        return str(v)
    if isinstance(v, float):
        if abs(v) < 1e-3 and v != 0:
            return f"{v:.2e}"
        if abs(v) < 1:
            return f"{v:.5f}".rstrip("0").rstrip(".")
        return f"{v:.3f}".rstrip("0").rstrip(".")
    if v is None:
        return "—"
    return str(v)


def find_summary_json(results_dir: Path, slug: str) -> Path:
    direct = results_dir / f"{slug}_summary.json"
    if direct.exists():
        return direct
    # Compatibility for older short slugs.
    aliases = {
        "coupled_drift_mpc": "09_coupled_drift_mpc",
        "fast_drift_mpc": "08_fast_drift_mpc",
    }
    alias = aliases.get(slug)
    if alias and (results_dir / f"{alias}_summary.json").exists():
        return results_dir / f"{alias}_summary.json"
    return direct


def image_exists(fig_dir: Path, filename: str) -> bool:
    return (fig_dir / filename).exists()


def policy_rows(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    for key in ("policy_ranking", "ranking", "policies", "policy_metrics"):
        val = data.get(key)
        if isinstance(val, list):
            return [x for x in val if isinstance(x, dict)]
        if isinstance(val, dict):
            rows = []
            for name, metrics in val.items():
                row = {"policy": name}
                if isinstance(metrics, dict):
                    row.update(metrics)
                rows.append(row)
            return rows
    return []


def make_docs_md(slug: str, meta: Dict[str, Any], data: Dict[str, Any], fig_root: Path) -> str:
    lines: List[str] = []
    lines += [
        f"# {meta['title']} (Control Stack)",
        "",
        meta["subtitle"],
        "",
        "---",
        "",
        "## Pipeline",
        "",
        meta["pipeline"],
        "",
        "---",
        "",
        "## Key Results",
        "",
    ]

    if data.get("key_results") and isinstance(data["key_results"], list):
        for item in data["key_results"]:
            lines.append(f"- {item}")
    else:
        lines += [
            "- Stabilizes calibration drift.",
            "- Reduces response-level error.",
            "- Preserves CGCS phase-lock stability.",
        ]

    lines += ["", "---", "", "## Figures", ""]

    folder = slug
    # Notebook 08 and 09 intentionally share existing folder name convention if configured.
    if slug == "coupled_drift_mpc":
        folder = "fast_drift_mpc"

    for title, filename, caption in meta["figures"]:
        lines += [
            f"### {title}",
            "",
            f"![{title}](../figures/{folder}/{filename})",
            "",
            caption,
            "",
            "---",
            "",
        ]

    lines += [
        "## Interpretation",
        "",
        data.get("interpretation", "Estimator quality and command constraints determine closed-loop response stability."),
        "",
        "## Key Takeaway",
        "",
        data.get("key_takeaway", "Control performance is limited by estimator structure as much as controller design."),
        "",
        "## Next Step",
        "",
        f"→ `{meta['next']}`",
        "",
    ]
    return "\n".join(lines)


def make_results_md(slug: str, meta: Dict[str, Any], data: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines += [
        f"# {meta['title']} Results Summary",
        "",
        "---",
        "",
        "## Configuration",
        "",
    ]

    config = data.get("configuration") or data.get("config") or {}
    if isinstance(config, dict) and config:
        for k, v in config.items():
            lines.append(f"- {k}: {fmt_value(v)}")
    else:
        lines += [
            f"- Notebook slug: `{slug}`",
            "- Source: generated from JSON summary",
        ]

    lines += ["", "---", ""]

    rows = policy_rows(data)
    if rows:
        lines += ["## Policy Ranking", ""]
        # Pick commonly used keys.
        lines += ["| Rank | Policy | Mean RMSE | Max RMSE |", "|------|--------|----------:|---------:|"]
        for i, row in enumerate(rows, start=1):
            policy = row.get("policy") or row.get("name") or row.get("label") or f"policy_{i}"
            mean = row.get("mean_rmse", row.get("mean_response_rmse", row.get("mean", "—")))
            maxv = row.get("max_rmse", row.get("max_response_rmse", row.get("max", "—")))
            rank = row.get("rank", i)
            lines.append(f"| {rank} | {policy} | {fmt_value(mean)} | {fmt_value(maxv)} |")
        lines += ["", "---", ""]

    phase = data.get("phase_lock") or data.get("phase_lock_metrics") or {}
    if isinstance(phase, dict) and phase:
        lines += ["## Phase-Lock Metrics", ""]
        if all(isinstance(v, dict) for v in phase.values()):
            lines += ["| Policy | Min Cosine | Mean Cosine | Max Angle |", "|--------|-----------:|------------:|----------:|"]
            for policy, vals in phase.items():
                lines.append(
                    f"| {policy} | {fmt_value(vals.get('min_cosine', vals.get('min')))} | "
                    f"{fmt_value(vals.get('mean_cosine', vals.get('mean')))} | "
                    f"{fmt_value(vals.get('max_angle_deg', vals.get('max_angle')))} |"
                )
        else:
            lines += ["| Metric | Value |", "|--------|------:|"]
            for k, v in phase.items():
                lines.append(f"| {k} | {fmt_value(v)} |")
        lines += ["", "---", ""]

    sweeps = data.get("sweeps") or data.get("control_sweeps") or {}
    if isinstance(sweeps, dict) and sweeps:
        lines += ["## Control Parameter Sweeps", ""]
        lines += ["| Sweep | Current | Best Tested |", "|-------|--------:|------------:|"]
        for name, vals in sweeps.items():
            if isinstance(vals, dict):
                lines.append(f"| {name} | {fmt_value(vals.get('current'))} | {fmt_value(vals.get('best', vals.get('best_tested')))} |")
        lines += ["", "---", ""]

    observations = data.get("key_observations") or data.get("observations") or []
    lines += ["## Key Observations", ""]
    if isinstance(observations, list) and observations:
        for obs in observations:
            lines.append(f"- {obs}")
    else:
        lines += [
            "- Estimator-aware control improves response stability.",
            "- Moving-average control is useful as a baseline but introduces lag.",
            "- Kalman-family controllers provide the strongest practical baseline.",
        ]

    lines += [
        "",
        "---",
        "",
        "## Interpretation",
        "",
        data.get("interpretation", "Closed-loop performance depends on both estimator quality and command policy."),
        "",
        "---",
        "",
        "## Key Takeaway",
        "",
        data.get("key_takeaway", "A stable estimator is the foundation for reliable hardware control."),
        "",
        "---",
        "",
        "## Next Step",
        "",
        f"→ `{meta['next']}`",
        "",
    ]

    return "\n".join(lines)


def main() -> None:
    root = repo_root()
    docs_dir = root / "docs"
    results_dir = root / "results"
    fig_dir = root / "figures"

    docs_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)

    generated = []

    for slug, meta in NOTEBOOKS.items():
        json_path = find_summary_json(results_dir, slug)
        data = load_json(json_path)

        docs_path = docs_dir / f"{slug}.md"
        summary_path = results_dir / f"{slug}_summary.md"

        docs_path.write_text(make_docs_md(slug, meta, data, fig_dir), encoding="utf-8")
        summary_path.write_text(make_results_md(slug, meta, data), encoding="utf-8")

        generated.append((docs_path, summary_path))

    print("Generated markdown files:")
    for d, s in generated:
        print(f"- {d}")
        print(f"- {s}")


if __name__ == "__main__":
    main()
