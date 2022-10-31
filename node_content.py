from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from collections import OrderedDict
from serializable import Serializable


class NodeContent(QWidget, Serializable):
    def __init__(self, node, node_type, parent=None):
        super().__init__(parent)

        self.node = node
        self.node_type = node_type

        self.initUI()

    def initUI(self):

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        #font = QFont()
        #font.setPointSize(35)
        #self.textbox = QTextEdit("")
        #self.textbox.setFont(font)
        ##self.textbox.setAlignment(Qt.AlignCenter)
        #self.layout.addWidget(self.textbox)

    def serialize(self):
        return OrderedDict([

        ])

    def deserialize(self, data, hashmap={}):
        return False
