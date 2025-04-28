from fastapi import FastAPI
from pydantic import BaseModel
from app.retriever import retrieve_context 
from app.generator import generate_answer


app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    retrieved_docs = retrieve_context(request.question)
    answer = generate_answer(retrieved_docs, request.question)
    return {"answer": answer}
