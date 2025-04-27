from fastapi import FastAPI
from pydantic import BaseModel
from vectorstore import VectorStore
from generator import generate_answer

app = FastAPI()

# Load vector store
vs = VectorStore()
vs.load_index()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    retrieved_docs = vs.query(request.question)
    answer = generate_answer(retrieved_docs, request.question)
    return {"answer": answer}
