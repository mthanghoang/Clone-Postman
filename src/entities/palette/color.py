
class PrimaryEntity():
    lighter: str = ""
    lightstr = ""
    main: str = ""
    dark: str = ""
    darker: str = ""
    contrastText: str = ""

    def __init__(self, options: dict) -> None:
        self.lighter = options["lighter"]
        self.light = options["light"]
        self.main = options["main"]
        self.dark = options["dark"]
        self.darker = options ["darker"]
        self.contrastText = options["contrastText"]


class SecondaryEntity():
    lighter: str = ""
    lightstr = ""
    main: str = ""
    dark: str = ""
    darker: str = ""
    contrastText: str = ""

    def __init__(self, options: dict) -> None:
        self.lighter = options["lighter"]
        self.light = options["light"]
        self.main = options["main"]
        self.dark = options["dark"]
        self.darker = options ["darker"]
        self.contrastText = options["contrastText"]
