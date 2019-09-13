#! /usr/bin/python
import pydot

edges=[("Hello",2), ("Hello",3), ("Hello",4), (3,4)]
g=pydot.graph_from_edges(edges, directed=True)
g.write_jpeg('graph_from_edges_dot.jpg', prog='dot') 
g.write_svg( 'graph_from_edges_dot.svg', prog='dot') 
