from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from scene import Scene  # imports class Scene from scene.py
from node import Node  # imports class Node from node.py
from graphics_view import View
from socket import Socket  # imports class Socket from socket.py
from edge import Edge, bezier_edge  # imports class Edge and variable EDGE_TYPE_BEZIER from edge.py


class EditorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 800, 600)  # geometry of the widget relative to parent (x,y,w,h)

        self.layout = QVBoxLayout()  # sets the geometry of the widget’s children added to the layout
        # QVBoxLayout is used to construct vertical box layout
        self.layout.setContentsMargins(0, 0, 0, 0)  # sets the margins around the widget’s contents.
        self.setLayout(self.layout)

        self.scene = Scene()  # creates instance scene of class Scene

        self.view = View(self.scene.grScene, self)  # creates instance view of class View
        # and adds graphics scene to view
        self.layout.addWidget(self.view)  # adds view to layout

        '''self.title = QGraphicsTextItem("Untitled Scene")  # create new text item
        self.title.setTextInteractionFlags(Qt.TextEditable)  # text item can be edited
        self.title.setFlag(QGraphicsTextItem.ItemIsMovable)  # text item can be moved
        self.title.setFlag(QGraphicsTextItem.ItemIsSelectable)  # text item can be selected
        self.title.document().setDefaultTextOption(QTextOption(Qt.AlignCenter))  # aligns text to center
        self.title.setDefaultTextColor(QColor("#ffffff"))  # sets text color
        self.title.setFont(QFont("Ubuntu", 25))  # sets text font and size
        self.title.setPos(150, -250)  # sets text position
        self.scene.grScene.addItem(self.title)  # adds text item to the scene'''

        self.button_size = QSize(130, 30)  # sets button dimensions

        self.button = QPushButton(self)  # creates new button object
        self.button.setText("Focus Mode")  # sets label of button
        self.button.move(625, 10)  # sets position of button
        self.button.clicked.connect(self.scene.focus)  # calls method focus() of class Scene when clicked
        self.button.setStyleSheet(
            "border: 1px solid black; color: black ;font-size: 12px ;background: #ffffff;font-weight: bold")
        # defines style of button
        self.button.setFixedSize(self.button_size)  # sets size of button
        # self.addNodes() # on initial run fills the scene with predefined graph nodes

        self.setWindowTitle("Intertwine")  # sets title of the EditorWindow Class
        self.show()

    def addNodes(self):
        '''node1 = Node(self.scene, "Number", outputs=[1], node_type="integer")
        node2 = Node(self.scene, "Number", outputs=[1], node_type="integer")
        node3 = Node(self.scene, "Number", outputs=[1], node_type="integer")
        node4 = Node(self.scene, "Number", outputs=[1], node_type="integer")
        node5 = Node(self.scene, "Add", inputs=[1, 1], outputs=[2], node_type="Add")
        node6 = Node(self.scene, "Subtract", inputs=[1, 1], outputs=[2], node_type="Subtract")
        node7 = Node(self.scene, "Multiply", inputs=[2, 2], node_type="Multiply")
        node1.setPos(-350, -250)
        node2.setPos(-350, -110)
        node3.setPos(-350, 50)
        node4.setPos(-350, 190)
        node5.setPos(50, -180)
        node6.setPos(50, 120)
        node7.setPos(450, -30)'''
        node1 = Node(self.scene, "Node", inputs=[1], outputs=[2], node_type="integer")
        node2 = Node(self.scene, "Node", inputs=[1],outputs=[2], node_type="integer")
        node3 = Node(self.scene, "Node", inputs=[1],outputs=[2], node_type="integer")
        node4 = Node(self.scene, "Node",inputs=[1], outputs=[2], node_type="integer")
        node5 = Node(self.scene, "Node", inputs=[1], outputs=[2], node_type="Add")
        node6 = Node(self.scene, "Node", inputs=[1], outputs=[2], node_type="Subtract")
        node7 = Node(self.scene, "Node", inputs=[1], outputs=[2], node_type="Multiply")
        node1.setPos(-350, -250)
        node2.setPos(-350, -110)
        node3.setPos(-350, 50)
        node4.setPos(-350, 190)
        node5.setPos(50, -180)
        node6.setPos(50, 120)
        node7.setPos(450, -30)
