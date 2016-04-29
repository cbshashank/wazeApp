EC504 Waze App
======
Shashank Chitti sbalac@bu.edu
Brian Soares soaresb@bu.edu
Varshith Hakkithimmanahalli Anilkumar varshith@bu.edu

Goal of the project:
Given 2 datasets:
    Nodes (cal.cnode.txt): <nodeID> <longitude> <Latitude>
    Edges (cal.cedge.txt): <EdgeID><Start Node ID> < End Node ID> <Distance>
1) Draw the Nodes onto a California Map
2) Create a UI where if you click on an intersection point (node) it displays adjacent edges.
3) Click on "shortest path" button, click two points (nodes), and display 3 shortest paths from Node A to Node B

This project uses:
Python 2.7
    -Flask framework
HTML/CSS/Javascript
    -Google Maps API

Preloading the map takes O(n). N is number of nodes.
Since node:edge data preloaded into a python dictionary, (2) takes O(1).
Shortest path uses Yens KSP algorithm; (3) takes approximately O(n^2)


To run the project:
1) Change nodedirectory, and edgedirectory in wazeApp.py, to the path on your local machine.
2) Change _directory_data in graph.py to /data/json on your local machine
3) Run wazeApp.py
4) Run the app in your browser at the appropriate address.
