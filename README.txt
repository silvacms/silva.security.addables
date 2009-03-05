silva.security.addable
**********************

This small Silva extension provides an interface in SMI to manage
which roles have the right to add which content type.

It's ensure as well that current permissions are set correctly
according the Silva logic.

It requires at least Silva 2.0.

Installation
============

If you installed Silva using buildout, by getting one from the `Infrae
SVN`_ repository, or creating one using `Paster`_, you should edit your
buildout configuration file ``buildout.cfg`` to add or edit the
following section::

  [instance]

  eggs +=
        silva.security.addables

  zcml += 
        silva.security.addables

If the section ``instance`` wasn't already in the configuration file,
pay attention to re-copy values for ``eggs`` and ``zcml`` from the
profile you use.

After you can restart buildout::

  $ ./bin/buildout


If you don't use buildout, you can install this extension using
``easy_install``, and after create a file called
``silva.security.addables-configure.zcml`` in the
``/path/to/instance/etc/package-includes`` directory.  This file will
responsible to load the extension and should only contain this::

  <include package="silva.security.addables" />


Latest version
==============

The latest version is available in a `Subversion repository
<https://svn.infrae.com/silva.security.addables/trunk#egg=silva.security.addables-dev>`_.

.. _Infrae SVN: https://svn.infrae.com/buildout/silva/
.. _Paster: https://svn.infrae.com/buildout/silva/INSTALL.txt
.. _Silva: http://infrae.com/products/silva
