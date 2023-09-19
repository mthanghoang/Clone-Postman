from PySide6.QtWidgets import QRadioButton
from PySide6.QtGui import QCursor, QPainter
from PySide6.QtCore import Qt



styles = '''
    QRadioButton {
        background-color: yellow;
        color: red;
        spacing: 20px;
        height: 20px;
    }

    QRadioButton::indicator {
        text-align: left;
    }

    QRadioButton::indicator::unchecked {
        border: 1px solid black; 
        height: 14px;
        width: 14px;
        border-radius: 8px;
        background: transparent;
    }

    QRadioButton::indicator::unchecked::hover {
        background: rgba(0, 167, 111, 0.2);
    }

    QRadioButton::indicator::checked {
        
    }
    
'''
# 

class CustomRadioButton(QRadioButton):
    def __init__(self, text="This is a radio button", disabled=False):
        super().__init__(text=text)

        self.setStyleSheet(styles)

        if disabled:
            self.setEnabled(False)
        else:
            self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    