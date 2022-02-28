# -*- coding: utf-8 -*-
"""

"""

import geopandas as gpd
import shapely
import osmnx as ox

if __name__ == "__main__":
    cop = gpd.read_file("copenhagen_poly.geojson")
    fre = gpd.read_file("frederiksberg_poly.geojson")
    metro_poly = shapely.ops.unary_union([cop['geometry'][0],
                                          fre['geometry'][0]])
    metro = ox.graph_from_polygon(metro_poly, simplify = False)
    #ox.plot_graph(metro)
    # attr_dict = dict()
    # for edge in metro.edges():
    #     for attr in list(metro.edges[edge[0], edge[1], 0].keys()):
    #         if attr in attr_dict:
    #             if metro.edges[edge[0], edge[1], 0][attr] in attr_dict[attr]:
    #                 pass
    #             else:
    #                 attr_dict[attr].append(metro.edges[edge[0],
    #                                                    edge[1], 0][attr])
    #         else:
    #             attr_dict[attr] = [metro.edges[edge[0], edge[1], 0][attr]]