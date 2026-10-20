from langchain_community.document_loaders import DirectoryLoader, TextLoader
from logger import log_step

@log_step
def load_documents():
    loader = DirectoryLoader(
        "knowledge_base",
        glob = "*.md",
        loader_cls = TextLoader,
        loader_kwargs = {"encoding": "utf-8"}
    )
    documents = loader.load()
    return documents