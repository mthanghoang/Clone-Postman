class BackgroundEntity:
    paper: str = ""
    default: str = ""
    neutral: str = ""

    def __init__(self, options: dict):
        self.paper = options["paper"]
        self.default = options["default"]
        self.neutral = options["neutral"]