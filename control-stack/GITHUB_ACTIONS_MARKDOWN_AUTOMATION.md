# GitHub Actions: Generate Control-Stack Markdown

Put this workflow here:

```text
.github/workflows/generate-control-stack-markdown.yml
```

Required script location:

```text
control-stack/scripts/generate_control_stack_markdown.py
```

## What it does

It runs:

```bash
cd control-stack
python scripts/generate_control_stack_markdown.py
```

Then commits generated files:

```text
control-stack/docs/*.md
control-stack/results/*_summary.md
```

## How to run manually

1. Go to your GitHub repo.
2. Click **Actions**.
3. Select **Generate control-stack markdown**.
4. Click **Run workflow**.

## Auto-run behavior

It also runs automatically when you push changes to:

```text
control-stack/results/*.json
control-stack/figures/**
control-stack/scripts/generate_control_stack_markdown.py
```

## Important

Your repo settings must allow GitHub Actions to write commits:

```text
Settings → Actions → General → Workflow permissions → Read and write permissions
```
