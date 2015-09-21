try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Fib',
    'version': '0.2',
    'packages': ['pyfib'],
    'include_package_data': True,
    'name': 'pyfib',
    'install_requires': ['pandas'],
}

setup(**config)
