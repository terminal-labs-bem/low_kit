from setuptools import setup, find_packages

package_dir = \
{'': 'src'}

packages = \
['lowkit']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'basekit',
    'version': '0.1.4',
    'description': '',
    'long_description': '',
    'author': 'Michael Verhulst',
    'author_email': 'michael@terminallabs.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'include_package_data': True,
    'python_requires': '>=3.8,<4.0',
}

setup(**setup_kwargs)
