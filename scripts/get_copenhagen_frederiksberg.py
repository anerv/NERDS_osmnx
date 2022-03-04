# -*- coding: utf-8 -*-
"""

"""

import geopandas as gpd
import shapely
import osmnx as ox

if __name__ == "__main__":
    cop = ox.geocode_to_gdf("Copenhagen Municipality")
    fre = ox.geocode_to_gdf("Frederiksberg Municipality")
    metro_poly = shapely.ops.unary_union([cop['geometry'][0],
                                          fre['geometry'][0]])
    metro = ox.graph_from_polygon(metro_poly, simplify = False)
    ox.plot_graph(metro, figsize = (12, 8), bgcolor = 'w', 
                  node_color = 'black', node_size = 30, edge_color = 'r', 
                  edge_linewidth = 3)