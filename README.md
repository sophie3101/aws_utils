# aws_utils

The proejct is built oo be used as module
to build the project
pip install build
python -m build

option1: upload to PyPI
pip install twine
twine upload dist/*

option2:
upload to git and let other project to isntall directly from github

in the other project pyproject.toml file
dependencies = [
  "sphinx@git+https://github.com/sphinx-doc/sphinx",
]