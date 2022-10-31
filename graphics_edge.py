from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math
from socket import *

edge_roundness = 100


class GraphicsEdge(QGraphicsPathItem):
    def __init__(self, edge, parent=None):
        super().__init__(parent)

        self.edge = edge

        self.color = QColor("#ffffff")
        self.color_selected = QColor("#E3242B")
        self.pen = QPen(self.color)
        self.pen_selected = QPen(self.color_selected)
        self.pen_dragging = QPen(self.color)
        self.pen_dragging.setStyle(Qt.DashLine)

        self.pen.setWidthF(2.5)
        self.pen_selected.setWidthF(2.5)
        self.pen_dragging.setWidthF(2.5)

        self.setFlag(QGraphicsItem.ItemIsSelectable)

        self.setZValue(-1)  # edges go under the socket

        self.posSource = [-100, -100]  # where edge will start
        self.posDestination = [200, 100]  # where it will end

    def setSource(self, x, y):
        self.posSource = [x, y]

    def setDestination(self, x, y):
        self.posDestination = [x, y]

    def boundingRect(self):
        return self.shape().boundingRect()

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        self.updatePath()

        if self.edge.end_socket is None:
            painter.setPen(self.pen_dragging)
        else:
            painter.setPen(self.pen if not self.isSelected() else self.pen_selected)

        painter.setBrush(Qt.NoBrush)
        painter.drawPath(self.path())

    def updatePath(self):
        # Handles drawing QPainterPath from Point A to B
        raise NotImplemented("This method has to be overriden in a child class")


class GraphicsEdgeDirect(GraphicsEdge):
    def updatePath(self):
        path = QPainterPath(QPointF(self.posSource[0], self.posSource[1]))
        path.lineTo(self.posDestination[0], self.posDestination[1])
        self.setPath(path)


class GraphicsEdgeBezier(GraphicsEdge):
    def updatePath(self):
        s = self.posSource
        d = self.posDestination
        dist = (d[0] - s[0]) * 0.5
        cpx_s = +dist
        cpx_d = -dist
        cpy_s = 0
        cpy_d = 0

        if self.edge.start_socket is not None:
            sspos = self.edge.start_socket.position

        if (s[0] > d[0] and sspos in (top_right, bottom_right)) or (s[0] < d[0] and sspos in (bottom_left, top_left)):
            cpx_d *= -1
            cpx_s *= -1

            cpy_d = (
                            (s[1] - d[1]) / math.fabs(
                        (s[1] - d[1]) if (s[1] - d[1]) != 0 else 0.00001
                    )
                    ) * edge_roundness
            cpy_s = (
                            (d[1] - s[1]) / math.fabs(
                        (d[1] - s[1]) if (d[1] - s[1]) != 0 else 0.00001
                    )
                    ) * edge_roundness

        path = QPainterPath(QPointF(self.posSource[0], self.posSource[1]))
        path.cubicTo(s[0] + cpx_s, s[1] + cpy_s, d[0] + cpx_d, d[1] + cpy_d, self.posDestination[0],
                     self.posDestination[1])
        self.setPath(path)

