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
    # TODO: Look to fill the polygon of copenhagen instead, and get it 
    # from osmnx in order to not need a file ?
    metro = ox.graph_from_polygon(metro_poly, simplify = False)