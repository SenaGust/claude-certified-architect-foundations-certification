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
pip install jupyter notebook ipykernel anthropic python-dotenv
```

| Package         | Purpose                                    |
| --------------- | ------------------------------------------ |
| `jupyter`       | Core Jupyter tooling                       |
| `notebook`      | Classic Jupyter Notebook UI                |
| `ipykernel`     | Connects the Python environment to Jupyter |
| `anthropic`     | Anthropic Python SDK (Claude API)          |
| `python-dotenv` | Loads variables from a `.env` file         |

---

## 3. Register the virtual environment as a Jupyter kernel

```bash
python -m ipykernel install --user --name claude-certificate --display-name "Python (claude-certificate)"
```

This makes the kernel available in the Jupyter UI as **Python (claude-certificate)**, ensuring notebooks use the correct environment.

---

## 4. Set your Anthropic API key

Create a `.env` file in the repository root:

```
ANTHROPIC_API_KEY=sk-ant-...
```

Then load it at the top of each notebook before using the Anthropic client:

```python
from dotenv import load_dotenv
load_dotenv()  # reads .env and sets environment variables

import anthropic
client = anthropic.Anthropic()  # automatically picks up ANTHROPIC_API_KEY
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

| Symptom                            | Fix                                                                                                                              |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `ModuleNotFoundError: anthropic`   | Confirm the venv is active (`which python` should point to `.venv/bin/python`) and reinstall: `pip install anthropic`            |
| `AuthenticationError` from the API | Check that `.env` exists, contains `ANTHROPIC_API_KEY=sk-ant-...`, and that `load_dotenv()` is called before creating the client |
| Kernel not listed                  | Re-run the `ipykernel install` command in step 3                                                                                 |
| Old pip warnings                   | Run `pip install --upgrade pip`                                                                                                  |
