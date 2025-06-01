import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import normalize
from deepface import DeepFace

#---------------------------------------------------------------------------------------------------------------

x_train = np.loadtxt("treino_emb.txt")
x_train_norm = normalize(x_train)
y_train = np.loadtxt("treino_img.txt", dtype=str)

model = KNeighborsClassifier(n_neighbors=5, weights="distance", metric="euclidean")
model.fit(x_train_norm, y_train)

#---------------------------------------------------------------------------------------------------------------

#Processa a imagem recebida e salva os dados do reconhecimento facial
def proc_received_photo(photo):
    try:
        embedding = DeepFace.represent(img_path=photo, model_name='Facenet512', enforce_detection=True)[0]['embedding']
    except Exception:
        return -1

    emb_norm = normalize([embedding])
    dist, index = model.kneighbors(emb_norm, n_neighbors=5)

    if dist[0][0] > 0.6: #pessoa desconhecida
        return 0
    else: #pessoa conhecida
        return 1
