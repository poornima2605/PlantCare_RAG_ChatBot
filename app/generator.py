import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(contexts, question):
    context_text = "\n\n".join(contexts)

    prompt = f"""You are an expert plant care assistant.
Given the following plant care information, answer the user's question clearly and concisely.

Information:
{context_text}

User Question:
{question}

Answer:"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful plant care advisor."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
        max_tokens=500,
    )
    return response['choices'][0]['message']['content']
