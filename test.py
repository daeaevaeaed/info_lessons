from ui_mainWindow import *
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QFrame,
    QHBoxLayout,
    QSizePolicy,
    QDialog,
    QInputDialog,
    # QAlignCenter,
)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()

if __name__ == '__main__':
    # ff1.Cache.enable_cache("F:\cache")
    # year = 2020
    # number = 3
    # f = fastf1(year=year, number=number, type="R")
    # position = position()
    # f.output_position(position)
    app = QApplication()
    mainWindow = MainWindow()
    mainWindow.show()
    mainWindow.setStyleSheet(open('./stylesheet_main.qss', encoding="utf-8").read())
    app.exec()