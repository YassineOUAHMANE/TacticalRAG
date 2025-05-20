from fastapi import APIRouter
from pydantic import BaseModel
from vector_store.vector_utils import search_similar
from ..rag.generator import generate_answer  # à implémenter si pas encore
from typing import List

router = APIRouter()

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str
    context: List[str]
@router.get("/")
def read_root():
    return {"message": "Football RAG Backend is running"}

@router.post("/ask", response_model=AskResponse)
def ask_question(payload: AskRequest):
    # Étape 1 : rechercher les documents similaires
    context_docs = search_similar(payload.question)

    # Étape 2 : générer la réponse avec le contexte
    context_text = "\n".join(context_docs)
    answer = generate_answer(context_text, payload.question)

    return AskResponse(answer=answer, context=context_docs)




'''@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    texts = parse_file(content, file.filename)
    embeddings = embed(texts)
    index(embeddings)
    return {"status": "success"}

@router.get("/stats", response_model=Stats)
async def stats():
    return get_stats()'''
