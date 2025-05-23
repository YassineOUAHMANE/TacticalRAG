from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def generate_answer(context: str, question: str) -> str:
    print("🟢 Received question:", question)
    prompt = f"""Context:
{context}

Question:
{question}

Answer:"""

    response = client.chat.completions.create(
        model="tinyllama",  # "changer le model au tinyllama"
        messages=[
            {"role": "system", "content": "You are a helpful assistant who answers based only on the context."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()

