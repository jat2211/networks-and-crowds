import networkx as nx
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from networkx.algorithms.centrality import degree_centrality
from networkx.algorithms.centrality import closeness_centrality
from networkx.algorithms.centrality import betweenness_centrality

# generating the graph
def get_graph(file):
    G = nx.Graph()
    file = open(file, 'r')
    lines = file.readlines()
    for i in lines:
        edge = i.strip().split()
        G.add_edge(edge[0],edge[1])
    return G
G = get_graph('email-Eu-core.txt')

# getting the label
def get_label(file):
    labels = {}
    file = open(file, 'r')
    lines = file.readlines()
    for i in lines:
        label = i.strip().split()
        labels[label[0]] = label[1]
    return labels

label = get_label('email-Eu-core-department-labels.txt')

degree_dict = degree_centrality(G)
closeness_dict = closeness_centrality(G)
betweenness_dict = betweenness_centrality(G)

nodes = []
degrees = []
closeness = []
betweenness = []
labels = []

for node in G.nodes():
    nodes.append(node)
    degrees.append(float(degree_dict[node]))
    closeness.append(float(closeness_dict[node]))
    betweenness.append(float(betweenness_dict[node]))
    labels.append(label[node])

df = pd.DataFrame()
df['Nodes'] = nodes
df['Degree'] = degrees
df['Closeness'] = closeness
df["Betweenness"] = betweenness
df['Label'] = labels

# generate features X and labels y
X = df[['Degree','Closeness','Betweenness']]
y = df['Label']
clf = RandomForestClassifier(n_estimators=100)
print(cross_val_score(clf, X, y, cv=10).mean())
