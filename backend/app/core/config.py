from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OLLAMA_MODEL: str = "llama3.2"
    COLLECTION_NAME: str = "ml_documents"
    VECTOR_STORE_PATH: str = "data/vector_store"
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    
    class Config:
        env_file = ".env"

settings = Settings()