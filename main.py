# import cac thu vien he thong
# import cac thu vien ben thu 3
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QFrame,
    QSplitter,
    QHBoxLayout
)
from PySide6.QtCore import (QSize,
                            Qt)
from src.views import (AYContainedButton, 
                       SSlider, 
                       TSlider, 
                       AYOutlinedButton,
                       CustomRadioButton,
                      )
from src.theme import palette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # doi title
        self.setWindowTitle("POSTMAN")

        # init theme
        # self.theme = palette("dark")
        # print(self.theme)


        # khai bao layout cho QMainWindow
        main_layout = QVBoxLayout()

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # thiet lap kich thuoc ban dau cho cua so ung dung
        self.resize(QSize(1500, 700))

        # section header for contained buttons
        section_header = QFrame()
        section_header.setStyleSheet("background: gray")
        section_header.setFixedHeight(50)
        hlo_section_header = QHBoxLayout(section_header)

        # section header for outlined buttons
        section_header_1 = QFrame()
        section_header_1.setStyleSheet("background: gray")
        section_header_1.setFixedHeight(50)
        hlo_section_header_1 = QHBoxLayout(section_header_1)

        # section header for custom radio buttons
        section_header_2 = QFrame()
        section_header_2.setStyleSheet("background: white")
        section_header_2.setFixedHeight(50)
        hlo_section_header_2 = QHBoxLayout(section_header_2)

        # row of contained buttons
        btn_aydefault = AYContainedButton(text="Default")
            
        btn_ay_primary = AYContainedButton(
            text="Primary",
            background_color="rgb(0, 167, 111)",
            hover_bg_color="rgb(12, 226, 154)"
        )

        btn_ay_secondary = AYContainedButton(
            text="Secondary",
            background_color="rgb(142, 51, 255)",
            hover_bg_color="rgb(57, 14, 109)"
        )

        btn_ay_disabled = AYContainedButton(
            text="Disabled",
            color="rgba(145, 158, 171, 0.8)",
            background_color="rgba(145, 158, 171, 0.24)",
            hover_bg_color="rgba(145, 158, 171, 0.24)",
            disabled=True
        )

        hlo_section_header.addWidget(btn_aydefault)
        hlo_section_header.addWidget(btn_ay_primary)
        hlo_section_header.addWidget(btn_ay_secondary)
        hlo_section_header.addWidget(btn_ay_disabled)

        # row of outlined buttons
        btn_outlined_default = AYOutlinedButton()

        btn_outlined_primary = AYOutlinedButton(
            text="Primary", 
            color="rgb(0, 167, 111)", 
            border="1px solid rgb(0, 167, 111)", 
            hover_bg_color="rgba(0, 167, 111, 0.1)",
            hover_border_color="rgb(0, 167, 111)"
            # hover_outline_style=""
        )
        btn_outlined_secondary = AYOutlinedButton(
            text="Secondary", 
            color="rgb(142, 51, 255)", 
            border="1px solid rgb(142, 51, 255)", 
            hover_bg_color="rgba(142, 51, 255, 0.1)",
            hover_border_color="rgb(142, 51, 255)"
        )
        btn_outlined_disabled = AYOutlinedButton(text="Disabled", color="rgba(145, 158, 171, 0.8)", disabled=True)

        hlo_section_header_1.addWidget(btn_outlined_default)
        hlo_section_header_1.addWidget(btn_outlined_primary)
        hlo_section_header_1.addWidget(btn_outlined_secondary)
        hlo_section_header_1.addWidget(btn_outlined_disabled)


        # row of custom radio buttons
        radio_btn_default = CustomRadioButton()
        radio_btn_primary = CustomRadioButton(text="Primary",
                                              bg_color_unchecked_hover="#ace8cd",
                                              border_color_checked="#00a76f")
        radio_btn_disabled = CustomRadioButton(text="Disabled",
                                               disabled=True)

        hlo_section_header_2.addWidget(radio_btn_default)
        hlo_section_header_2.addWidget(radio_btn_primary)
        hlo_section_header_2.addWidget(radio_btn_disabled)



        # body
        section_body = QFrame()
        section_body.setStyleSheet("background: gray")

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
        main_layout.addWidget(section_header_1)
        main_layout.addWidget(section_header_2)
        main_layout.addWidget(section_body)
        body_layout.addWidget(splitter_main_bottom)
        bottom_layout.addWidget(section_bottom_menu)
        bottom_layout.addWidget(section_footer)
        
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
