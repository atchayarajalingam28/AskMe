from langchain_community.document_loaders import DirectoryLoader, TextLoader

def load_documents():
    loader = DirectoryLoader(
        "knowledge_base",
        glob = "*.md",
        loader_cls = TextLoader,
        loader_kwargs = {"encoding": "utf-8"}
    )
    documents = loader.load()
    print(f"Loaded {len(documents)} documents from knowledge_base directory.")
    return documents