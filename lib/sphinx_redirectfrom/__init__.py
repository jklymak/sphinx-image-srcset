import importlib.metadata


try:
    __version__ = importlib.metadata.version("sphinx-redirectfrom")
except ImportError:
    __version__ = "0+unknown"
