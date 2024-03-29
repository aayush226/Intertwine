# Welcome to Intertwine!

**Intertwine** is a Graph based Editor for planning a manufacturing industry. It can be used in various ways such as process design and simulation, machine control, supply chain management and data analysis by providing a visual representation of the systems and networks.

Imagine a manufacturing process that includes several stages such as raw material input, assembly, testing, and packaging. Each stage of the process can be represented by a Graph Node in the editor. By connecting these nodes together, you can create a visual representation of the entire process, and easily identify any inefficiencies in the process.
For example, you can connect a graph node that represents the raw material input to a graph node that represents the assembly stage. This connection would indicate that the raw material is used in the assembly stage. By connecting all the nodes that represent each stage of the process, you can create a visual representation of the entire manufacturing process.

*Graph Nodes* can contain algorithms, functions, attributes etc with multiple input and output *Sockets*. *Edges* connect output socket of one Graph Node to input socket of another. Data/Information is propagated between Graph Nodes via Edges.

**Tutorial**:
- Double Click to add new Graph Node to the Scene
- Drag and Drop Or Click on 2 Sockets to create Edge between 2 Graph Nodes
- Click on Graph Node to select. Drag Selected Graph Node with Left Mouse Button to move

  https://user-images.githubusercontent.com/44861043/199162992-6731d93a-92de-45c3-b351-ceab9c9aa1bf.mp4

- Press Ctrl to select multiple Graph Nodes at once
- Use Mouse Wheel to Zoom In and Out at location
- Click and Drag Middle Mouse Button to Navigate/Pan Scene
- Click and Drag Left Mouse Button to Select Graph Nodes and Edges. Use *Delete* key to delete Selected Items
- Press Ctrl + S to Save Scene in **JSON format**
- Press Ctrl + L to Load Scene saved in **JSON format**

**Features**:
- Number of Atttributes, i.e., input and output Sockets of each Graph Node can be controlled

![image](https://user-images.githubusercontent.com/44861043/199062174-8d98a26d-35cd-408d-adff-5c2aac751dc5.png)

- Every Socket can have multiple input and output edges

![image](https://user-images.githubusercontent.com/44861043/199062952-391fa67d-df4c-439e-af66-f4737ebe7a0f.png)

- When any Graph Node is moved, all its connected edges are updated
- On deleting any Graph Node, all its edges are also deleted
- Select Graph Node and click *Focus Mode* to perform **Depth First Search** on selected Graph Node to analyse data propagation through its adjacent nodes. Edges are directed from output to input socket
- 2 Edge Types - Bezier Curve Edge and Direct Edge are available
- Edge and Socket Colors can be controlled
- Graph Node color and dimensions can be modified
- Each Graph Node can be customized to contain algorithms, functions etc and elements like textboxes, sliders, buttons etc

**Example**:

1: *Data Flow/Information Propagation* via Edges between Graph Nodes: Basic Arithmetic Example

https://user-images.githubusercontent.com/44861043/198516040-0841c8ba-7b34-49b5-97ee-95c4e4faf6aa.mp4

2: *Focus Mode* on a Graph Node using *Depth First Search* Example

https://user-images.githubusercontent.com/44861043/198864206-a43e1217-d2a4-4de2-9c4a-ceb8afef90af.mp4

3: Graph Nodes based *Mind Mapping* Example inspired by [Whimsical](https://whimsical.com/)

![MindMap_Github](https://user-images.githubusercontent.com/44861043/198703482-ea0ffa25-ce1f-48fb-8ae2-c5cd086d10af.PNG)


