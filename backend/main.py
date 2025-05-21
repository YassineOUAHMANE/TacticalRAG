from fastapi import FastAPI
from .api.routes import router
from vector_store.vector_utils import initialize_vector_store
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")  
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["*"] for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("✅ Middleware CORS activé")
app = FastAPI(title="Football RAG API")
app.include_router(router)


initialize_vector_store()
