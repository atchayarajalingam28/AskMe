from dotenv import load_dotenv
from embeddings import build_vector_store
from llm import answer_question
from loader import load_documents
from chunking import split_documents

#import environment variables from .env file
load_dotenv()

#Main function
if __name__ == "__main__":
    # Load documents from the knowledge_base directory
    documents = load_documents()

    # Split the loaded documents into chunks
    chunks = split_documents(documents)

    # Build the vector store from the chunks
    vector_store = build_vector_store(chunks)

    print("\nAskAtchaya is ready. Type a question, or 'quit' to exit.")
    while True:
        question = input("\nYou: ")
        if question.strip().lower() in ("quit", "exit"):
            break
        print("\nAskAtchaya:", answer_question(vector_store, question))