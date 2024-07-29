import os
import openai

# Set the API key in the environment variable
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
openai.api_key = os.environ["OPENAI_API_KEY"]

def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1000,
        temperature=0.7,
    )
    generated_text = response["choices"][0]["message"]["content"]
    return generated_text.strip()

prompt = "Write a haiku about a sunset."
generated_text = generate_text(prompt)
print(generated_text)
