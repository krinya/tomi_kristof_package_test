# my_simple_package/my_simple_package/__init__.py
# Make the version easily accessible (matches pyproject.toml)
__version__ = "0.1.1"

from .core import greet
__all__ = ['greet'] # Explicitly define the public API