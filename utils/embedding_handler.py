import os
import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from typing import List

class EmbeddingHandler:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.chunks = None
    
    def create_embeddings(self, chunks: List[str]) -> np.ndarray:
        """Create embeddings for text chunks"""
        self.chunks = chunks
        return self.model.encode(chunks, convert_to_numpy=True)
    
    def build_faiss_index(self, embeddings: np.ndarray):
        """Build and save FAISS index"""
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)
    
    def save_index(self, index_path: str, embeddings_path: str):
        """Save FAISS index and embeddings"""
        if not os.path.exists(os.path.dirname(index_path)):
            os.makedirs(os.path.dirname(index_path))
        
        faiss.write_index(self.index, index_path)
        with open(embeddings_path, 'wb') as f:
            pickle.dump(self.chunks, f)
    
    def load_index(self, index_path: str, embeddings_path: str):
        """Load FAISS index and embeddings"""
        self.index = faiss.read_index(index_path)
        with open(embeddings_path, 'rb') as f:
            self.chunks = pickle.load(f)
        return self.index, self.chunks
    
    def search(self, query: str, k: int = 3) -> List[str]:
        """Search for similar chunks"""
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, k)
        
        results = []
        for idx in indices[0]:
            if idx >= 0:  # -1 indicates no result
                results.append(self.chunks[idx])
        
        return results