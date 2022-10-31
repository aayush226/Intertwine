from graphics_socket import GraphicsSocket
from serializable import Serializable
from collections import OrderedDict

top_left = 1
bottom_left = 2
top_right = 3
bottom_right = 4


class Socket(Serializable):
    def __init__(self, node, index=0, position=top_left, socket_type=1, multi_edges=True):
        # index stores in which position on the side the current socket is
        super().__init__()

        self.node = node
        self.index = index
        self.position = position
        self.socket_type = socket_type
        self.is_multi_edges = multi_edges

        self.grSocket = GraphicsSocket(self, self.socket_type)
        self.grSocket.setPos(*self.node.getSocketPosition(index, position))

        self.edges = []

    def getSocketPosition(self):
        res = self.node.getSocketPosition(self.index, self.position)
        return res

    def setConnectedEdge(self, edge=None):  # which edge is connected to the socket
        self.edges = edge

    def hasEdge(self):
        return self.edges is not None

    def addEdge(self, edge):
        self.edges.append(edge)

    def removeEdge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
        else:
            print("Cant remove Edge:", edge, " from self.edges as it doesnt exist in the list")

    def removeAllEdges(self):
        while self.edges:
            edge = self.edges.pop(0)
            edge.remove()

    def serialize(self):
        return OrderedDict([
            ('id', self.id),
            ('index', self.index),
            ('multi_edges', self.is_multi_edges),
            ('position', self.position),
            ('socket_type', self.socket_type),
        ])

    def deserialize(self, data, hashmap={}, restore_id=True):
        if restore_id: self.id = data['id']
        self.is_multi_edges = data['multi_edges']
        hashmap[data['id']] = self
        return True
