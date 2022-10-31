from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class GraphicsNode(QGraphicsItem):
    def __init__(self, node, parent=None):
        super().__init__(parent)

        self.node = node
        self.content = self.node.content
        self.title_color = Qt.white
        self.title_font = QFont("SansSerif", 11, QFont.Bold)

        self.width = 100
        self.height = 60
        self.edge_size = 10.0
        self.title_height = 28.0
        self._padding = 5.0

        self.pen_default = QPen(QColor("#ffffff"))
        self.pen_default.setWidthF(2.5)
        self.pen_selected = QPen(QColor("#E3242B"))
        self.pen_selected.setWidthF(2.5)
        self.brush_title = QBrush(QColor("#4a4b4c"))
        self.brush_background = QBrush(QColor("#545556"))

        self.initTitle()
        self.title = self.node.title  # calls setter

        self.initSockets()
        #self.initContent()
        self.initUI()

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        for node in self.scene().scene.nodes:  # all edges of node updated when moved
            if node.grNode.isSelected():
                node.updateConnectedEdges()

    def boundingRect(self):
        return QRectF(
            0,
            0,
            self.width,
            self.height
        ).normalized()

    def initUI(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)  # node can be selected
        self.setFlag(QGraphicsItem.ItemIsMovable)  # node can be moved

    def initTitle(self):
        self.title_item = QGraphicsTextItem(self)
        self.title_item.node = self.node
        self.title_item.setDefaultTextColor(self.title_color)
        self.title_item.setFont(self.title_font)
        self.title_item.setPos(self._padding, 0)
        self.title_item.document().setDefaultTextOption(QTextOption(Qt.AlignHCenter))
        self.title_item.setTextWidth(
            self.width
            - 2 * self._padding
        )

    @property
    def title(self): return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.title_item.setPlainText(self._title)

    '''def initContent(self):
        self.grContent = QGraphicsProxyWidget(self)
        self.content.setGeometry(int(self.edge_size), int(self.title_height) + int(self.edge_size),
                                 int(self.width) - 2 * int(self.edge_size), int(self.height) - 2 * int(self.edge_size) - int(self.title_height))

        self.grContent.setWidget(self.content)'''

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        # creates path for node's title
        path_title = QPainterPath()
        path_title.setFillRule(Qt.WindingFill)
        path_title.addRoundedRect(0, 0, self.width, self.title_height, self.edge_size, self.edge_size)
        path_title.addRect(0, self.title_height - self.edge_size, self.edge_size, self.edge_size)
        path_title.addRect(self.width - self.edge_size, self.title_height - self.edge_size, self.edge_size,
                           self.edge_size)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.brush_title)
        painter.drawPath(path_title.simplified())

        # creates path for node's content
        path_content = QPainterPath()
        path_content.setFillRule(Qt.WindingFill)
        path_content.addRoundedRect(0, self.title_height, self.width, self.height - self.title_height, self.edge_size,
                                    self.edge_size)
        path_content.addRect(0, self.title_height, self.edge_size, self.edge_size)
        path_content.addRect(self.width - self.edge_size, self.title_height, self.edge_size, self.edge_size)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.brush_background)
        painter.drawPath(path_content.simplified())

        # creates path for node's outline
        path_outline = QPainterPath()
        path_outline.addRoundedRect(0, 0, self.width, self.height, self.edge_size, self.edge_size)
        painter.setPen(self.pen_default if not self.isSelected() else self.pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outline.simplified())

    def initSockets(self):
        pass
