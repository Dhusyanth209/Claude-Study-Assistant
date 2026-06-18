# Claude Study Assistant (Local Ollama)

A Python-based study assistant that answers student questions using a **locally-running Llama 3.2 model** via [Ollama](https://ollama.com). No paid API key required — everything runs on your machine.

## Prerequisites

- **Python 3.9+**
- **Ollama** installed and running ([download here](https://ollama.com/download))

## Setup

1. **Install Ollama** (if not already installed):
   - **Windows**: Download and run the installer from https://ollama.com/download
   - **macOS**: `brew install ollama` or download from https://ollama.com/download
   - **Linux**: `curl -fsSL https://ollama.com/install.sh | sh`

2. **Pull the Llama 3.2 model**:
   ```bash
   ollama pull llama3.2
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Make sure Ollama is serving** (open a separate terminal if needed):
   ```bash
   ollama serve
   ```

## Usage

```bash
python app.py
```

This will ask a sample question ("What is photosynthesis?") and print the AI-generated answer.

### Customise

Edit `app.py` to change the question or integrate the `study_assistant()` function into your own project:

```python
from app import study_assistant

answer = study_assistant("Explain Newton's third law of motion")
print(answer)
```

## Project Structure

```
├── app.py              # Main application
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## License

This project is for educational purposes.
