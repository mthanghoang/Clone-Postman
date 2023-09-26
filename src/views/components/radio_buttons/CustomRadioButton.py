from PySide6.QtWidgets import QRadioButton
from PySide6.QtGui import QCursor, QPainter
from PySide6.QtCore import Qt



styles = '''
    QRadioButton {
        background-color: white;
        color: red;
        height: 20px;
    }

    QRadioButton::indicator {
        text-align: left;
    }

    QRadioButton::indicator::unchecked {
        border: 2px solid black;
        height: 14px;
        width: 14px;
        border-radius: 9px;
        background: transparent;
    }

    QRadioButton::indicator::unchecked::hover {
        background: rgba(0, 167, 111, 0.2);
        outline: solid 3px
    }

    QRadioButton::indicator::checked {
        border: 2px solid black;
        height: 14px;
        width: 14px;
        border-radius: 9px;
        background: rgb(0, 167, 111);
    }
    
'''
# 

class CustomRadioButton(QRadioButton):
    def __init__(self, text="Radio button", disabled=False):
        super().__init__(text=text)

        self.setStyleSheet(styles)

        if disabled:
            self.setEnabled(False)
        else:
            self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    