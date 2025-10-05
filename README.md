# Organization's Python package index

The index is build from the [index.yml](index.yml) file (reference: [PEP 503](https://peps.python.org/pep-0503/)).

View the index: <https://dfint.github.io/pypi-index/>

## Installation of a package from the index:

```shell
pip install package-name --extra-index-url https://dfint.github.io/pypi-index/
```

## Using poetry:

```shell
poetry source add --priority=explicit dfint https://dfint.github.io/pypi-index/
poetry add --source=dfint package-name
```

## Using uv:

```shell
uv add package-name --index dfint=https://dfint.github.io/pypi-index/
```

It's recommended to add `explicit = true` for `dfint` index in `[[tool.uv.index]]` section of `pyproject.toml`:

```
[[tool.uv.index]]
name = "dfint"
url = "https://dfint.github.io/pypi-index/"
explicit = true  # <-- added
```
