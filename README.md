# 🌿 PlantCare RAG ChatBot

The **PlantCare RAG ChatBot** is an AI-powered assistant built using Retrieval-Augmented Generation (RAG) that provides helpful information and personalized advice on plant care. Whether you're a seasoned gardener or a houseplant newbie, this chatbot leverages natural language processing to answer your questions based on custom plant care documents and models.

---

## 🚀 Features

- 🌱 **Plant care Q&A**: Ask questions about watering, light, soil, and more.
- 🔎 **Retrieval-Augmented Generation (RAG)**: Combines vector search with LLMs to provide accurate and grounded answers.
- 🧠 **Sentence-BERT embeddings**: For high-quality semantic search using the `all-MiniLM-L6-v2` model.
- 📁 **Custom document support**: Easily extend knowledge base with your own plant care files.
- ⚡ **FastAPI + Uvicorn backend**: Lightweight and production-ready API.

---

## 🧩 System Architecture


**Components:**
- User sends a question via frontend or API.
- FastAPI handles the request and passes it to the retriever.
- Retriever uses Sentence-BERT to embed the query.
- VectorStore retrieves relevant documents.
- Retrieved context is passed to the LLM for answer generation.

---

## 🔄 Request Flow

1. User submits a plant care question.
2. Question is embedded using Sentence-BERT.
3. Vector search finds relevant context.
4. Context + question are passed to the language model.
5. Response is returned via the FastAPI endpoint.

---

## 🏗️ Project Structure

     .
    ├── PlantCare_RAG_ChatBot/
    ├── app/                   # FastAPI app and route definitions
    │   ├── retriever.py       # Logic for retrieving relevant plant care info via vector search
    │   ├── vectorstore.py     # Code for embedding documents and managing the FAISS vector store
    │   └── documents/         # Folder containing raw plant care text documents (.txt files)
    ├── Dockerfile             # Instructions to build and run the container
    ├── requirements.txt       # List of Python packages required for the project
    ├── README.md              # Project documentation



---

## 🛠️ Setup & Installation

### Prerequisites:

1. Python 3.9+
2. Docker
3. OpenAI API Key​


### Steps:

#### Step 1: Clone the Repository:

git clone https://github.com/yourusername/plantcare-rag-chatbot.git
cd plantcare-rag-chatbot

#### Step 2: Set Up Environment Variables:

Create a .env file in the root directory and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key

#### Step 3: Build the Docker image

docker build -t plant-bot .

#### Step 4: Run the container

docker run -p 8000:8000 plant-bot

---

## 💬 Usage

Once the application is running, navigate to http://localhost:8000/docs in your browser. Enter your plant care questions, and the chatbot will provide informed responses based on the integrated knowledge base.

### 🧪 API Usage Example

Endpoint: /query
Method: POST
Payload:

{
  "question": "How often should I water a snake plant?"
}

Response:

{
  "answer": "Snake plants prefer to dry out completely between waterings. Water once every 2-3 weeks."
}

---

## 🧰 Tech Stack

1. **FastAPI**: Web framework for building APIs
2. **Uvicorn**: ASGI server FastAPI server
3. **Sentence-Transformers**: all-MiniLM-L6-v2 for semantic embeddings
4. **HuggingFace Transformers**
5. **Docker**: Containerized deployment

---

## 📄 Customizing the Knowledge Base

1. Add your .txt to the app/documents/ directory.
2. Rebuild the vector store by running app/create_index.py "path_to_new_txt".
3. Restart the app to load new embeddings.
