# E-boekhouden-Python API client
This is a simple API client for the E-boekhouden.nl API. It is written in Python and uses the ZEEP library. This library is partly inspired by work of Roel van den Boom.

## Installation and basic configuration
To install the library, simply run the following command:

```bash
pip install eboekhouden-python
```

To use the library, you need to configure it with your API credentials. While you can add these credentials as parameters to the class constructor, it is recommended to use environment variables. The following environment variables are automatically recognized by the library:

```bash
EBOEKHOUDEN_USERNAME=your_username
EBOEKHOUDEN_CODE1=your_code_1
EBOEKHOUDEN_CODE2=your_code_2
```

## Usage
The library is very simple to use. The following example shows how to retrieve a list of all mutations:

```python
from eboekhouden_python import EboekhoudenClient

client = EboekhoudenClient()
mutations = client.get_mutaties()
```

## Development
Feel free to extend the library, pull requests are welcome. For a development environment, you can use the following commands:

```bash
conda env create -f environment.yml
poetry install
pre-commit install
```
