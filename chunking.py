from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from logger import log_step

@log_step
def split_documents(documents):
    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ],
        strip_headers=False,
    )
    size_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=100,
    )
    chunks = []

    for doc in documents:
        sections = header_splitter.split_text(doc.page_content)
        chunks.extend(size_splitter.split_documents(sections))
    return chunks
            