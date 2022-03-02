# -*- coding: utf-8 -*-
"""
"""

def get_every_edge_attributes(graph, ignore_key_list = []):
    """
    Get all the possible value for all attributes for edges of the graph 
    except the ones on a given ignore list. 
    See also get_specific_edge_attributes

    Parameters
    ----------
    graph : networkx Graph/DiGraph/MultiGraph/MultiDiGraph/...
        Graph where we want to simplify an attribute.
    
    ignore_key_list : list, optional
        Key we want to ignore. The default is [].

    Returns
    -------
    attr_dict : dict
        Dictionary of every possible values for every attributes except the
        ignored ones.

    """
    attr_dict = dict()
    for edge in graph.edges:
        for attr in list(graph.edges[edge].keys()):
            if attr in ignore_key_list:
                pass
            elif attr in attr_dict:
                if graph.edges[edge][attr] in attr_dict[attr]:
                    pass
                else:
                    attr_dict[attr].append(graph.edges[edge][attr])
            else:
                attr_dict[attr] = [graph.edges[edge][attr]]
    return attr_dict

def get_specific_edge_attributes(graph, take_key_list):
    """
    Get all the possible value for specific attributes for edges of the graph.
    See also get_every_edge_attributes

    Parameters
    ----------
    graph : networkx Graph/DiGraph/MultiGraph/MultiDiGraph/...
        Graph where we want to simplify an attribute.
    take_key_list : list
        List of the key we want to get.

    Returns
    -------
    attr_dict : dict
        Dictionary of every possible values for specified attributes.

    """
    attr_dict = dict()
    for key in take_key_list:
        attr_dict[key] = []
    for edge in graph.edges:
        for attr in list(graph.edges[edge].keys()):
            if attr in take_key_list:
                if graph.edges[edge][attr] in attr_dict[attr]:
                    pass
                else:
                    attr_dict[attr].append(graph.edges[edge][attr])
    return attr_dict
  
def simplify_edge_attribute_name(graph, key, name_list, simple_name):
    """
    Simplify an arbitrary list of name values for a given key into one.

    Parameters
    ----------
    graph : networkx Graph/DiGraph/MultiGraph/MultiDiGraph/...
        Graph where we want to simplify an attribute.
    key : str
        Name of the edges' attributes.
    name_list : list
        List of values for the given attribute we want to merge into one.
    simple_name : str
        Name for the fusion of every values in the given list.

    Returns
    -------
    ng : networkx Graph/DiGraph/MultiGraph/MultiDiGraph/...
        Graph with the modified attribute.

    """
    ng = graph.copy()
    for edge in ng.edges:
        if ng.edges[edge][key] in name_list:
            ng.edges[edge][key] = simple_name
    return ng

def add_edge_attribute(graph, attr_dict, name, bool_response = True):
    """
    Add an edge attribute where the value are binary bool based on whether the
    edge have a specific value for a given attribute, given as a dictionary.

    Parameters
    ----------
    graph : networkx Graph/DiGraph/MultiGraph/MultiDiGraph/...
        Graph on which we want to add an attribute.
    attr_dict : dict
        Dictionary where the key are the key of the edges' attributes and
        values are the values of those attributes that we want to take into
        account.
    name : str
        Name of the new attribute.
    bool_response : bool, optional
        Bool response if we find one of the values on one of the attributes of
        the edges from the dictionary. The default is True.

    Raises
    ------
    NameError
        Raised if the name is already an attribute of an edge of the graph,
        in order to avoid unintended mix.

    Returns
    -------
    ng : networkx Graph/DiGraph/MultiGraph/MultiDiGraph/...
        Graph with the new binary attribute.

    """
    ng = graph.copy()
    for edge in ng.edges:
        if name in ng.edges[edge]:
            raise NameError(
                "New attribute {} already in edge {}, use a new name".format(
                    name, edge)
                )
        for key in list(attr_dict.keys()):
            if ng.edges[edge][key] in attr_dict[key]:
                ng.edges[edge][name] = bool_response
            else:
                ng.edges[edge][name] = not bool_response
    return ng
  
