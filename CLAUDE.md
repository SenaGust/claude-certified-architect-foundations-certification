# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Code and exercises from the **Claude Certified Architect: Foundations** certification. All work lives in `.ipynb` Jupyter notebooks.

## Environment setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name claude-certificate --display-name "Python (claude-certificate)"
```

Copy `.env.example` to `.env` and fill in the API key:

```
ANTHROPIC_API_KEY=sk-ant-...
```

Launch notebooks:

```bash
jupyter notebook   # or: jupyter lab
```

## Notebook conventions

Every notebook starts with:

```python
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"
```

## Repository structure

```
courses/
  <course-name>/
    <lesson-number>. <lesson-name>/
      code.ipynb   # exercise notebook
      README.md    # lesson notes
lessons/           # scratch/personal notebooks outside course structure
requirements.txt
SETUP.md           # full environment setup walkthrough
```

Lessons follow the naming convention `module-NN-<topic>/NN-<name>.ipynb` inside `lessons/`.
