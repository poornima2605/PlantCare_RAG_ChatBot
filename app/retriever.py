from vectorstore import VectorStore

# Initialize VectorStore
vs = VectorStore()
vs.load_index()

def retrieve_context(question: str, k: int = 3):
    """
    Retrieve top k documents from the vector store based on the question.
    
    Args:
        question (str): User's question.
        k (int): Number of documents to retrieve.

    Returns:
        List[str]: List of relevant documents/snippets.
    """
    retrieved_docs = vs.query(question, k=k)
    return retrieved_docs
