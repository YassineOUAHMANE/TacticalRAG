import faiss
from sentence_transformers import SentenceTransformer

# Dimension du modèle utilisé (384 pour 'all-MiniLM-L6-v2')
DIMENSION = 384

# Index FAISS (L2 = Euclidean, tu peux aussi essayer IndexFlatIP pour cosinus)
index = faiss.IndexFlatL2(DIMENSION)

# Embedder global (optionnel ici si tu le fais déjà dans embedder.py)
embed_model = SentenceTransformer('all-MiniLM-L6-v2')
