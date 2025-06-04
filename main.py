import streamlit as st
from utils.pdf_processor import extract_text_from_pdf, chunk_text
from utils.embedding_handler import EmbeddingHandler
from utils.rag_helper import RAGHelper
import os
from datetime import datetime

# Initialize components
@st.cache_resource
def initialize_components():
    pdf_path = "data/brain.pdf"
    index_path = "embeddings/faiss_index/index.faiss"
    embeddings_path = "embeddings/embeddings.pkl"
    
    handler = EmbeddingHandler()
    
    if os.path.exists(index_path) and os.path.exists(embeddings_path):
        handler.load_index(index_path, embeddings_path)
    else:
        pages = extract_text_from_pdf(pdf_path)
        chunks = chunk_text(pages)
        embeddings = handler.create_embeddings(chunks)
        handler.build_faiss_index(embeddings)
        os.makedirs(os.path.dirname(index_path), exist_ok=True)
        handler.save_index(index_path, embeddings_path)
    
    return handler

def main():
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.title("🧠 Neuroscience Chat Assistant")
    
    # Initialize components
    handler = initialize_components()
    rag = RAGHelper()

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            st.caption(message["time"])

    # Accept user input
    if prompt := st.chat_input("Ask about the human brain..."):
        # Add user message to chat history
        current_time = datetime.now().strftime("%H:%M")
        st.session_state.messages.append({
            "role": "user", 
            "content": prompt,
            "time": current_time
        })
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
            st.caption(current_time)

        # Get bot response
        with st.spinner("Thinking..."):
            context_chunks = handler.search(prompt, k=3)
            context = "\n\n".join(context_chunks)
            response = rag.generate_response(prompt, context)
            
            # Add bot response to chat history
            current_time = datetime.now().strftime("%H:%M")
            st.session_state.messages.append({
                "role": "assistant",
                "content": response,
                "time": current_time
            })

        # Display bot response
        with st.chat_message("assistant"):
            st.markdown(response)
            st.caption(current_time)

if __name__ == "__main__":
    main()