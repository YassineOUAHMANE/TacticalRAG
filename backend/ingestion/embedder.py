from sentence_transformers import SentenceTransformer
import numpy as np

# Charger le modèle une fois
model = SentenceTransformer('all-MiniLM-L6-v2')  # Tu peux changer si besoin

def generate_embedding(text: str) -> np.ndarray:
    """
    Génère un vecteur d'embedding (shape: (1, dim)) pour le texte donné.
    """
    return model.encode([text]).astype('float32')
