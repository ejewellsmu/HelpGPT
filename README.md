# HelpGPT

A Streamlit-based chatbot application that uses RAG to train the model on technical documentation for IT support purposes. The application uses Ollama for local LLM inference and ChromaDB for vector storage.

## Quick Start

0. Place PDF training documents in ```Chatbot_RAG/pdf``` or an existing database in ```Chatbot_RAG/docs```.

1. Install dependencies:
```bash
cd Chatbot_RAG
./install.sh
```

2. Start Ollama:
```bash
ollama serve
```

3. Run the app:
```bash
source venv/bin/activate
streamlit run Chat_RAG_final.py
```

## Credits

Original implementation by Tue Vu - AI/ML Research Scientist at SMU
