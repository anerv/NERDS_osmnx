# -*- coding: utf-8 -*-

import numpy as np
import networkx as nx
import osmnx as ox
import nerds_osmnx.simplification

def normalized_array(arr):
    return (arr - min(arr))/(max(arr) - min(arr))

def average_node_to_edge(G, attr_name):
    G = G.copy()
    for edge in G.edges:
        G.edges[edge][attr_name] = np.mean([
            G.nodes[edge[0]][attr_name],
            G.nodes[edge[1]][attr_name]
            ])
    return G

if __name__ == "__main__":
    G = ox.graph_from_bbox(43.5337, 43.5233, 5.4577, 5.4376,
                           simplify = False)
    ox.plot_graph(G, figsize = (12, 8), bgcolor = 'w', 
                  node_color = 'r', node_size = 30, edge_color = 'black', 
                  edge_linewidth = 3)
    G = nerds_osmnx.simplification.simplify_graph(G)
    ox.plot_graph(G, figsize = (12, 8), bgcolor = 'w', 
                  node_color = 'r', node_size = 30, edge_color = 'black', 
                  edge_linewidth = 3)
    G = nerds_osmnx.simplification.multidigraph_to_graph(G)

    # ox.plot_graph(G, figsize = (12, 8), bgcolor = 'w', 
    #               node_color = 'r', node_size = 30, edge_color = 'black', 
    #               edge_linewidth = 3)

    betw = nx.betweenness_centrality(G, weight = "length")
    clos = nx.closeness_centrality(G, distance = "length")
    katz = nx.katz_centrality(G) # not relevant but for another look
    nx.set_node_attributes(G, betw, name = "betweenness")
    nx.set_node_attributes(G, clos, name = "closeness")
    nx.set_node_attributes(G, katz, name = "katz")
    betw_nc = ox.plot.get_node_colors_by_attr(G, "betweenness")
    clos_nc = ox.plot.get_node_colors_by_attr(G, "closeness")
    katz_nc = ox.plot.get_node_colors_by_attr(G, "katz")
    # ox.plot_graph(G, figsize = (12, 8), bgcolor = 'w', 
    #               node_color = betw_nc, node_size = 30, edge_color = 'black', 
    #               edge_linewidth = 3)
    # ox.plot_graph(G, figsize = (12, 8), bgcolor = 'w', 
    #               node_color = clos_nc, node_size = 30, edge_color = 'black', 
    #               edge_linewidth = 3)
    # ox.plot_graph(G, figsize = (12, 8), bgcolor = 'w', 
    #               node_color = katz_nc, node_size = 30, edge_color = 'black', 
    #               edge_linewidth = 3)

    A = 0.3
    B = 0.3
    C = 0.3
    cost_function = (A * normalized_array(np.array(list(betw.values()))) +
                     B * normalized_array(np.array(list(clos.values()))) +
                     C * normalized_array(np.array(list(katz.values()))))
    cost_dict = dict(zip(betw.keys(), cost_function))
    nx.set_node_attributes(G, cost_dict, name = "cost")
    cost_nc = ox.plot.get_node_colors_by_attr(G, "cost")
    # ox.plot_graph(G, figsize = (12, 8), bgcolor = 'w', 
    #               node_color = cost_nc, node_size = 30, edge_color = 'black', 
    #               edge_linewidth = 3)

    G = average_node_to_edge(G, 'cost')
    cost_ec = ox.plot.get_edge_colors_by_attr(G, "cost")
    # ox.plot_graph(G, figsize = (12, 8), bgcolor = 'w', 
    #               node_color = 'black', node_size = 30, edge_color = cost_ec, 
    #               edge_linewidth = 3)

    e_betw = nx.edge_betweenness_centrality(G, weight = "length")
    nx.set_edge_attributes(G, e_betw, name = "edge_betweenness")
    G = average_node_to_edge(G, 'betweenness')
    betw_ec = ox.plot.get_edge_colors_by_attr(G, "betweenness")
    ebet_ec = ox.plot.get_edge_colors_by_attr(G, "edge_betweenness")
    #osmx.plot_graph only take multigraph because it retrieves keys
    G = nx.MultiGraph(G) 
    ox.plot_graph(G, figsize = (12, 8), bgcolor = 'w', 
                  node_color = 'black', node_size = 30, edge_color = betw_ec, 
                  edge_linewidth = 3)
    ox.plot_graph(G, figsize = (12, 8), bgcolor = 'w', 
                  node_color = 'black', node_size = 30, edge_color = ebet_ec, 
                  edge_linewidth = 3)