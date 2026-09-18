import chromadb
from sentence_transformers import SentenceTransformer
from app.core.config import settings

client = None
collection = None
embedding_model = None

def load_retrieval():
    global client, collection, embedding_model
    embedding_model = SentenceTransformer(settings.EMBEDDING_MODEL)
    client = chromadb.PersistentClient(path=settings.VECTOR_STORE_PATH)
    collection = client.get_collection(name=settings.COLLECTION_NAME)
    print(f"✅ Loaded collection with {collection.count()} chunks")

def retrieve(query: str, n_results: int = 3):
    query_embedding = embedding_model.encode([query]).tolist()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )
    chunks = []
    for i in range(len(results["documents"][0])):
        chunks.append({
            "text": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"]
        })
    return chunks