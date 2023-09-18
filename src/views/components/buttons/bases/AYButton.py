from PySide6.QtWidgets import QPushButton


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
class AYButton(QPushButton):
    def __init__(
        self,
        text,
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