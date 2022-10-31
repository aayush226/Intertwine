# Welcome to Intertwine!

**Intertwine** is a multi-purpose graph based editor built using [PyQt5](https://pypi.org/project/PyQt5/)

https://user-images.githubusercontent.com/44861043/198516040-0841c8ba-7b34-49b5-97ee-95c4e4faf6aa.mp4

https://user-images.githubusercontent.com/44861043/198864206-a43e1217-d2a4-4de2-9c4a-ceb8afef90af.mp4

![MindMap_Github](https://user-images.githubusercontent.com/44861043/198703482-ea0ffa25-ce1f-48fb-8ae2-c5cd086d10af.PNG)

**Tutorial**:
- Double Click to add new Graph Node to the Scene
- Drag and Drop Or Click on 2 Sockets to create Edge between 2 Graph Nodes
- Click on Graph Node to select. Drag Selected Graph Node with Left Mouse Button to move
- Press Ctrl to select multiple Graph Nodes at once
- Use Mouse Wheel to Zoom In and Out at location
- Click and Drag Middle Mouse Button to Navigate/Pan Scene
- Click and Drag Left Mouse Button to Select Graph Nodes and Edges. Use *Delete* key to delete Selected Items
- Press Ctrl + S to Save Scene in **JSON format**
- Press Ctrl + L to Load Scene saved in **JSON format**

**Features**:
- Number of Atttributes, i.e., input and output Sockets of each Graph Node can be controlled
- Every Socket can have multiple edges
- When any Graph Node is moved, all its connected edges are updated
- On deleting any Graph Node, all its edges are also deleted
- Select Graph Node and click *Focus Mode* to perform **Depth First Search** on selected Graph Node to analyse data propagation through its adjacent nodes. Edges are directed from output to input socket
- 2 Edge Types - Bezier Curve Edge and Direct Edge are available
- Edge and Socket Colors can be controlled
- Graph Node color and dimensions can be modified
- Each Graph Node can be customized to contain textboxes, sliders, buttons etc
