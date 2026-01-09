from spectrai import App
from ui.main_ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from constants import *
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton,QColorDialog,QMessageBox,QShortcut

if __name__ == "__main__":
    import sys
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = App()
    MainWindow.show()
    sys.exit(app.exec_())