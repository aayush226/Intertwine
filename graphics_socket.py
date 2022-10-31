from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class GraphicsSocket(QGraphicsItem):
    def __init__(self, socket, socket_type=1):
        super().__init__(socket.node.grNode)

        self.socket = socket
        self.radius = 6
        self.outline_width = 1
        self.colors = [
            QColor("#FFFF7700"),
            QColor("#FF52e220"),
            QColor("#FF0056a6"),
            QColor("#FFa86db1"),
            QColor("#FFb54747"),
            QColor("#FFdbe220"),
        ]
        self.color_background = self.colors[socket_type]
        self.color_outline = QColor("#FF000000")

        self.pen = QPen(self.color_outline)
        self.pen.setWidthF(self.outline_width)
        self.brush = QBrush(self.color_background)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawEllipse(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)

    def boundingRect(self):
        return QRectF(
            - self.radius - self.outline_width,
            - self.radius - self.outline_width,
            2 * (self.radius + self.outline_width),
            2 * (self.radius + self.outline_width),
        )
