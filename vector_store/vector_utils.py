from .vector_config import index
import numpy as np
import faiss
from typing import List
from backend.ingestion.indexer import load_documents
from vector_store.state import indexed_documents



def add_to_index(embeddings: List[List[float]], texts: List[str]):
    """
    Ajoute des embeddings + leurs textes associés dans l'index.
    """
    vectors = np.array(embeddings).astype('float32')
    index.add(vectors)
    indexed_documents.extend(texts)

def embed_text(text: str) -> np.ndarray:
    """
    Fonction utilitaire si tu veux générer un embedding ici.
    Sinon utilise directement generate_embedding() de embedder.py
    """
    from .vector_config import embed_model
    return np.array(embed_model.encode([text])).astype('float32')

def search_similar(query: str, k: int = 5) -> List[str]:
    query_vector = embed_text(query)
    distances, indices = index.search(query_vector, k)

    results = []
    for i in indices[0]:
        if i < len(indexed_documents) and len(indexed_documents)!=0:
            results.append(indexed_documents[i])
        else:
            print(f"[WARNING] index {i} hors limites — indexé : {len(indexed_documents)}")
    return results


def get_stats():
    return {
        "documents_indexed": index.ntotal,
        "total_tokens": sum(len(doc.split()) for doc in indexed_documents)
    }

def save_index(path="index.faiss"):
    faiss.write_index(index, path)

def load_index(path="index.faiss"):
    global index
    
    index = faiss.read_index(path)

def initialize_vector_store(index_path="index.faiss", docs_path="documents.json"):
    try:
        load_index(index_path)
    except:
        print(f"⚠️ Pas de {index_path}, index vide initialisé.")

    try:
        load_documents(docs_path)
    except:
        print(f"⚠️ Pas de {docs_path}, documents non chargés.")

