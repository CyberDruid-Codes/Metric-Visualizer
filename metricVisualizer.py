##
#Import Section

import networkx as nx

import matplotlib.pyplot as plt
##

##
class_length = 0

##
#method that formats the mitre result from dict to a list and gets the graph number of nodes

def formatting(classes):
    
    global class_length

    #Gets the length of the classes
    class_length = len(classes)

    #list that creates the right amount of numbers based on length

    count = []

    for x in range(class_length): 

        count.append(x)

    #formats the lists into a dict for the graph

    label_names = {count[i]:classes[i]for i in range(0, class_length)}

    return label_names 
##

##
#creates the graph 

def classcomp_graph():

    global class_length

    #Mock List of classes and methods per class
    classes = ["CCP", "Class 1","Class 2","Class 3","Class 4"]
    methods = ["C1.Method 1","C2.Method 1","C1.Method 2","C4.Method 1","C3.Method 1","C3.Method 3","C2.Method 2","C3.Method 3","C3.Method 4","C3.Method 5","C3.Method 2"]

    #creates labels for the nodes
    graph_labels = formatting(classes) 

    #Creates the graph, of the right length

    G=nx.star_graph(class_length-1)
    
    #for the sake of making things visual, this adds a "Cetral Class Point". Main Class from which the others are called.
    G.add_node("CCP")


    #Adds the class nodes edges based on how many classes there are

    nodes_len = class_length -1

    while (nodes_len >= 0):

        G.add_edge(0,nodes_len)

        nodes_len -=1


    #adds edges for each method of the class parsed 

    for met in methods: 

        if "C1" in met:

            G.add_edge("Class 1",met)

        elif "C2" in met:

            G.add_edge("Class 2",met)

        elif "C3" in met:

             G.add_edge("Class 3",met)

        elif "C4" in met:

             G.add_edge("Class 4",met)
    

    #Labels the nodes to the classes and methods names

    H=nx.relabel_nodes(G,graph_labels)
    

    #Options for the graph (e.g. colour of nodes, nodes size, edges size )

    options = {

        "node_color": "#ff6700",

        "width": 4,

        "node_size":3500,

        "with_labels": True,

        "font_size":9,

    }


    plt.figure(figsize=(10,9))

    nx.draw(H, **options)

    plt.savefig("class_complexity_visualization.jpeg")

    plt.show()
##


classcomp_graph()