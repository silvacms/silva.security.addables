# Copyright (c) 2008 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from setuptools import setup, find_packages
import os

version = '1.1'

setup(name='silva.security.addables',
      version=version,
      description="Configure which content type is addable for which Silva roles",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        ],
      keywords='silva roles security',
      author='Sylvain Viollon',
      author_email='info@infrae.com',
      url='http://infrae.com/products/silva',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['silva', 'silva.security'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        ],
      )
