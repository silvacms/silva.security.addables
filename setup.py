from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='silva.security.addables',
      version=version,
      description="Configure which content type is addable for which Silva roles",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='silva roles security',
      author='Sylvain Viollon',
      author_email='info@infrae.com',
      url='http://infrae.com/products/silva',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['silva', 'silva.security'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      )
