class ProjectPathAlreadyExists(Exception):
    """Base class for Project path already exists"""


class StaticPathAlreadyExists(Exception):
    """Base class for Static path already exists"""


class TemplatePathAlreadyExists(Exception):
    """Base class for Template path already exists"""


class ModulePathAlreadyExists(Exception):
    """Base class for Module path already exists"""


class InvalidProjectName(Exception):
    """Base class for Invalid project name"""


class InvalidModuleName(Exception):
    """Base class for Invalid module name"""


class TemplateModuleAlreadyExists(Exception):
    """Base class for Template Module Already exists"""


class InvalidFileName(Exception):
    """Base class for Invalid File name"""


class InvalidFolderName(Exception):
    """Base class for Invalid Folder name"""


class RootPathDoesNotExists(Exception):
    """Base class for Root Path Does Not Exists"""