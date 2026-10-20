# AskMe

A retrieval-augmented generation (RAG) assistant that answers questions about me (Atchaya Rajalingam), built for my portfolio website. Recruiters and visitors can ask about my experience, projects and skills in plain language and get answers grounded in a knowledge base I wrote, instead of reading a static resume.

It is a personal project, written in Python with LangChain, ChromaDB and Groq.

## How it works

```
knowledge_base/*.md
      |
      v
  loader.py      loads the markdown files
      |
      v
  chunking.py    splits by markdown headers, then by size
      |
      v
  embeddings.py  embeds each chunk and stores it in ChromaDB
      |
      v
  question --> similarity search (top 4 chunks) --> prompt --> LLM --> answer
                                                    llm.py
```

1. **Load:** every `.md` file in `knowledge_base/` is read.
2. **Chunk:** each file is split at `#` and `##` headers so a project or FAQ answer stays together with its heading. Sections that are still too long are split again by size.
3. **Embed and store:** each chunk is converted to a vector with a local Hugging Face model and stored in ChromaDB.
4. **Retrieve:** a question is embedded the same way, and the four closest chunks are retrieved.
5. **Generate:** the chunks and the question are passed to an LLM with a system prompt that restricts it to the retrieved facts.

## Design decisions

| Decision | Reason |
|---|---|
| RAG instead of fine-tuning | The knowledge base changes whenever I update a project or role. Editing a markdown file is enough, with no retraining. |
| Header-aware chunking, then size-based splitting | A plain size-based split separated FAQ questions from their answers and project details from their headings. Splitting on headers first fixed this. |
| One FAQ question per `##` heading | Each answer becomes its own chunk, so retrieval returns one focused answer instead of several mixed ones. |
| Local embeddings (`sentence-transformers/all-MiniLM-L6-v2`) | Free, runs on a laptop, and needs no external API. |
| Strict system prompt | The assistant answers only from retrieved facts, declines out-of-scope questions (such as salary), stays on topic, and ignores instructions to change its rules. |
| Logging decorator (`logger.py`) | Records each step so retrieval and answers can be inspected when something looks wrong. |

## Tech stack

- Python
- LangChain (`langchain`, `langchain-community`, `langchain-text-splitters`)
- ChromaDB as the vector store (`langchain-chroma`)
- Hugging Face `sentence-transformers` for embeddings (`langchain-huggingface`)
- Groq API for generation (`langchain-groq`), model `openai/gpt-oss-120b`
- `python-dotenv` for configuration

## Project structure

```
AskMe/
├── knowledge_base/   markdown files the assistant answers from
├── loader.py         loads the documents
├── chunking.py       splits documents into chunks
├── embeddings.py     builds the ChromaDB vector store
├── llm.py            prompt and LLM call
├── logger.py         logging helper
├── rag.py            entry point (command-line chat)
├── requirements.txt
└── .env.example
```

## Setup

You need Python 3 and a free [Groq](https://console.groq.com) API key.

```bash
git clone https://github.com/atchayarajalingam28/AskMe.git
cd AskMe

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file in the project folder (see `.env.example`):

```
GROQ_API_KEY=your_key_here
```

Run it:

```bash
python rag.py
```

The first run downloads the embedding model (roughly 90 MB), so it takes a little longer. Type a question at the prompt, or `quit` to exit.

If Groq reports that the model is not found, model availability changes over time. List the models your key can use and set a valid name in `llm.py`.

## Example questions

- "What are Atchaya's strongest projects?"
- "What did she build on project X?"
- "Does she know Python?"

Questions the knowledge base does not cover (salary, personal details, unrelated topics) are declined, and the assistant points to her contact email instead of guessing.

## Current limitations

- The assistant only knows what is in `knowledge_base/`. Anything missing from those files, it cannot answer.
- Retrieval always returns a fixed number of chunks, even when fewer are relevant.
- Changing a document means re-indexing the knowledge base. There is no incremental update or version history yet.
- There is no automated evaluation yet, only manual testing of sample and adversarial questions.

## Roadmap

- [ ] Incremental indexing with stable chunk IDs, so only changed content is re-embedded
- [ ] A small evaluation set of questions with expected behaviour, including prompt-injection attempts
- [ ] FastAPI backend wrapping the pipeline
- [ ] Chat widget on my portfolio website

## Contact

Atchaya Rajalingam, Applied AI Engineer
Email: atchayaraja2811@gmail.com
LinkedIn: [linkedin.com/in/atchaya-r](https://www.linkedin.com/in/atchaya-r/)