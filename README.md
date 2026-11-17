# Foundry

## Alternative Title: Study repository for the AI-901 cert

Mostly used for archive purposes. Definitely not meant to be used as study resources since the cert is bound to frequently change.

**For the record, the name of the agent used within this study is `andresgpt`**. Feel free to change it to whatever name you'd prefer (when you clone this repo).

**This repository also asumes you have an .env, please look at `env.example` for it.**
### How to install

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/).

```sh
git clone <repo-url> foundry
cd foundry
uv sync
```

`uv sync` installs the right Python version (3.14+) if needed, creates `.venv` and installs all dependencies from `uv.lock`.

Then set up your config and sign in to Azure:

```sh
cp .env.example .env   # fill in your endpoint and agent name
az login
```

To run:

```sh
uv run index.py
```