
from Products.Silva.tests import SilvaTestCase
from Products.Five import zcml

from Testing import ZopeTestCase as ztc


class FakeRequest(dict):
    """Dictionarish like fake request with an attribute form.
    """

    @property
    def form(self):
        return self['form']

class AddablesPermissionsTestCase(SilvaTestCase.SilvaTestCase):
    """Tests for silva.security.addables.
    """

    def afterSetUp(self):

        #import pdb ; pdb.set_trace()

        root = self.getRoot()
        root.service_extensions.install('silva.security.addables')
    
    def test_00install(self):
        """Install should provide a new service.
        """
        root = self.getRoot()
        self.failUnless(hasattr(root.aq_base, 'service_addablespermissions'))

    def test_10retrieve(self):
        """There is utilities which retrieve current settings.
        """
        root = self.getRoot()
        service = root.service_addablespermissions

        expected_roles = ('Author', 'Editor', 'ChiefEditor', 'Manager')
        self.assertEqual(service.manageableRoles(), expected_roles)

        expected_perms = {'Silva AutoTOC': 'Author', 
                          'Silva Link': 'Author', 
                          'Silva Folder': 'Author', 
                          'Silva Image': 'Author', 
                          'Silva Publication': 'Editor', 
                          'Silva Document': 'Author', 
                          'Silva File': 'Author', 
                          'Silva Find': 'Editor', 
                          'Silva Ghost Folder': 'Editor', 
                          'Silva Indexer': 'Editor', 
                          'Silva Ghost': 'Author'}
        self.assertEqual(service.currentAddablesPermissions(), expected_perms)

    def test_20modification(self):
        """Modification should work.
        """
        root = self.getRoot()
        service = root.service_addablespermissions

        new_perms = {'Silva AutoTOC': 'Manager', 
                     'Silva Link': 'Author', 
                     'Silva Folder': 'Author', 
                     'Silva Image': 'Author', 
                     'Silva Publication': 'Editor', 
                     'Silva Document': 'Author', 
                     'Silva File': 'Author', 
                     'Silva Find': 'ChiefEditor', 
                     'Silva Ghost Folder': 'Editor', 
                     'Silva Indexer': 'ChiefEditor', 
                     'Silva Ghost': 'Author'}
        REQUEST = FakeRequest({'form': new_perms})
        service.manage_editAddablesPermissions(REQUEST)

        self.assertEqual(service.currentAddablesPermissions(), new_perms)

    def test_60corruptpermissions(self):
        """When permission settings doesn't match Silva logic, we
        should get an value error.
        """
        root = self.getRoot()
        service = root.service_addablespermissions

        # Set bad permissions
        root.manage_permission('Add Silva Documents',
                               ('Author', 'Manager'),
                               0)

        self.assertRaises(ValueError, service.currentAddablesPermissions)


import unittest
def test_suite():
    
    # Load Five ZCML
    from Products import Five
    zcml.load_config('meta.zcml', Five)
    zcml.load_config('configure.zcml', Five)

    # Load our ZCML, which add the extension as a Product
    from silva.security import addables
    zcml.load_config('configure.zcml', addables)

    # Load the Zope Product
    ztc.installPackage('silva.security.addables')

    # Run tests
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AddablesPermissionsTestCase))
    return suite
