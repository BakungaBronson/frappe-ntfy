from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_ntfy/__init__.py
from frappe_ntfy import __version__ as version

setup(
	name="frappe_ntfy",
	version=version,
	description="A package to send simple notifications via the Ntfy app",
	author="Bakunga Bronson",
	author_email="bakungabronson@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
