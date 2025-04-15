#!/bin/bash

# Print header
echo "============================================="
echo "Setting up HelpGPT Chatbot RAG Environment"
echo "============================================="

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirement.txt

# Make script executable
chmod +x install.sh

echo "============================================="
echo "Installation complete!"
echo "To start the app:"
echo "1. Make sure Ollama is running locally"
echo "2. Run: source venv/bin/activate"
echo "3. Run: streamlit run Chat_RAG_final.py"
echo "=============================================" 