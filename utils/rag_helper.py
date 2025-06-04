from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

class RAGHelper:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    def generate_response(self, query: str, context: str, model: str = "llama-3.3-70b-versatile") -> str:
        """Generate response using Groq API with RAG context"""
        prompt = f"""
        You are a helpful neuroscience assistant. Answer the user's question using only the provided context.
        If the context doesn't contain the answer, say "I don't have information about that in my knowledge base."

        Context:
        {context}

        Question: {query}
        Answer:
        """
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful neuroscience assistant."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=model,
                temperature=0.3
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"An error occurred: {str(e)}"