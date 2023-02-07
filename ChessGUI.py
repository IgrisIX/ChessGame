from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QPixmap
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
        central_widget = CentralWidget(self.app)
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
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.game = Game()
        
        layout_main = QHBoxLayout()

        self.setLayout(layout_main)
        chess_widget = ChessWidget(self.app, self.game)
        user_widget = UserWidget(self.app)
        layout_main.addWidget(chess_widget)
        layout_main.addWidget(user_widget)
        
    

class ChessWidget(QWidget):
    def __init__(self, app, game):
        super().__init__()
        self.app = app

        self.chessBoard = QGridLayout()
        self.setLayout(self.chessBoard)
        self.chessBoard.setOriginCorner(Qt.BottomLeftCorner)
        self.chessBoard.setSpacing(0)
        self.game = game
        self.cell_array = []
        for i in range(8):
            row = []
            for j in range(8):
                button = QPushButton()
                button.setText(str(i) + str(j))
                row.append(button)
            self.cell_array.append(row)

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    self.cell_array[i][j].setStyleSheet("background-color:#000000; color:#000000; border: none; font-size: 1px")
                else:
                    self.cell_array[i][j].setStyleSheet("background-color:#F06292; color:#F06292; border: none; font-size: 1px")
                self.cell_array[i][j].clicked.connect(self.button_clicked)
                self.cell_array[i][j].setFixedSize(QSize(70, 70))
                self.cell_array[i][j].setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                self.chessBoard.addWidget(self.cell_array[i][j], j, i)
                self.render_board()

        
    def button_clicked(self):
        x = int(self.sender().text()[0])
        y = int(self.sender().text()[1])
        self.game.choose_move(x, y)
        self.render_board()
        if self.game.gameOver is True:
            self.game_over_message()

    def render_board(self):
        for i in range(8):
            for j in range(8):
                self.cell_array[i][j].setIcon(QIcon())

        for i in range(8):
            for j in range(8):
                cell = self.game.chessBoard.grid[i][j]
                if cell is not None:
                    icon = QIcon(QPixmap("./Resources/chess_pieces/" + self.game.chessBoard.grid[i][j].icon + ".png"))
                    self.cell_array[i][j].setIcon(icon)
                    self.cell_array[i][j].setIconSize(QSize(50, 50))

    def game_over_message(self):
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        if self.game.turn == WHITE:
            winner = "Black win!!!"
        else:
            winner = "White win!!!"
        message.setWindowTitle(winner)
        message.setText("Retry or Close?")
        message.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
        message.setDefaultButton(QMessageBox.Close)

        reply = message.exec()
        if reply == QMessageBox.Retry:
            self.game = Game()
            self.render_board()
        else:
            self.app.quit()


class UserWidget(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app

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


