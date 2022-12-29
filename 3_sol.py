# 3.py
import networkx as nx
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from node2vec import Node2Vec
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

# generate features X and labels y
node2vec = Node2Vec(G, dimensions=50, walk_length=40, num_walks=10, q=4, p=1)
model = node2vec.fit(window=10, min_count=1)

for i, node in enumerate(G.nodes()):
    if i == 0:
        row = list(model.wv[node])
        row.insert(0, node)
        row.insert(1, label[node])
        df = pd.DataFrame([row])
    else:
        row = list(model.wv[node])
        row.insert(0, node)
        row.insert(1, label[node])
        df.loc[len(df)] = row

X = df.iloc[:,2:]
y = df.iloc[:, 1]
clf = RandomForestClassifier(n_estimators=100)
print(cross_val_score(clf, X, y, cv=10).mean())
