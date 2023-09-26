class TextEntity:
    primary: str = "#FFFFF"
    secondary: str 
    disabled: str


    def __init__(self, options):
        self.primary = options["primary"]
        self.secondary = options["secondary"]
        self.disabled = options["disabled"]