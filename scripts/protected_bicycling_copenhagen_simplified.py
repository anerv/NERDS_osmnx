# -*- coding: utf-8 -*-
"""
Make a simplified graph of Copenhagen (and Frederiksberg) by removing
every non-necessary interstitial nodes and discriminating roads with
protected bicycling infrastructure (or safe place) and others, based on 
the criterion of bikewgrowth.
"""

import simplification
import utils
import networkx as nx
import osmnx as ox

if __name__ == "__main__":
    G = nx.read_gpickle('copenhagen_biketrack.pickle')
    