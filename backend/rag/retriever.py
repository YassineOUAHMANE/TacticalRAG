from vector_store.vector_utils import search_similar

def retrieve_context(query: str, k: int = 5):
    return search_similar(query, k)
