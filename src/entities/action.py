class ActionEntity:
    hover: str = ""
    selected: str = ""
    disabled: str = ""
    disabled_background: str = ""
    focus: str = ""
    hover_opacity: 0.08
    disabled_opacity: 0.48
    active: str = ""

    def __init__(self, options: dict):
        self.hover = options["hover"]
        self.selected = options["selected"]
        self.disabled = options["disabled"]
        self.disabled_background = options["disabled_background"]
        self.focus = options["focus"]
        self.hover_opacity = options["hover_opacity"]
        self.disabled_opacity = options["disabled_opacity"]
        self.active = options.get("active")
        
    def update(self, active):
        self.active = active