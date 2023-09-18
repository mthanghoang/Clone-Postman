from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt

styles = '''
    QPushButton {{
        border: {};
        margin: {};
        vertical-align: {};
        text-decoration: {};
        font-weight: {};
        line-height: {};
        font-size: {};
        font-family: {};
        min-width: {};
        padding: {} {};
        border-radius: {};
        color: {};
        background-color: {};
    }}

    QPushButton::hover {{
        background-color: {};
    }}
'''
# rgb(255, 255, 255)
# rgb(33, 43, 54)
class AYContainedButton(QPushButton):
    def __init__(
        self,
        text="AY Default Button",
        border="0px",
        margin="0px",
        vertical_align="middle",
        text_decoration="none",
        font_weight="700",
        line_height="1.71429",
        font_size="0.875rem",
        font_family='"Public Sans", sans-serif',
        min_width="64px",
        padding_x="6px",
        padding_y="12px",
        border_radius="8px",
        color="rgb(255, 255, 255)",
        background_color="rgb(33, 43, 54)",
        hover_bg_color="rgb(58, 75, 94)",
        disabled=False
    ):
        super().__init__()
        
        self.setText(text)
        self.setStyleSheet(styles.format(
            border,
            margin,
            vertical_align,
            text_decoration,
            font_weight,
            line_height,
            font_size,
            font_family,
            min_width,
            padding_x,
            padding_y,
            border_radius,
            color,
            background_color,
            hover_bg_color
        ))
        if disabled:
            self.setEnabled(False)
        else:
            self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))