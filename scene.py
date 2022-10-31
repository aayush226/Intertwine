import json
from collections import OrderedDict
from serializable import Serializable
from graphics_scene import GraphicsScene
from node import Node
from edge import Edge


class Scene(Serializable):
    def __init__(self):
        super().__init__()

        self.nodes = []  # initializes list to maintain all graph nodes in the scene
        self.edges = []  # initializes list to maintain all edges between the graph nodes in the scene

        self.scene_width = 64000  # defines width of scene
        self.scene_height = 64000  # defines height of scene

        self.adjacency_list = {}  # initializes dictionary to maintain adjacent nodes of every node in scene
        self.origin = None  # initializes origin from which depth first search should be performed
        self.initUI()  # initializes UI of scene

    def initUI(self):
        self.grScene = GraphicsScene(self)  # creates instance of GraphicsScene
        self.grScene.setGrScene(self.scene_width, self.scene_height)  # sets dimensions of scene

    def addNode(self, node):
        self.nodes.append(node)  # when called, this method adds node to the list "self.nodes"

    def addEdge(self, edge):
        self.edges.append(edge)  # when called, this method adds edge to the list "self.edges"

    def removeNode(self, node):
        if node in self.nodes:  # when called, this method removes node from the list "self.nodes"
            self.nodes.remove(node)
        else:
            print("Cant remove Node:", node, " from self.nodes as it doesnt exist in the list")

    def removeEdge(self, edge):
        if edge in self.edges:  # when called, this method removes edge from the list "self.edges"
            self.edges.remove(edge)
        else:
            print("Cant remove Edge:", edge, " from self.edges as it doesnt exist in the list")

    def clear(self):
        while len(self.nodes) > 0:
            self.nodes[0].remove()  # empties current list self.nodes when method deserialize() is called

    def dfs(self, visited, _list, node):
        # Performs Depth First Search on current selected node when "Focus Mode" button is pressed
        if node not in visited:
            node.setSelected(True)  # selects node
            visited.add(node)
            for x in _list[node]:
                for edge in self.edges:
                    if edge.start_socket.node.grNode == node and edge.end_socket.node.grNode == x:
                        edge.grEdge.setSelected(True)  # selects edge
                if x in _list:
                    self.dfs(visited, _list, x)
                else:
                    x.setSelected(True)
        return

    def focus(self):
        #  method is called when button "Focus Mode" is pressed
        for node in self.nodes:  # finds which node is currently selected
            if node.grNode.isSelected():
                self.origin = node  # sets currently selected node as origin from which dfs starts
        if self.origin.grNode in self.adjacency_list:
            # node exists in self.adjacency_list only if an edge starts from it (from output socket)
            # node doesn't exist in self.adjacency_list if an edge ends in itself (in input socket)
            # node network acts as a Directed Graph
            # edges are directed from output(right) socket to input(left) socket
            self.dfs(set(), self.adjacency_list, self.origin.grNode)
        else:
            return

    def saveToFile(self, filename):
        # saves current scene info with all nodes and edges to "graph.json.txt" file
        # calls self.serialize() to translate all nodes and edges in JSON format
        with open(filename, "w") as file:
            file.write(json.dumps(self.serialize(), indent=4))
            print("Saved to", filename, "successfully!")

    def loadFromFile(self, filename):
        # loads saved nodes and edges from "graph.json.txt" file
        # calls self.deserialize() to reconstruct all saved nodes and edges from JSON format
        with open(filename, "r") as file:
            raw_data = file.read()
            data = json.loads(raw_data)  # , encoding='utf-8'
            self.deserialize(data)

    def serialize(self):
        # serializes all nodes and edges in JSON format
        nodes, edges = [], []
        for node in self.nodes:
            nodes.append(node.serialize())
        for edge in self.edges:
            edges.append(edge.serialize())
        return OrderedDict([
            ('id', self.id),
            ('scene_width', self.scene_width),
            ('scene_height', self.scene_height),
            ('nodes', nodes),
            ('edges', edges),
        ])

    def deserialize(self, data, hashmap={}):
        # deserializes all nodes and edges saved in JSON format in graph.json.txt file
        self.clear()  # removes all nodes and edges currently in scene
        hashmap = {}

        for node_data in data['nodes']:  # re-creates saved nodes
            Node(self).deserialize(node_data, hashmap)

        for edge_data in data['edges']:  # re-creates saved edges
            Edge(self).deserialize(edge_data, hashmap)

        return True
