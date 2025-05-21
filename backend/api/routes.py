from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from ..rag.generator import generate_answer
from vector_store.vector_utils import search_similar

router = APIRouter()
@router.get("/")
def read_root():
    return {"message": "Football RAG Backend is running"}
# Gestion manuelle de la requête OPTIONS (preflight CORS)
@router.options("/ask")
def preflight_ask():
    return JSONResponse(
        content={},  # pas de contenu nécessaire
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "*"
        }
    )

# Route POST normale
@router.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    question = data.get("question", "")
    print("📥 Question reçue:", question)

    # Simule une réponse pour test
    context_docs = search_similar(question)
    context_text = "\n".join(context_docs)
    response_data = generate_answer(context_text,question)

    return JSONResponse(
        content=response_data,
        headers={
            "Access-Control-Allow-Origin": "*"
        }
    )



"""@router.post("/ask", response_model=AskResponse)
def ask_question(payload: AskRequest):
    # Étape 1 : rechercher les documents similaires
    context_docs = search_similar(payload.question)

    # Étape 2 : générer la réponse avec le contexte
    context_text = "\n".join(context_docs)
    answer = generate_answer(context_text, payload.question)

    return AskResponse(answer=answer, context=context_docs)"""




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
