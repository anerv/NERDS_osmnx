# OSMnx

**OSMnx** is a Python package that lets you download geospatial data from OpenStreetMap and model, project, visualize, and analyze real-world street networks and any other geospatial geometries. You can download and model walkable, drivable, or bikeable urban networks with a single line of Python code then easily analyze and visualize them. You can just as easily download and work with other infrastructure types, amenities/points of interest, building footprints, elevation data, street bearings/orientations, and speed/travel time.

If you use OSMnx in your work, please cite the journal article.

**Citation info**: Boeing, G. 2017. "[OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks](https://geoffboeing.com/publications/osmnx-complex-street-networks/)." *Computers, Environment and Urban Systems* 65, 126-139. doi:10.1016/j.compenvurbsys.2017.05.004


## Changes to OSMnx

Based on the osmnx.simplification.simplify_graph function of **OSMnx**, we want to adapt it in such a way that it can avoid to simplify nodes where an attribute ( from an arbitrary list of attributes optionally given as an input) differ between the edges. To use network theory terminology, this is a way to generalize the function to multilayer graph. It allows us to simplify **OpenStreetMap** datafile while keeping the informations on the attributes we want to look at, for instance to discriminate between primary and secondary highway, or lane with and without bicycle path, information that is lost otherwise with the function from **OSMnx**.

After such simplification where we remove unnecessary (because we don't loose information without them) interstitional (because they are between other nodes) nodes, we want to independently be able to simplify the structure of the network while loosing as less as possible information :
* Go from a directed multigraph to a directed graph by avoiding multiple edges and getting rid of the more ‘theoretical’ edges that are added to represent traffic on both directions. In order to do this, we will need to create unnecessary interstitional nodes so that there is no self-loop or mutliple path between two nodes.
* Go from a directed graph to an undirected graph
This step helps us to manipulate the network afterwards, for instance to use metrics that works only on graph such as betweenness centrality.

![simplification_image](https://user-images.githubusercontent.com/61236142/155726851-92bccbc4-10fb-4fd3-9fdc-c0673cd284fd.jpg)

## To add as a local package

Based on the [The Good Research Code Handbook](https://goodresearch.dev/setup.html#pip-install-your-package), you should:
* Put yourself on your virtual environment and on the folder, such as /NERDS_osmnx
* Run pip install -e .

". indicates that we’re installing the package in the current directory. -e indicates that the package should be editable. That means that if you change the files inside the [source] folder, you don’t need to re-install the package for your changes to be picked up by Python."
