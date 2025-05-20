from fastapi import FastAPI
from .api.routes import router
from vector_store.vector_utils import initialize_vector_store
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")  




app = FastAPI()


app = FastAPI(title="Football RAG API")
app.include_router(router)


initialize_vector_store()
