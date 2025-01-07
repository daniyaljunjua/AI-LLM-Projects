from groq import Groq

def analyze_text(input_text, question):
    client = Groq()
    instruction = (
        "Please answer the following question briefly based on the provided text. "
        "Avoid any information not present in the provided text. "
        "If the question is irrelevant, indicate it is out of context."
    )
    try:
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": f"{input_text}\n\n{question}"}
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True
        )
        answer = "".join(chunk.choices[0].delta.content or "" for chunk in completion)
        return answer
    except Exception as e:
        return f"Error during analysis: {e}"
