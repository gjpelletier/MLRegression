from setuptools import setup
import sys
sys.path.insert(0, ".")
from MLRegression import __version__

setup(
    name='MLRegression',
    version=__version__,
    author='Greg Pelletier',
    py_modules=['MLRegression'], 
    install_requires=['numpy','pandas','statsmodels','scikit-learn','tabulate','matplotlib'],
)