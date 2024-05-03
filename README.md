# Dwarf Fortress localization project Python package index

The index is build from the [index.yml](index.yml) file.

View the index: https://dfint.github.io/pypi-index/

Installation of a package from the index:
```
pip install df-translation-toolkit --extra-index-url https://dfint.github.io/pypi-index/
```

Using poetry:
```
poetry source add --priority=explicit dfint https://dfint.github.io/pypi-index/
poetry add --source=dfint df-translation-toolkit
```
Reference: [PEP 503](https://peps.python.org/pep-0503/)
