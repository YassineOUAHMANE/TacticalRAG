import faiss
import json
import os
from vector_store.vector_config import index
from vector_store.state import indexed_documents  # ✅ Accès direct à la mémoire partagée


def add_document_to_index(text: str, embedding):
    from vector_store.vector_utils import index, indexed_documents
    index.add(embedding)
    indexed_documents.append(text)



def save_documents(path="documents.json"):
    """
    Sauvegarde les textes associés à l'index.
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(indexed_documents, f, ensure_ascii=False, indent=2)


def load_documents(path="documents.json"):
    """
    Recharge les documents dans indexed_documents[]
    """
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            loaded = json.load(f)
            indexed_documents.clear()
            indexed_documents.extend(loaded)


