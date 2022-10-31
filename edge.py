from collections import OrderedDict
from serializable import Serializable
from graphics_edge import *
from scene import *
direct_edge = 1
bezier_edge = 2


class Edge(Serializable):
    def __init__(self, scene, start_socket=None, end_socket=None, edge_type=direct_edge):
        super().__init__()

        self.scene = scene

        self._start_socket = None
        self._end_socket = None

        self.start_socket = start_socket
        self.end_socket = end_socket
        self.edge_type = edge_type

        self.scene.addEdge(self)
        self.logic()

    @property
    def start_socket(self): return self._start_socket

    @start_socket.setter
    def start_socket(self, value):
        # if assigned to some socket before, delete us from the socket
        if self._start_socket is not None:
            self._start_socket.removeEdge(self)

        # assign new start socket
        self._start_socket = value
        # addEdge to the Socket class
        if self.start_socket is not None:
            self.start_socket.addEdge(self)

    @property
    def end_socket(self): return self._end_socket

    @end_socket.setter
    def end_socket(self, value):
        # if we were assigned to some socket before, delete us from the socket
        if self._end_socket is not None:
            self._end_socket.removeEdge(self)

        # assign new end socket
        self._end_socket = value
        # addEdge to the Socket class
        if self.end_socket is not None:
            self.end_socket.addEdge(self)

    @property
    def edge_type(self): return self._edge_type

    @edge_type.setter
    def edge_type(self, value):
        if hasattr(self, 'grEdge') and self.grEdge is not None:
            self.scene.grScene.removeItem(self.grEdge)

        self._edge_type = value

        if self.edge_type == direct_edge:
            self.grEdge = GraphicsEdgeDirect(self)
        elif self.edge_type == bezier_edge:
            self.grEdge = GraphicsEdgeBezier(self)
        else:
            self.grEdge = GraphicsEdgeBezier(self)

        self.scene.grScene.addItem(self.grEdge)

        if self.start_socket is not None:
            self.updatePositions()

    '''def logic(self):
        if self.end_socket is not None:
            num = self.start_socket.node.content.textbox.toPlainText()
            textbox = self.end_socket.node.content.textbox
            if self.end_socket.node.node_type == "Add":
                if textbox.toPlainText() == "":
                    textbox.setText(num)
                else:
                    num2 = int(textbox.toPlainText())
                    textbox.setText(str(int(num) + num2))
            elif self.end_socket.node.node_type == "Subtract":
                if textbox.toPlainText() == "":
                    textbox.setText(num)
                else:
                    num2 = int(textbox.toPlainText())
                    textbox.setText(str(abs(int(num) - num2)))
            elif self.end_socket.node.node_type == "Multiply":
                if textbox.toPlainText() == "":
                    textbox.setText(num)
                else:
                    num2 = int(textbox.toPlainText())
                    textbox.setText(str(int(num)*num2))'''
    def logic(self):
        if self.end_socket is not None:
            key = self.start_socket.node.grNode
            self.scene.adjacency_list.setdefault(key, []).append(self.end_socket.node.grNode)

    def updatePositions(self):
        source_pos = self.start_socket.getSocketPosition()
        source_pos[0] += self.start_socket.node.grNode.pos().x()
        source_pos[1] += self.start_socket.node.grNode.pos().y()
        self.grEdge.setSource(*source_pos)
        if self.end_socket is not None:
            end_pos = self.end_socket.getSocketPosition()
            end_pos[0] += self.end_socket.node.grNode.pos().x()
            end_pos[1] += self.end_socket.node.grNode.pos().y()
            self.grEdge.setDestination(*end_pos)
        else:
            self.grEdge.setDestination(*source_pos)
        self.grEdge.update()

    def remove_from_sockets(self):

        self.end_socket = None
        self.start_socket = None

    def remove(self):
        self.remove_from_sockets()
        self.scene.grScene.removeItem(self.grEdge)
        self.grEdge = None
        try:
            self.scene.removeEdge(self)
        except ValueError:
            pass
        # when nodes are removed edges are also removed. when that edge is selected which
        # means it must be removed it is not found in the list. so gives value error

    def serialize(self):
        return OrderedDict([
            ('id', self.id),
            ('edge_type', self.edge_type),
            ('start', self.start_socket.id),
            ('end', self.end_socket.id),
        ])

    def deserialize(self, data, hashmap={}):
        self.id = data['id']
        self.start_socket = hashmap[data['start']]
        self.end_socket = hashmap[data['end']]
        self.edge_type = data['edge_type']


