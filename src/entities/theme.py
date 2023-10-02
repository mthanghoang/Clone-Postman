from .text import TextEntity
from .background import BackgroundEntity
from .action import ActionEntity
from .common import CommonEntity

class ThemeEntity(CommonEntity):
    mode: str = ""
    text: TextEntity = None
    background: BackgroundEntity = None
    # action: ActionEntity = None


    def __init__(self, light: dict, common: dict):
        super().__init__(common)
        self.mode = light["mode"]
        self.text = light["text"]
        self.background = light["background"]
        # self.action = light["action"]