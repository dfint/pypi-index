# pypi-index

View the index: https://dfint.github.io/pypi-index/

Installation of a package from the index:
```
pip install df-gettext-toolkit --extra-index-url https://dfint.github.io/pypi-index/
```

Using poetry:
```
poetry source add --priority=explicit dfint https://dfint.github.io/pypi-index/
poetry add --source=dfint df-gettext-toolkit
```
