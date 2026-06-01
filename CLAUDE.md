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
import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

auth_token = os.getenv("ANTHROPIC_API_KEY")

client = Anthropic(
    auth_token=auth_token,
    base_url="https://flow.ciandt.com/flow-llm-proxy/"
)

model = "bedrock/anthropic.claude-4-6-sonnet"
```

The API calls go through a CI&T Flow proxy — do not use the plain `Anthropic()` constructor.

## Repository structure

```
courses/
  <course-name>/
    NN. <lesson-name>/   # zero-padded lesson number (e.g. 05, 06)
      code.ipynb         # exercise notebook
      README.md          # lesson notes
requirements.txt
SETUP.md                 # full environment setup walkthrough
```
