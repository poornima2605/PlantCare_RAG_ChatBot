from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.retriever import retrieve_context 
from app.generator import generate_answer

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Optional CORS settings (for frontend access, if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    retrieved_docs = retrieve_context(request.question)
    answer = generate_answer(retrieved_docs, request.question)
    return {"answer": answer}


# --- GUI Web Form ---

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "answer": None})

@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, question: str = Form(...)):
    retrieved_docs = retrieve_context(question)
    answer = generate_answer(retrieved_docs, question)
    return templates.TemplateResponse("index.html", {"request": request, "answer": answer})
