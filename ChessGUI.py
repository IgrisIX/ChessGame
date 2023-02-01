from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("MainWindow")

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&File")
        new_action = file_menu.addAction("New Game")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        option_menu = menu_bar.addMenu("&Option")
        setting_action = option_menu.addAction("Setting")

        central_widget = CentralWidget()
        self.setCentralWidget(central_widget)

    def quit_app(self):
        self.app.quit()


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()

        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Button2")
        button2.clicked.connect(self.button2_clicked)
        
        layout_main = QHBoxLayout()

        self.setLayout(layout_main)

        layout_main.addWidget(button1)
        layout_main.addWidget(button2)
        

    def button1_clicked(self):
        print("button1 clicked")

    def button2_clicked(self):
        print("button2 clicked")
        


app = QApplication(sys.argv)
window = MainWindow(app)

window.show()

app.exec()