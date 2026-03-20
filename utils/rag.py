import faiss
import numpy as np
from models.embeddings import get_embedding

documents = []
vectors = []

def load_data():
    global documents, vectors
    with open("data/skincare.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        if line.strip():
            documents.append(line)
            vectors.append(get_embedding(line))

def search(query):
    query_vec = np.array([get_embedding(query)])
    index = faiss.IndexFlatL2(len(query_vec[0]))
    index.add(np.array(vectors))
    _, I = index.search(query_vec, k=3)

    return [documents[i] for i in I[0]]