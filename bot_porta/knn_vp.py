import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# -------------------------------------------------------------------------------------------------------------------------------------------

x_train = np.loadtxt("treino_emb.txt")
x_train_norm = normalize(x_train)
y_train = np.loadtxt("treino_img.txt", dtype=str)

x_valid = np.loadtxt("validacao_emb.txt")
x_valid_norm = normalize(x_valid)
y_valid = np.loadtxt("validacao_img.txt", dtype=str)

x_test = np.loadtxt("teste_emb.txt")
x_test_norm = normalize(x_test)
y_test = np.loadtxt("teste_img.txt", dtype=str)

x_test_desc = np.loadtxt("desc_emb.txt")
x_test_desc_norm = normalize(x_test_desc)
y_test_desc = np.loadtxt("desc_img.txt", dtype=str)

x_test_all = np.concatenate([x_test_norm, x_test_desc_norm])
y_test_all = np.concatenate([y_test, y_test_desc])

# -------------------------------------------------------------------------------------------------------------------------------------------

#Ajuste de parâmetros
for i in range(1, 15):
    model = KNeighborsClassifier(n_neighbors=i, weights="distance", metric="euclidean")
    model.fit(x_train_norm, y_train)

    pred = model.predict(x_valid_norm)
    #prob = model.predict_proba(x_valid_norm)
    print("k = ", i)
    print(classification_report(y_valid, pred, zero_division=0))
    #print(accuracy_score(y_valid, pred))
    #print(confusion_matrix(y_valid, pred))

    '''
    for i in range(30):
        print(f"Class:\t{y_test_all[i]}")
        print(f"Pred:\t{pred[i]}")
        print(f"Prob: {prob[i]}\n")
    '''

# -------------------------------------------------------------------------------------------------------------------------------------------
'''
#Gráfico
X_all = np.concatenate([x_train_norm, x_valid_norm])
y_all = np.concatenate([y_train, y_valid])

pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_all)

plt.figure(figsize=(10, 8))
for label in np.unique(y_all):
    idx = y_all == label
    plt.scatter(X_2d[idx, 0], X_2d[idx, 1], label=label, alpha=0.7)

plt.legend()
plt.grid(True)
plt.show()
'''
