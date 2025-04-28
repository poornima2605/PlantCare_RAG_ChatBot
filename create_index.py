# Install needed libraries first if not installed:
# pip install faiss-cpu sentence-transformers

import faiss
import pickle
from sentence_transformers import SentenceTransformer
import os

# 1. Load your plant documents
documents = [
    "Tomato plants need 6-8 hours of sunlight daily.",
    "Yellow leaves can mean overwatering.",
    "To treat powdery mildew, spray with neem oil.",
    "Best soil pH for roses is 6.0 to 6.5.",
    "Aphids can be removed with a strong water spray."
]

# 2. Load an embedding model (small but good one)
model = SentenceTransformer('all-MiniLM-L6-v2')

# 3. Create embeddings
embeddings = model.encode(documents)

# 4. Create FAISS index
dimension = embeddings.shape[1]  # length of embedding vector
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# 5. Save FAISS index
faiss.write_index(index, "vector.index")

# 6. Save documents
with open("documents.pkl", "wb") as f:
    pickle.dump(documents, f)

print("✅ Created vector.index and documents.pkl successfully!")
