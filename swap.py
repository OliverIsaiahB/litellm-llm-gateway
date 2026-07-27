"""one_gateway — step 2: same code, different provider."""
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

QUESTION = [{"role": "user", "content": "Name one thing airports and APIs have in common."}]

# OpenAI — LiteLLM recognizes bare OpenAI model names.
openai_reply = completion(model="gpt-5", messages=QUESTION)
print("OpenAI:   ", openai_reply.choices[0].message.content)

# Anthropic — the provider prefix routes the call. Nothing else changes.
anthropic_reply = completion(model="anthropic/claude-sonnet-5", messages=QUESTION)
print("Anthropic:", anthropic_reply.choices[0].message.content)

# A local model through Ollama is one more string swap — same interface:
#   completion(model="ollama/llama3", messages=QUESTION)
