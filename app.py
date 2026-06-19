import sys
import ollama


SYSTEM_PROMPT = (
    "You are a friendly and patient study tutor for students. "
    "You explain concepts clearly using simple language, real-world examples, "
    "and analogies. When asked to quiz, you create well-structured multiple-choice "
    "questions. When asked to summarize, you produce concise bullet-point revision "
    "notes. Always encourage the student and check if they need further clarification."
)

COMMAND_PROMPTS = {
    "/explain": (
        "Give a detailed, step-by-step explanation of the following topic. "
        "Include at least two real-world examples and break complex ideas into "
        "simple parts:\n\n{}"
    ),
    "/quiz": (
        "Create exactly 5 multiple-choice questions (A–D) on the following topic. "
        "Print all questions first WITHOUT revealing the answers, then after all "
        "5 questions print a clearly separated ANSWER KEY with brief explanations "
        "for each correct answer:\n\n{}"
    ),
    "/summarize": (
        "Summarize the following text into concise bullet-point revision notes "
        "suitable for quick review before an exam. Group related points under "
        "sub-headings where appropriate:\n\n{}"
    ),
    "/simplify": (
        "Explain the following topic as if I were a 10-year-old child. Use a fun "
        "analogy, everyday language, and avoid jargon entirely:\n\n{}"
    ),
}

BANNER = r"""
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
"""

MODEL = "llama3.2"


def check_ollama():
    """Verify Ollama is reachable before entering the main loop."""
    try:
        ollama.list()
    except Exception:
        print(
            "\n❌  Could not connect to Ollama.\n"
            "    Make sure it is installed and running:\n"
            "      • Start it with:  ollama serve\n"
            "      • Download from:  https://ollama.com/download\n"
        )
        sys.exit(1)


def ask(history: list[dict]) -> str:
    """Send the full conversation history to Ollama and return the response."""
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
    )
    return response["message"]["content"]


def parse_input(user_input: str) -> tuple[str | None, str]:
    """Return (command, argument_text).  command is None for free questions."""
    stripped = user_input.strip()
    if not stripped:
        return None, ""

    parts = stripped.split(maxsplit=1)
    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ""

    if cmd in COMMAND_PROMPTS:
        return cmd, arg
    if cmd in ("/clear", "/quit"):
        return cmd, ""
    # Not a recognised command → treat the whole input as a free question
    return None, stripped


def main():
    check_ollama()
    print(BANNER)

    history: list[dict] = []

    while True:
        try:
            user_input = input("\n🎓 You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nGoodbye — happy studying! 👋")
            break

        if not user_input:
            continue

        command, argument = parse_input(user_input)

        # --- built-in actions ------------------------------------------------
        if command == "/quit":
            print("\nGoodbye — happy studying! 👋")
            break

        if command == "/clear":
            history.clear()
            print("\n🧹  Conversation history cleared. Fresh start!")
            continue

        # --- commands that need an argument -----------------------------------
        if command in COMMAND_PROMPTS:
            if not argument:
                print(f"\n⚠️  Usage: {command} <topic or text>")
                continue
            message_text = COMMAND_PROMPTS[command].format(argument)
        else:
            # Free-form study question
            message_text = argument if argument else user_input

        # --- send to model ----------------------------------------------------
        history.append({"role": "user", "content": message_text})

        print("\n🤖 Tutor: ", end="", flush=True)
        try:
            answer = ask(history)
        except Exception as e:
            print(f"\n❌  Error talking to Ollama: {e}")
            history.pop()  # remove the failed message so history stays clean
            continue

        print(answer)
        history.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    main()
