from .action import ActionEntity

class CommonEntity:
    common: str = ""
    primary: str = ""
    secondary: str = ""
    info: str = ""
    success: str = ""
    warning: str = ""
    error: str = ""
    grey: str = ""
    divider: str = ""
    action: ActionEntity = None
    
    def __init__(self, options):
        self.common = options["common"]
        self.primary = options["primary"]
        self.secondary = options["secondary"]
        self.info = options["info"]
        self.success = options["success"]
        self.warning = options["warning"]
        self.error = options["error"]
        self.grey = options["grey"]
        self.divider = options["divider"]
        self.action = options["action"]
                