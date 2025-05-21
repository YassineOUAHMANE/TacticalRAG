def build_prompt(question: str, context: list[str]) -> str:
    context_text = "\n".join(context)
    return f"Contexte:\n{context_text}\n\nQuestion: {question}\nRéponse:"
