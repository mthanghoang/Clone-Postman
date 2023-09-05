# import cac thu vien he thong
# import cac thu vien ben thu 3
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QFrame,
    QSplitter
)
from PySide6.QtCore import (QSize,
                            Qt)
# from PySide6.QtGui import()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # doi title
        self.setWindowTitle("POSTMAN")
        # khai bao layout cho QMainWindow
        main_layout = QVBoxLayout()

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # thiet lap kich thuoc ban dau cho cua so ung dung
        self.resize(QSize(800, 600))

        # section header
        section_header = QFrame()
        section_header.setStyleSheet("background: red")
        section_header.setFixedHeight(60)
        # body
        section_body = QFrame()
        section_body.setStyleSheet("background: red")

        # tao layout cho body: co 2 cach
        # Cach 1:
        body_layout = QVBoxLayout()
        section_body.setLayout(body_layout)

        # Cach2:
        # body_layout = QVBoxLayout(section_body)

        splitter_main_bottom = QSplitter(section_body)
        splitter_main_bottom.setOrientation(Qt.Orientation.Vertical)
        splitter_main_bottom.setStyleSheet("background: yellow")

        # section main
        section_main = QFrame(splitter_main_bottom) 
        section_main.setStyleSheet("background: blue")
    

        # bottom bao gom menu va footer
        section_bottom = QFrame(splitter_main_bottom)
        section_bottom.setStyleSheet("background: blue")
        # tao layout trong bottom
        bottom_layout = QVBoxLayout(section_bottom)

        # split main and bottom inside body
        splitter_main_bottom.addWidget(section_main)
        splitter_main_bottom.addWidget(section_bottom)

        #bottom menu
        section_bottom_menu = QFrame(section_bottom)
        section_bottom_menu.setStyleSheet("background: green")
        section_bottom_menu.setFixedHeight(40)
        
        # section footer
        section_footer = QFrame(section_bottom)
        section_footer.setStyleSheet("background: green")

        # them cac section vao main layout
        main_layout.addWidget(section_header)
        main_layout.addWidget(section_body)
        body_layout.addWidget(splitter_main_bottom)
        bottom_layout.addWidget(section_bottom_menu)
        bottom_layout.addWidget(section_footer)
        
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
