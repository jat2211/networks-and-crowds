# 4.py
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

dim = [50,70]
walk_len = [40,60]
num_walks = [10,15]
max_score = 0
best_d = 0
best_w = 0
best_n = 0
for d in dim:
    for w in walk_len:
        for n in num_walks:
            node2vec = Node2Vec(G, dimensions=d, walk_length=w, num_walks=n, q=4, p=1)
            model = node2vec.fit(window=10, min_count=1)

            #df_validation = df.head(int(len(df)*(10/100))) # validation data
            #df_train = df.iloc[int(len(df)*(10/100)):] # training data
            X = df.iloc[:,2:]
            y = df.iloc[:, 1]
            clf = RandomForestClassifier(n_estimators=100)
            score = cross_val_score(clf, X, y, cv=10).mean()
            if score > max_score:
                max_score = score
                best_d = d
                best_w = w
                best_n = n

node2vec = Node2Vec(G, dimensions=best_d, walk_length=best_w, num_walks=best_n, q=4, p=1)
model = node2vec.fit(window=10, min_count=1)

X = df.iloc[:,2:]
y = df.iloc[:, 1]
clf = RandomForestClassifier(n_estimators=100)
score = cross_val_score(clf, X, y, cv=10).mean()
print(score)
