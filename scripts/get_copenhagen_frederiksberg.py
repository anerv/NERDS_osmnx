# -*- coding: utf-8 -*-
"""

"""

import shapely
import osmnx as ox

if __name__ == "__main__":
    cop = ox.geocode_to_gdf("Copenhagen Municipality")
    fre = ox.geocode_to_gdf("Frederiksberg Municipality")
    metro_poly = shapely.ops.unary_union([cop['geometry'][0],
                                          fre['geometry'][0]])
    # We can also fill the copenhagen polygon, works too but don't know
    # if that is way more obvious and easy to read
    
    # metro_poly = shapely.ops.unary_union([
    #     shapely.geometry.Polygon(
    #         list(cop['geometry'][0][0].exterior.coords)
    #         ),
    #     cop['geometry'][0][1:]
    #     ])
    
    metro = ox.graph_from_polygon(metro_poly, simplify = True)
    ox.plot_graph(metro, figsize = (12, 8), bgcolor = 'w', 
                  node_color = 'black', node_size = 30, edge_color = 'r', 
                  edge_linewidth = 3)
    
    # We can look at how the haversine is measured
    
    #import haversine
    #import numpy as np
    # index = 1
    # f_point = list(metro.edges)[index][0]
    # s_point = list(metro.edges)[index][1]
    # x1, y1 = metro.nodes[f_point]['x'], metro.nodes[f_point]['y']
    # x2, y2 = metro.nodes[s_point]['x'], metro.nodes[s_point]['y']
    # h = round(haversine.haversine(
    #     [y1, x1], [y2, x2], unit = haversine.Unit.METERS), 3)
    # l = metro.edges[f_point, s_point, list(metro.edges)[index][2]]['length']
    # print("Length measured by haversine = {} \n OSM value = {}".format(
    #     h, l))
    # print("Relative difference of {} %".format(np.abs(100 * (l - h)/l)))