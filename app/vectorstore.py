from sentence_transformers import SentenceTransformer
import faiss
import os
import pickle

class VectorStore:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = faiss.IndexFlatL2(384)  # 384 is the dimension of MiniLM
        self.documents = []  # To keep track of texts

    def build_index(self, docs_folder):
        texts = []
        for filename in os.listdir(docs_folder):
            with open(os.path.join(docs_folder, filename), "r", encoding="utf-8") as f:
                texts.append(f.read())

        embeddings = self.model.encode(texts)
        self.index.add(embeddings)
        self.documents = texts
        # Save index and docs for reuse
        faiss.write_index(self.index, "vector.index")
        with open("documents.pkl", "wb") as f:
            pickle.dump(self.documents, f)

    def load_index(self):
        self.index = faiss.read_index("vector.index")
        with open("documents.pkl", "rb") as f:
            self.documents = pickle.load(f)

    def query(self, question, k=3):
        q_emb = self.model.encode([question])
        distances, indices = self.index.search(q_emb, k)
        results = [self.documents[i] for i in indices[0]]
        return results
