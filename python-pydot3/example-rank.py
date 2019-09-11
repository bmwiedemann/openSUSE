
graph = pydot.Dot('graphname', graph_type='digraph') 
subg = pydot.Subgraph('', rank='same') 
subg.add_node(pydot.Node('a')) 
graph.add_subgraph(subg) 
subg.add_node(pydot.Node('b')) 
subg.add_node(pydot.Node('c')) 
