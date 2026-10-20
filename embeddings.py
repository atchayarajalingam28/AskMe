import os
import shutil
from logger import log_step
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


CHROMA_DIR = "chroma_db"

#Start fresh each run so re-running doesn't store duplicate chunks
#Remove this when implementing versioning
@log_step
def vector_store_rerun():
    if os.path.exists(CHROMA_DIR):
        shutil.rmtree(CHROMA_DIR)

@log_step
def build_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vector_store = Chroma.from_documents(
        documents = chunks,
        embedding = embeddings,
        persist_directory = CHROMA_DIR,
    )
    return vector_store