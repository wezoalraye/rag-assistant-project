import ollama
from app.core.config import settings

def build_prompt(query: str, chunks: list) -> str:
    context = ""
    for i, chunk in enumerate(chunks):
        context += f"[Source {i+1}: {chunk['source']}]\n{chunk['text']}\n\n"
    
    prompt = f"""You are a helpful ML assistant. Answer the question based ONLY on the provided context.
If the answer is not in the context, say "I don't know".
Always mention which source you used.

Context:
{context}

Question: {query}

Answer:"""
    return prompt

def generate_answer(query: str, chunks: list) -> dict:
    prompt = build_prompt(query, chunks)
    
    response = ollama.chat(
        model=settings.OLLAMA_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    
    answer = response["message"]["content"]
    sources = list(set([c["source"] for c in chunks]))
    
    return {"answer": answer, "sources": sources}