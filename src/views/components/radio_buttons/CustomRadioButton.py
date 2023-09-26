from PySide6.QtWidgets import QRadioButton, QSizePolicy
from PySide6.QtGui import QCursor, QPainter, QPen
from PySide6.QtCore import Qt, QRect, QPoint



styles = '''
    QRadioButton {
        background-color: yellow;
        color: white;
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
        border: 1px solid rgb(0, 167, 111);
        height: 14px;
        width: 14px;
        border-radius: 8px;
        background: transparent;
    }
    
'''
# 

class CustomRadioButton(QRadioButton):
    def __init__(self, text="Radio button", disabled=False):
        super().__init__(text=text)
        
        self.setStyleSheet(styles)
        
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        if disabled:
            self.setEnabled(False)
        else:
            self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        

    def paintEvent(self, event):
        if self.isChecked():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)



            # Outer circle
            outer_radius = self.height() // 2
            outer_pen = QPen(Qt.black, 2)
            painter.setPen(outer_pen)
            painter.drawEllipse(QPoint(7, 7), outer_radius, outer_radius)

             # Inner circle
            inner_radius = int(outer_radius * 0.6)
            inner_pen = QPen(Qt.red, 2)
            painter.setPen(inner_pen)
            painter.drawEllipse(QPoint(7, 7), inner_radius, inner_radius)
        else:
            super().paintEvent(event)

    