import sys
from PyQt5.QtWidgets import *
from window import EditorWindow  # imports class EditorWindow from window.py file

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    wnd = EditorWindow()  # Creates instance of class EditorWindow
    wnd.showMaximized()  # window is opened in Maximised mode on "run"
    app.exec()
