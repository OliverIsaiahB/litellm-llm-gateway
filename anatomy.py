"""one_gateway — step 3: what actually comes back."""
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

response = completion(
    model="anthropic/claude-sonnet-5",
    messages=[{"role": "user", "content": "Say hello in exactly three words."}],
)

# The reply text lives on the first choice.
choice = response.choices[0]
print("content:      ", choice.message.content)
print("role:         ", choice.message.role)   # always "assistant"
print("finish_reason:", choice.finish_reason)  # "stop", "length", ...

# Token accounting comes back normalized, whatever the provider.
print("prompt tokens:    ", response.usage.prompt_tokens)
print("completion tokens:", response.usage.completion_tokens)
print("total tokens:     ", response.usage.total_tokens)

# The model field echoes which backend actually answered.
print("model:", response.model)
