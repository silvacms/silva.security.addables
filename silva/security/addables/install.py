
from AddablesPermissions import SERVICE_ID

def install(root):
    """Install method for the service.
    """
    product = root.manage_addProduct['silva.security.addable']
    product.manage_addAddablesPermissionsService(SERVICE_ID)

def uninstall(root):
    """Uninstall method for the service.
    """
    root.manage_delObjects([SERVICE_ID])

def is_installed(root):
    """Return true is the service is installed.
    """
    return hasattr(root.aq_base, SERVICE_ID)


if __name__ == '__main__':
    print """This module is not an installer. You don't have to run it."""
