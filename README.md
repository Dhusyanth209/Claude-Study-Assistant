# 📚 Claude Study Assistant (Local Ollama)

An **interactive, terminal-based study tutor** powered by a locally-running **Llama 3.2** model via [Ollama](https://ollama.com). No paid API keys — everything runs on your machine.

## ✨ Features

- **Interactive loop** — stays open until you type `/quit`
- **Conversation memory** — the tutor remembers context across messages
- **Slash commands** — structured study modes (explain, quiz, summarize, simplify)
- **Free-form questions** — just type anything without a command
- **Startup health check** — friendly error if Ollama isn't running
- **No API key required** — 100 % local inference

## Prerequisites

- **Python 3.9+**
- **Ollama** installed and running ([download here](https://ollama.com/download))
- **llama3.2** model pulled: `ollama pull llama3.2`

## Setup

```bash
# 1. Clone the repo
git clone https://github.com/Dhusyanth209/Claude-Study-Assistant.git
cd Claude-Study-Assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Make sure Ollama is serving (open a separate terminal if needed)
ollama serve

# 4. Run the assistant
python app.py
```

## Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/explain <topic>` | Step-by-step explanation with real-world examples | `/explain mitosis` |
| `/quiz <topic>` | 5 multiple-choice questions with answer key at the end | `/quiz Newton's laws` |
| `/summarize <text>` | Bullet-point revision summary | `/summarize <paste your notes>` |
| `/simplify <topic>` | Explain like I'm 10 years old, with an analogy | `/simplify quantum entanglement` |
| `/clear` | Wipe conversation history and start fresh | `/clear` |
| `/quit` | Exit the app | `/quit` |

> **Tip:** You can also just type any question directly without a slash command!

## Example Session

```
╔══════════════════════════════════════════════════════════════╗
║               📚  STUDY ASSISTANT  (Ollama)                 ║
║                  Powered by Llama 3.2                       ║
╠══════════════════════════════════════════════════════════════╣
║  Commands:                                                  ║
║    /explain  <topic>   Step-by-step explanation + examples   ║
║    /quiz     <topic>   5 MCQs with answer key                ║
║    /summarize <text>   Bullet-point revision summary         ║
║    /simplify <topic>   Explain like I'm 10                   ║
║    /clear              Wipe conversation history             ║
║    /quit               Exit the app                          ║
║                                                              ║
║  Or just type any study question directly!                   ║
╚══════════════════════════════════════════════════════════════╝

🎓 You: /explain photosynthesis

🤖 Tutor: **Photosynthesis — Step by Step**
1. Light Absorption ...
2. Water Splitting ...
...

🎓 You: /quiz photosynthesis

🤖 Tutor: **Quiz: Photosynthesis**
Q1. What is the primary pigment ...
   A) ...  B) ...  C) ...  D) ...
...
ANSWER KEY:
1. C — Chlorophyll absorbs ...

🎓 You: What is the difference between mitosis and meiosis?

🤖 Tutor: Great question! Mitosis produces two identical ...

🎓 You: /quit

Goodbye — happy studying! 👋
```

## Project Structure

```
├── app.py              # Interactive study assistant
├── requirements.txt    # Python dependencies (ollama)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## License

This project is for educational purposes.
