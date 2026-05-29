# Local Environment Setup

Requirements to run the `.ipynb` notebooks in this repository on macOS.

## Prerequisites

- macOS with [Homebrew](https://brew.sh) installed
- Python 3.11+ (detected: Python 3.13.2)

---

## 1. Create a virtual environment

From the repository root, create and activate an isolated Python environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> Activate the environment every time you open a new terminal session before working on the notebooks.

---

## 2. Install Jupyter and core dependencies

```bash
pip install --upgrade pip
pip install jupyter notebook ipykernel anthropic
```

| Package | Purpose |
|---|---|
| `jupyter` | Core Jupyter tooling |
| `notebook` | Classic Jupyter Notebook UI |
| `ipykernel` | Connects the Python environment to Jupyter |
| `anthropic` | Anthropic Python SDK (Claude API) |

---

## 3. Register the virtual environment as a Jupyter kernel

```bash
python -m ipykernel install --user --name claude-certificate --display-name "Python (claude-certificate)"
```

This makes the kernel available in the Jupyter UI as **Python (claude-certificate)**, ensuring notebooks use the correct environment.

---

## 4. Set your Anthropic API key

The notebooks call the Claude API. Export your key before launching Jupyter:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

To avoid repeating this step, add the line to your shell profile (`~/.zshrc`):

```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.zshrc
source ~/.zshrc
```

---

## 5. Launch Jupyter Notebook

```bash
jupyter notebook
```

This opens the UI in your browser at `http://localhost:8888`. Open any `.ipynb` file from there.

**Important:** before running a notebook, select the correct kernel via **Kernel → Change kernel → Python (claude-certificate)**.

---

## 6. (Optional) Use JupyterLab instead

JupyterLab provides a more modern interface:

```bash
pip install jupyterlab
jupyter lab
```

---

## Day-to-day workflow

```bash
# 1. Activate the environment
source .venv/bin/activate

# 2. Start Jupyter
jupyter notebook        # or: jupyter lab
```

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| `ModuleNotFoundError: anthropic` | Confirm the venv is active (`which python` should point to `.venv/bin/python`) and reinstall: `pip install anthropic` |
| `AuthenticationError` from the API | Verify `echo $ANTHROPIC_API_KEY` prints the correct key |
| Kernel not listed | Re-run the `ipykernel install` command in step 3 |
| Old pip warnings | Run `pip install --upgrade pip` |
