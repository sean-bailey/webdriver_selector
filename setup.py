"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/

"""
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

# Always prefer setuptools over distutils
import setuptools

keywords = ['selenium','webdriver','headless','automation','testing','random','chrome','chromium','edge','firefox','opera']

setuptools.setup(
    name="webdriver_selector",
    version="0.2",
    author="Sean Bailey",
    author_email="seanbailey518@gmail.com",
    description="webdriver_selector provides a quick and easy way to automatically get the first available webdriver on the system, preconfigured to be incognito and headless by default, with now the ability to choose headless state.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://www.github.com/sean-bailey/webdriver_selector",
    keywords = keywords,
    install_requires=['beautifulsoup4', 'selenium', 'fake_useragent', 'webdriver-manager', 'unidecode','cchardet'],
    packages = setuptools.find_packages(),
    classifiers=['Development Status :: 4 - Beta',
              'Intended Audience :: End Users/Desktop',
              'Intended Audience :: Developers',
              'Intended Audience :: System Administrators',
              'License :: OSI Approved :: GNU Alfero V3 License',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Topic :: Communications :: Email',
              'Topic :: Office/Business',
              'Topic :: Software Development :: Bug Tracking',
              ],
)
