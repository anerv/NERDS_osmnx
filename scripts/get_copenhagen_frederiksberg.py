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
    # we can also fill the copenhagen polygon, works too but don't know
    # if that is way more obvious and easy to read
    # metro_poly = shapely.ops.unary_union([
    #     shapely.geometry.Polygon(
    #         list(cop['geometry'][0][0].exterior.coords)
    #         ),
    #     cop['geometry'][0][1:]
    #     ])
    
    metro = ox.graph_from_polygon(metro_poly, simplify = False)
    ox.plot_graph(metro, figsize = (12, 8), bgcolor = 'w', 
                  node_color = 'black', node_size = 30, edge_color = 'r', 
                  edge_linewidth = 3)
    

    