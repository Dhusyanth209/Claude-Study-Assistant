import ollama


def study_assistant(question: str) -> str:
    """Send question to local Ollama (Llama 3.2), get study explanation back."""
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": (
                    "I'm a student learning. "
                    "Please explain this clearly and simply: "
                    f"{question}"
                ),
            }
        ],
    )

    return response["message"]["content"]


if __name__ == "__main__":
    # Test the function
    question = "What is photosynthesis?"
    answer = study_assistant(question)
    print(f"Question: {question}")
    print(f"\nAnswer:\n{answer}")
