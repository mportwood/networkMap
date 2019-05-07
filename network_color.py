#Adapted from: 
# http://jonathansoma.com/lede/algorithms-2017/classes/networks/networkx-graphs-from-source-target-dataframe/

# Import libraries
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
df = pd.read_csv("engagementPairs.csv")
# print(df.head()) #prints first 5 relationships

## Create a graph based on the columns in the data source
g = nx.from_pandas_edgelist(df, source='partner_name', target='im_team_name') 

## Make a list of all IM Teams
im_team = list(df.im_team_name.unique())

##Make a list of all IM Partners
partners = list(df.partner_name.unique())
#Count the list of Partners orgs to display in the subtitle later
partner_cnt = len(partners)

##I'll use the degree function to see how many connxns a given team has
# print(g.degree('EAA')) #38
##I can use this patter to create a list of all connxns for all im_teams using a list comprehension
# [g.degree(im_team) for im_team in im_team] #[38, 32, 22, 31, 18, 34, 60, 18]

##Set Figure Size 
plt.figure(figsize=(20, 14))

## Create a layout for the nodes 
layout = nx.kamada_kawai_layout(g) #gives more of a circular kind of layout
# layout = nx.spring_layout(g,iterations=50) #this one is good, but works a little less consistently

# Go through every im_team name, ask the graph how many connections it has. 
# Apply a multiplier to up circle size based on partnership count
im_team_size = [g.degree(im_team) * 70 for im_team in im_team]
nx.draw_networkx_nodes(g, 
                       layout, 
                       nodelist=im_team, 
                       node_size=im_team_size, # a LIST of sizes, based on g.degree
                       node_color='lightblue')

# Draw all Partnerships in gray
nx.draw_networkx_nodes(g, layout, nodelist=partners, node_color='#cccccc', node_size=100)

# Draw common Partners and color them orange
popular_partners = [partners for partners in partners if g.degree(partners) > 1]
nx.draw_networkx_nodes(g, layout, nodelist=popular_partners, node_color='orange', node_size=100)

nx.draw_networkx_edges(g, layout, width=1, edge_color="#cccccc")

node_labels = dict(zip(im_team, im_team))
nx.draw_networkx_labels(g, layout, labels=node_labels)

# 4. Turn off the axis and add a title/subtitle
plt.axis('off')
plt.suptitle("    IM Engagement Map", fontsize=20)
plt.title("Count of IM Teams: " + str(len(im_team_size)) + 
    "; Count of IM partners: " + str(partner_cnt)+ "; Count of Common Partners: " + str(len(popular_partners))
    , fontsize=8.5)

# 5. Use the show function in matplotlib to show the graph
plt.show()