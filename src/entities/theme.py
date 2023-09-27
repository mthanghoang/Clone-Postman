from .text import TextEntity
from .background import BackgroundEntity
from .action import ActionEntity


class ThemeEntity:
    mode: str = "dark"
    text: TextEntity = None
    background: BackgroundEntity = None
    action: ActionEntity = None

    def __init__(self, options):
        self.mode = options["mode"]
        self.text = options["text"]
        self.background = options["background"]
        self.action = options["action"]