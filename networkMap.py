##Pull in the datasets and transform them to a to and a from list
import csv
with open("engagementPairs.csv") as f: 
    reader = csv.reader(f)
    my_list = list(reader)

pairs = (my_list[1:434])

to_list = []
from_list = []
for pair in pairs: 
    to_list.append(pair[0])
    from_list.append(pair[1])

# libraries
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
 
# Build a dataframe with 4 connections
df = pd.DataFrame({ 'from': from_list,  'to': to_list})
df
 
# Build your graph
G=nx.from_pandas_edgelist(df, 'from', 'to')

# Plot it
nx.draw(G, with_labels=True, node_size=800, node_color="skyblue", node_shape="o", alpha=0.6
, linewidths=1, font_size=8, font_color="grey", font_weight="bold", width=2, edge_color="grey")
plt.show()
