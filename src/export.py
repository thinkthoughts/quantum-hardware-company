import os
import json
import matplotlib.pyplot as plt


class ExportManager:
    """
    Handles saving figures, results, and markdown summaries
    for residual-phase-lock notebooks.
    """

    def __init__(self, notebook_id, notebook_slug):
        self.id = notebook_id
        self.slug = notebook_slug

        self.fig_dir = "figures"
        self.results_dir = "results"
        self.docs_dir = "docs"

        os.makedirs(self.fig_dir, exist_ok=True)
        os.makedirs(self.results_dir, exist_ok=True)
        os.makedirs(self.docs_dir, exist_ok=True)

    # ------------------------
    # Figures
    # ------------------------
    def save_fig(self, name):
        path = f"{self.fig_dir}/{self.id}_{name}.png"
        plt.savefig(path, dpi=220, bbox_inches="tight")
        print(f"[export] saved figure: {path}")

    # ------------------------
    # Results
    # ------------------------
    def save_csv(self, df, name):
        path = f"{self.results_dir}/{self.id}_{name}.csv"
        df.to_csv(path, index=False)
        print(f"[export] saved csv: {path}")

    def save_json(self, obj, name):
        path = f"{self.results_dir}/{self.id}_{name}.json"
        with open(path, "w") as f:
            json.dump(obj, f, indent=2)
        print(f"[export] saved json: {path}")

    # ------------------------
    # Markdown
    # ------------------------
    def write_md(self, title, metrics_dict, figure_names, interpretation=None):
        """
        Generate a clean markdown summary for the notebook.
        """

        md_path = f"{self.docs_dir}/{self.id}_{self.slug}.md"

        # Metrics table
        metrics_lines = "\n".join(
            [f"| {k} | {v:.3f} |" for k, v in metrics_dict.items()]
        )

        # Figures
        figure_lines = "\n".join(
            [f"![{name}](../figures/{self.id}_{name}.png)" for name in figure_names]
        )

        # Interpretation block
        interpretation_block = ""
        if interpretation:
            interpretation_block = f"""
## Interpretation

```text
{interpretation}
