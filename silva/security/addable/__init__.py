import install
import AddablesPermissions

from Products.Silva.ExtensionRegistry import extensionRegistry

def initialize(context):
    extensionRegistry.register(
        'silva.security.addable', 
        'Silva configuration utility for addables permissions', 
        context, [], install, depends_on='Silva')

    context.registerClass(
        AddablesPermissions.AddablesPermissionsService,
        constructors = (AddablesPermissions.manage_addAddablesPermissionsServiceForm,
                        AddablesPermissions.manage_addAddablesPermissionsService),
        icon = "www/addablespermissions_service.gif"
        )

