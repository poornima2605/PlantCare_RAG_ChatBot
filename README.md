# 🌿 PlantCare RAG ChatBot

A lightweight, intelligent chatbot that answers user queries about plant care using Retrieval-Augmented Generation (RAG). Built with **FastAPI**, **OpenAI**, and enhanced with **dynamic image search** to show relevant plant visuals alongside answers.

---

## Features

- Semantic search-based context retrieval (RAG)
- Natural language answer generation using OpenAI GPT
- Image search integration using Unsplash API
- Web-based interface with FastAPI + Jinja2 templates
- CI/CD with Docker & GitHub Actions
- Kubernetes deployment via AWS EKS (Elastic Kubernetes Service)

---

## Image Search Support

The chatbot now enriches responses with **relevant plant images**, fetched dynamically using the [Unsplash API](https://unsplash.com/developers).

> Example:  
> **Question**: _"How much water does a rose plant need?"_  
> **Answer**: _"Rose plants typically need deep watering twice a week..."_  
> **Image**: A real-time photo of a rose plant is shown below the answer.

---

## Tech Stack

- **Backend**: FastAPI
- **LLM Integration**: OpenAI API
- **Context Retrieval**: Custom semantic retriever
- **Frontend**: HTML (Jinja2 templating)
- **Image API**: Unsplash
- **CI/CD**: GitHub Actions + Docker
- **Deployment**: Kubernetes (AWS EKS)

---

## System Architecture


**Components:**
- User sends a question via frontend or API.
- FastAPI handles the request and passes it to the retriever.
- Retriever uses Sentence-BERT to embed the query.
- VectorStore retrieves relevant documents.
- Retrieved context is passed to the LLM for answer generation.

---

## CI/CD & DevOps Workflow

### Dockerized App

- Docker image builds using `Dockerfile`
- Optimized for lightweight deployment

### GitHub Actions

Automated pipeline includes:

- Linting & tests
- Docker image build
- Push to DockerHub or ECR
- Kubernetes deployment

### Kubernetes on EKS

- YAML manifests for Deployments & Services
- Helm chart support (optional)
- Secrets, ConfigMaps & autoscaling in production

---

## Request Flow

1. User submits a plant care question.
2. Question is embedded using Sentence-BERT.
3. Vector search finds relevant context and image using unsplash API.
4. Context + question are passed to the language model.
5. Response is returned via the FastAPI endpoint.
6. Image search search result is displayed.

---

## Project Structure

     
    ├── PlantCare_RAG_ChatBot/
    ├── app/                   # FastAPI app and route definitions
    │   ├── retriever.py       # Logic for retrieving relevant plant care info via vector search
    │   ├── vectorstore.py     # Code for embedding documents and managing the FAISS vector store
    │   ├── documents/         # Folder containing raw plant care text documents (.txt files)
    │   └── utils/             # Additional helper files
    ├── Dockerfile             # Instructions to build and run the container
    ├── requirements.txt       # List of Python packages required for the project
    ├── README.md              # Project documentation


---

## Setup & Installation

### Prerequisites:

1. Python 3.9+
2. Docker
3. OpenAI API Key​
4. Unsplash API key
5. EKS clous credentials and setup knowledge (Optional)


### Steps Locally to run app:

#### Step 1: Clone the Repository:

git clone https://github.com/poornima2605/plantcare-rag-chatbot.git
cd plantcare-rag-chatbot

#### Step 2: Set Up Environment Variables:

Create a .env file in the root directory and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key

#### Step 3: Build the Docker image

docker build -t plant-bot .

#### Step 4: Run the container

docker run -p 8000:8000 plant-bot

---

## Usage

Once the application is running, navigate to http://localhost:8000 in your browser. Enter your plant care questions, and the chatbot will provide informed responses based on the integrated knowledge base. Below is an example how the GUI in web browser looks like:

![input prompt](https://github.com/poornima2605/PlantCare_RAG_ChatBot/blob/main/images/InputPrompt.png)

![output](https://github.com/poornima2605/PlantCare_RAG_ChatBot/blob/main/images/Output.png?raw=true)


### API Usage Example

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

## Tech Stack

1. **FastAPI**: Web framework for building APIs
2. **Uvicorn**: ASGI server FastAPI server
3. **Sentence-Transformers**: all-MiniLM-L6-v2 for semantic embeddings
4. **HuggingFace Transformers**
5. **Docker**: Containerized deployment

---

## Customizing the Knowledge Base

1. Add your .txt to the app/documents/ directory.
2. Rebuild the vector store by running app/create_index.py "path_to_new_txt".
3. Restart the app to load new embeddings.
