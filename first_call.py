"""one_gateway — step 1: your first call through LiteLLM."""
from dotenv import load_dotenv
from litellm import completion

load_dotenv()  # pulls OPENAI_API_KEY / ANTHROPIC_API_KEY out of .env

response = completion(
    model="gpt-5",
    messages=[
        {"role": "user", "content": "In one sentence, what is an LLM gateway?"},
    ],
)

print(response.choices[0].message.content)
