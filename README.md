# Foundry

## Alternative Title: Study repository for the AI-901 cert

Mostly used for archive purposes. Definitely not meant to be used as study resources since the cert is bound to frequently change.

### How to install

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/).

```sh
git clone <repo-url> foundry
cd foundry
uv sync
```

`uv sync` installs the right Python version (3.14+) if needed, creates `.venv` and installs all dependencies from `uv.lock`.

To run:

```sh
uv run index.py
```