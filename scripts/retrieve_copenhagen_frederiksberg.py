# -*- coding: utf-8 -*-
"""

"""

import geopandas as gpd
import shapely
import osmnx as ox
import networkx as nx
import folium
import numpy as np

def get_edges_attributes_list(graph):
    "Get all the possible value for all attributes for edges of the graph"
    if type(graph) is nx.classes.multidigraph.MultiDiGraph:
        attr_dict = dict()
        for edge in metro.edges():
            for attr in list(metro.edges[edge[0], edge[1], 0].keys()):
                if attr in attr_dict:
                    if metro.edges[edge[0], edge[1], 0][attr] in attr_dict[attr]:
                        pass
                    else:
                        attr_dict[attr].append(metro.edges[edge[0],
                                                            edge[1], 0][attr])
                else:
                    attr_dict[attr] = [metro.edges[edge[0], edge[1], 0][attr]]
    elif type(graph) is nx.classes.graph.Graph:
        attr_dict = dict()
        for edge in metro.edges():
            for attr in list(metro.edges[edge[0], edge[1]].keys()):
                if attr in attr_dict:
                    if metro.edges[edge[0], edge[1]][attr] in attr_dict[attr]:
                        pass
                    else:
                        attr_dict[attr].append(metro.edges[edge[0],
                                                            edge[1]][attr])
                else:
                    attr_dict[attr] = [metro.edges[edge[0], edge[1]][attr]]
    return attr_dict
        

if __name__ == "__main__":
    cop = gpd.read_file("copenhagen_poly.geojson")
    fre = gpd.read_file("frederiksberg_poly.geojson")
    metro_poly = shapely.ops.unary_union([cop['geometry'][0],
                                          fre['geometry'][0]])
    metro = ox.graph_from_polygon(metro_poly, simplify = False)
    for (u, v, k) in metro.edges:
        metro.edges[u, v, k]['random_color'] = float(np.random.randint(3))/2.
    ec = ox.plot.get_edge_colors_by_attr(metro, 'random_color', cmap='Set1')
    ox.plot_graph(metro, figsize = (12, 8), bgcolor = 'w', 
                  node_color = 'black', node_size = 5, edge_color = ec, 
                  edge_linewidth = 1.5)
    
    
    ####For visualisation purpose only !
    # cf = '["highway"~"cycleway|pedestrian|primary|secondary|tertiary"]'
    # metro = ox.graph_from_polygon(metro_poly, simplify = False,
    #                               custom_filter = cf)
    # highway_color = dict()
    # highway_color['primary'] = 'red'
    # highway_color['primary_link'] = 'lightred'
    # highway_color['secondary'] = 'orange'
    # highway_color['secondary_link'] = 'lightorange'
    # highway_color['tertiary'] = 'yellow'
    # highway_color['tertiary_link'] = 'lightyellow'
    # highway_color['pedestrian'] = 'blue'
    # highway_color['cycleway'] = 'green'
    
    # COPENHAGEN_COORD = [55.6761, 12.5683]
    # m = folium.Map(location = COPENHAGEN_COORD, zoom_start = 12) 
    # for net_type in list(highway_color.keys()):
    #     new_layer = folium.FeatureGroup(net_type, show = False)
    #     edge_list = [(u,v,k,d) for u,v,k,d in metro.edges(keys=True, data=True)
    #                  if d['highway']==net_type]
    #     for edge in edge_list:
    #         pos = [[metro.nodes[edge[0]]['y'], metro.nodes[edge[0]]['x']],
    #                [metro.nodes[edge[1]]['y'], metro.nodes[edge[1]]['x']]]
    #         folium.PolyLine(locations = pos,
    #                         color = highway_color[net_type]).add_to(new_layer)
    #     new_layer.add_to(m)
    # for node in metro.nodes():
    #     folium.Circle(location = [metro.nodes[node]['y'],
    #                                   metro.nodes[node]['x']],
    #                      color = 'black', radius = 1).add_to(m)
    # folium.LayerControl().add_to(m)  
    # m.save("./non_simplified_copenhagen_map.html")