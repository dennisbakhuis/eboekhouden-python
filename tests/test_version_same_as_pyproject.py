import tomli

from eboekhouden_python import __version__


def test_version_same_as_pyproject():
    with open("pyproject.toml", "rb") as f:
        pyproject = tomli.load(f)
    assert __version__ == pyproject["project"]["version"]
