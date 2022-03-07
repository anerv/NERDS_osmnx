# -*- coding: utf-8 -*-
"""

"""

import osmnx as ox

if __name__ == "__main__":
    default_access = '["access"!~"private"]'
    overpass_filter = (
        f'["highway"]["area"!~"yes"]{default_access}'
        f'["highway"!~"abandoned|bridleway|bus_guideway|construction|corridor|cycleway|elevator|'
        f"escalator|footway|path|pedestrian|planned|platform|proposed|raceway|service|"
        f'steps|track"]'
        f'["motor_vehicle"!~"no"]["motorcar"!~"no"]'
        f'["service"!~"alley|driveway|emergency_access|parking|parking_aisle|private"]'
    )
    timeout = 180
    memory = None
    maxsize = f"[maxsize:{memory}]"
    overpass_settings = "[out:json][timeout:{timeout}]{maxsize}".format(
        timeout = timeout, maxsize = maxsize)
    dummy = [[15.2, 55.6], [15.3, 55.7], [15.1, 55.5]]
    query_str_drive = f"{overpass_settings};(way{overpass_filter}(poly:'{dummy}');>;);out;"
    print("query_str_drive:", query_str_drive)
    
    custom_filter = '["highway"~"motorway"]'
    query_str_custom = f"{overpass_settings};(way{custom_filter}(poly:'{dummy}');>;);out;"
    print("query_str_custom:", query_str_custom)
    