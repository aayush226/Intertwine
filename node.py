from socket import *
from node_content import NodeContent
from graphics_node import GraphicsNode
from serializable import Serializable
from collections import OrderedDict


class Node(Serializable):
    def __init__(self, scene, title="Undefined Node", inputs=[], outputs=[], node_type="integer"):
        super().__init__()

        self._title = title
        self.scene = scene
        self.node_type = node_type

        self.content = NodeContent(self, self.node_type)  # creates instance of NodeContent class
        self.grNode = GraphicsNode(self)  # creates instance of GraphicsNode class

        self.title = title

        self.scene.addNode(self)  # adds this node to list
        self.scene.grScene.addItem(self.grNode)  # adds node item to scene

        self.socket_spacing = 22  # defines how far apart sockets will be in case of multiple sockets

        self.inputs = []  # defines input sockets list
        self.outputs = []  # defines output sockets list

        counter = 0
        for item in inputs:
            socket = Socket(node=self, index=counter, position=top_left, socket_type=item, multi_edges=False)
            counter += 1
            self.inputs.append(socket)

        counter = 0
        for item in outputs:
            socket = Socket(node=self, index=counter, position=top_right, socket_type=item, multi_edges=True)
            counter += 1
            self.outputs.append(socket)

    def setPos(self, x, y):  # sets node position in scene
        self.grNode.setPos(x, y)

    @property
    def pos(self):
        return self.grNode.pos()  # QPointF

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.grNode.title = self._title

    def getSocketPosition(self, index, position):
        # returns socket position
        x = 0 if (position in (top_left, bottom_left)) else self.grNode.width

        if position in (bottom_left, bottom_right):
            y = self.grNode.height - self.grNode.edge_size - self.grNode._padding - index * self.socket_spacing
        else:
            y = self.grNode.title_height + self.grNode._padding + self.grNode.edge_size + index * self.socket_spacing

        return [x, y]

    def updateConnectedEdges(self):
        # all edges of current node are updated when node is moved
        for socket in self.inputs + self.outputs:
            for edge in socket.edges:
                edge.updatePositions()

    def remove(self):
        # removes itself and all its edges from scene
        for socket in (self.inputs + self.outputs):
            for edge in socket.edges:
                edge.remove()

        self.scene.grScene.removeItem(self.grNode)
        self.grNode = None  # makes sure its removed
        self.scene.removeNode(self)

    def serialize(self):
        # when file is saved, node is serialized to json format
        inputs, outputs = [], []
        for socket in self.inputs:
            inputs.append(socket.serialize())
        for socket in self.outputs:
            outputs.append(socket.serialize())
        return OrderedDict([
            ('id', self.id),
            ('title', self.title),
            ('pos_x', self.grNode.scenePos().x()),
            ('pos_y', self.grNode.scenePos().y()),
            ('inputs', inputs),
            ('outputs', outputs),
            ('content', self.content.serialize()),
        ])

    def deserialize(self, data, hashmap={}):
        # when saved file is loaded, node is re-instated
        self.id = data['id']
        hashmap[data['id']] = self

        self.setPos(data['pos_x'], data['pos_y'])
        self.title = data['title']

        data['inputs'].sort(key=lambda socket: socket['index'] + socket['position'] * 10000)
        data['outputs'].sort(key=lambda socket: socket['index'] + socket['position'] * 10000)

        self.inputs = []
        for socket_data in data['inputs']:
            new_socket = Socket(node=self, index=socket_data['index'], position=socket_data['position'],
                                socket_type=socket_data['socket_type'])
            new_socket.deserialize(socket_data, hashmap)
            self.inputs.append(new_socket)

        self.outputs = []
        for socket_data in data['outputs']:
            new_socket = Socket(node=self, index=socket_data['index'], position=socket_data['position'],
                                socket_type=socket_data['socket_type'])
            new_socket.deserialize(socket_data, hashmap)
            self.outputs.append(new_socket)
        return True


