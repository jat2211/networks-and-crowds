import networkx as nx
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

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
X =
y = 
clf = RandomForestClassifier(n_estimators=100)
print(cross_val_score(clf, X, y, cv=10).mean())