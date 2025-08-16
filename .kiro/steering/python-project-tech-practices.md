---
title: Python projects best tech practices
inclusion: always
---

## Project & Dependency Management with `uv`

  - **Virtual Environments:** Always create and use a virtual environment with `uv venv`.
  - **No `requirements.txt`:** Do not use `requirements.txt` files. All project dependencies must be managed in `pyproject.toml`.
  - **Adding Dependencies:** Use `uv add <package>` to add a dependency to `pyproject.toml` and install it.
  - **Syncing Environment:** Use `uv sync` to install all dependencies specified in `pyproject.toml`.

## Script-Specific Dependencies

  - **Declare in File:** For standalone scripts, dependencies **must** be declared at the top of the `.py` file using a `/// script` block. This ensures portability and explicit dependency tracking.

  - **Example:**

    ```python
    # /// script
    # dependencies = [
    #   "requests<3",
    #   "rich",
    # ]
    # ///
    import requests
    from rich.pretty import pprint

    resp = requests.get("https://peps.python.org/api/peps.json")
    data = resp.json()
    pprint([(k, v["title"]) for k, v in data.items()][:10])
    ```