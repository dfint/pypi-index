# Dwarf Fortress localization project Python package index

The index is build from the [index.yml](index.yml) file (reference: [PEP 503](https://peps.python.org/pep-0503/)).

View the index: <https://dfint.github.io/pypi-index/>

Installation of a package from the index:

```shell
pip install package-name --extra-index-url https://dfint.github.io/pypi-index/
```

Using poetry:

```shell
poetry source add --priority=explicit dfint https://dfint.github.io/pypi-index/
poetry add --source=dfint package-name
```

Using uv:

```shell
uv add package-name --index dfint=https://dfint.github.io/pypi-index/
```
