from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QToolBar, QStatusBar, QMessageBox, QGridLayout, QCheckBox, QSizePolicy
import sys
from Gameplay import *

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("MainWindow")
        self.setGeometry(50, 50, 0, 0)

        #Menu Bar
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("&File")
        new_action = file_menu.addAction("New Game")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        option_menu = menu_bar.addMenu("&Option")
        setting_action = option_menu.addAction("Setting")

        # Tool Bar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction("Some Action", self)
        action2.setStatusTip("Status message for some action")
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        toolbar.addAction(quit_action)

        # Status bar
        self.setStatusBar(QStatusBar(self))


        # Main body
        central_widget = CentralWidget()
        self.setCentralWidget(central_widget)

    def quit_app(self):
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle("Goodbye!")
        message.setText("Do you sure you want to Quit?")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        reply = message.exec()
        if reply == QMessageBox.Ok:
            self.app.quit()
        else:
            pass

    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from toolbar", 3000)


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.game = Game()
        
        layout_main = QHBoxLayout()

        self.setLayout(layout_main)
        chess_widget = ChessWidget(self.game)
        user_widget = UserWidget()
        layout_main.addWidget(chess_widget)
        layout_main.addWidget(user_widget)
        
    

class ChessWidget(QWidget):
    def __init__(self, game):
        super().__init__()

        chessBoard = QGridLayout()
        self.setLayout(chessBoard)
        chessBoard.setOriginCorner(Qt.BottomLeftCorner)
        chessBoard.setSpacing(0)
        self.game = game

        for i in range(8):
            for j in range(8):
                cell_button = QPushButton()

                if (i + j) % 2 == 1:
                    cell_button.setStyleSheet("background-color:#ffd692; border: none;")
                else:
                    cell_button.setStyleSheet("background-color:#CE9C4C; border: none;")
                cell_button.clicked.connect(self.button_clicked)
                cell_button.setFixedSize(QSize(70, 70))
                cell_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                chessBoard.addWidget(cell_button, i, j)
        
    def button_clicked(self):
        print("something happened")




class UserWidget(QWidget):
    def __init__(self):
        super().__init__()

        button1 = QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Button2")
        button2.clicked.connect(self.button2_clicked)
        
        layout = QVBoxLayout()

        self.setLayout(layout)

        layout.addWidget(button1)
        layout.addWidget(button2)

    def button1_clicked(self):
        print("button1 clicked")

    def button2_clicked(self):
        print("button2 clicked")

