from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class GraphicsScene(QGraphicsScene):
    def __init__(self, scene, parent=None):
        super().__init__(parent)

        self.scene = scene
        self.color_background = QColor("#1a1c1d")  # sets background color of scene
        self.setBackgroundBrush(self.color_background)

    def setGrScene(self, width, height):
        self.setSceneRect(-width // 2, -height // 2, width, height)
        # initializes the bounding rectangle of scene
        # defines the extent of the scene used by QGraphicsView to determine its default scrollable area
