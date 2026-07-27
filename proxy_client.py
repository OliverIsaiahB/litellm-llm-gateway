"""one_gateway — step 8: call the gateway with a scoped virtual key."""
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:4000",
    api_key="sk-...paste-a-generated-virtual-key...",  # NOT the master key
)

response = client.chat.completions.create(
    model="fast",
    messages=[{"role": "user", "content": "Who is answering this request?"}],
)

print(response.choices[0].message.content)
