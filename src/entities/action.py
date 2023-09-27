class ActionEntity:
    hover: str = ""
    selected: str = ""
    disabled: str = ""
    disabledBackground: str = ""
    focus: str = ""
    hoverOpacity: 0.08
    disabledOpacity: 0.48
    active: str = ""

    def __init__(self, options):
        self.hover = options["hover"]
        self.selected = options["selected"]
        self.disabled = options["disabled"]
        self.disabled_background = options["disabledBackground"]
        self.focus = options["focus"]
        self.hover_opacity = options["hoverOpacity"]
        self.disabled_opacity = options["disabledOpacity"]
        self.active = options.get("active")
        
    def update(self, options):
        self.active = options["active"]