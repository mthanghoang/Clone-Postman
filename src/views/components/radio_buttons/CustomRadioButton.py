from PySide6.QtWidgets import QRadioButton, QFrame
from PySide6.QtGui import QCursor, QPainter, QPen, QBrush, QColor
from PySide6.QtCore import Qt


styles = '''
    QRadioButton {{
        background-color: transparent;
        color: black;
        spacing: 6px;
    }}

    QRadioButton::indicator::unchecked {{
        border: 2px solid rgb(99, 115, 129);
        height: 14px;
        width: 14px;
        border-radius: 9px;
    }}

    QRadioButton::indicator::unchecked::hover {{
        background: {};
    }}
    
'''
# 

class CustomRadioButton(QRadioButton):
    def __init__(self, 
                 text="Default", 
                 disabled=False,
                 bg_color_unchecked_hover="#63738133",
                 border_color_checked="#637381"
                 ):
        super().__init__(text=text)

        self._border_color_checked = border_color_checked
        self._inner_circle_color = border_color_checked
        self._bg_color_checked_hover = bg_color_unchecked_hover
        
        self.setStyleSheet(styles.format(bg_color_unchecked_hover))

        self._hovered = False


        if disabled:
            self.setEnabled(False)
        else:
            self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
    def enterEvent(self, event):
        self._hovered = True
        self.update()

    def leaveEvent(self, event):
        self._hovered = False
        self.update()


    def paintEvent(self, event):
        if self.isChecked():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)

            self.setFixedHeight(30)
            print("self.height_______", self.height())
            # Draw the circle to the left of the content area
            # circle_diameter = min(self.height(), self.width())
            circle_diameter = 16
            circle_radius = 8
            circle_x = 1
            circle_y = self.height() // 2 - circle_radius

            # fill outermost ring 
            if self._hovered:
                painter.setPen(Qt.NoPen)
                painter.setBrush(QBrush(QColor(self._bg_color_checked_hover)))
                painter.drawEllipse(circle_x - 5, 
                                    circle_y - 5, 
                                    circle_diameter + 10, 
                                    circle_diameter + 10)

            
            # if self._hovered:
            #     # fill outer circle when hovering (bg color when checked and hovered)
            #     painter.setPen(Qt.NoPen)
            #     painter.setBrush(QBrush(QColor(self._bg_color_checked_hover)))
            #     painter.drawEllipse(circle_x + 1, 
            #                     circle_y + 1, 
            #                     circle_diameter - 2, 
            #                     circle_diameter - 2)
                
            #     # fill the ring outside the border
            #     # painter.drawEllipse(circle_x - 2,
            #     #                     circle_y - 2,
            #     #                     circle_diameter + 4,
            #     #                     circle_diameter + 4)
            
            # Outer circle
            outer_pen = QPen(QColor(self._border_color_checked), 2)
            painter.setPen(outer_pen)
            painter.setBrush(Qt.NoBrush)
            painter.drawEllipse(circle_x, 
                                circle_y, 
                                circle_diameter, 
                                circle_diameter)

            # Inner circle
            inner_radius = int(circle_radius * 0.6)
            inner_brush = QBrush(QColor(self._inner_circle_color))
            painter.setBrush(inner_brush)
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(circle_x + circle_radius - inner_radius, 
                                circle_y + circle_radius - inner_radius, 
                                inner_radius * 2, 
                                inner_radius * 2)
            
            
            # Draw the text in the content area
            painter.setPen(QPen(Qt.black, 2))
            text_rect = self.rect().adjusted(circle_diameter + 8, 0, 0, 0)
            painter.drawText(text_rect, Qt.AlignVCenter, self.text())
            
            painter.end()

        else:
            super().paintEvent(event)

    
    