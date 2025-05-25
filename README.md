# LoTR_RAG: Lord of the Rings Retrieval-Augmented Generation

A Retrieval-Augmented Generation (RAG) project powered by a custom dataset derived from J.R.R. Tolkien's works, enabling semantic search and answer generation for a Tolkien-inspired chatbot.

## Overview

LoTR_RAG leverages a rich dataset of Tolkien's literature to create a chatbot capable of answering queries with context-aware, lore-accurate responses. The system parses, chunks, embeds, and stores text from various Tolkien works in a vector store for efficient retrieval and generation.

## Project Structure

- `app/` — Core application code for the RAG system.
- `Confg/` — Configuration files for environment settings.
- `Notebook/` — Jupyter notebooks for experiments and analysis.
- `Rag/` — Modules specific to the RAG pipeline.

## Source Texts

The RAG system is built on a custom dataset created from the following J.R.R. Tolkien works (EPUB format):

- *The Hobbit* (Enhanced and Standard Editions)
- *The Lord of the Rings* trilogy
- *The Silmarillion*
- *The Children of Húrin*
- *Unfinished Tales*
- *The Book of Lost Tales* (Parts 1 & 2)
- *Tales from the Perilous Realm*
- *The Legend of Sigurd and Gudrun*
- *The Return of the Shadow*
- *Bilbo's Last Song* (source)
- And additional Tolkien works.

These texts are parsed, chunked, embedded, and stored in a vector store to support semantic search and answer generation.

## Setup

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd LoTR_RAG
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**

   - Copy `.env.example` to `.env`:

     ```bash
     cp .env.example .env
     ```

   - Update `.env` with your specific configurations (e.g., vector store credentials, API keys).

## Usage

### ▶️ Run the API Server

Start the FastAPI server to access the chatbot's endpoints:

```bash
python app/main.py
```

The server will run at `http://localhost:8000`. Visit `http://localhost:8000/docs` for interactive API documentation.

### 💬 Launch the Streamlit Chat UI

Launch the interactive chat interface:

```bash
streamlit run ui/main.py
```

A browser window will open with a user-friendly interface to interact with the Tolkien-inspired chatbot.

### 📓 Run Notebooks

Open and run Jupyter notebooks in the `Notebook/` directory for experimentation and analysis:

```bash
jupyter notebook Notebook/
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

# For major changes, please open an issue first to discuss your proposed changes.

## License

This project is licensed under the MIT License.

### Acknowledgments

1. Powered by Rich for enhanced terminal output.
2. Built with love for J.R.R. Tolkien's legendary works.