################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 3 - Alpha",
		"License :: OSI Approved :: Apache Software License",
	],
	description = "This python module provides an annotation that caches results of function calls automatically.",
	download_url = "https://github.com/jkpubsrc/python-module-jk-cachefunccalls/tarball/0.2020.3.5",
	include_package_data = False,
	install_requires = [
	],
	keywords = [
		"caching",
	],
	license = "Apache 2.0",
	name = "jk_cachefunccalls",
	packages = [
		"jk_cachefunccalls",
	],
	url = "https://github.com/jkpubsrc/python-module-jk-cachefunccalls",
	version = "0.2020.3.5",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
