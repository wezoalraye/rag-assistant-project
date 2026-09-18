from fastapi import APIRouter
from app.schemas.query import QueryRequest, QueryResponse
from app.services.retrieval import retrieve
from app.services.generation import generate_answer

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    chunks = retrieve(request.question)
    result = generate_answer(request.question, chunks)
    return QueryResponse(
        answer=result["answer"],
        sources=result["sources"]
    )