from pydantic import BaseModel

class Question(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str

class Stats(BaseModel):
    documents_indexed: int
    total_tokens: int
