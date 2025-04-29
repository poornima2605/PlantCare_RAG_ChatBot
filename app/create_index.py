import faiss
import pickle
from sentence_transformers import SentenceTransformer
import os
import sys

def load_documents_from_txt(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"❌ File not found: {filepath}")
    
    with open(filepath, "r", encoding="utf-8") as f:
        documents = [line.strip() for line in f if line.strip()]
    return documents

def main(txt_file_path):
    print(f"📄 Loading documents from {txt_file_path}...")
    documents = load_documents_from_txt(txt_file_path)

    if not documents:
        raise ValueError("❌ No documents found in the file.")

    print(f"📚 Loaded {len(documents)} documents.")

    # Load embedding model
    print("🔍 Loading embedding model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    print("🧠 Encoding documents...")
    embeddings = model.encode(documents)

    # Create FAISS index
    print("📦 Creating FAISS index...")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Save FAISS index
    faiss.write_index(index, "vector.index")
    print("✅ Saved vector.index")

    # Save documents
    with open("documents.pkl", "wb") as f:
        pickle.dump(documents, f)
    print("✅ Saved documents.pkl")

    print("🎉 Indexing complete!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python build_index_from_txt.py <path_to_txt_file>")
    else:
        main(sys.argv[1])
