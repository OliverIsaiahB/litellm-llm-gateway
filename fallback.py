"""one_gateway — step 5: when a provider falls over, fail over."""
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

# Try gpt-5 first. If the call still fails after its retries, LiteLLM
# replays the SAME request against each fallback model, in order.
response = completion(
    model="gpt-5",
    messages=[{"role": "user", "content": "What is a single point of failure?"}],
    num_retries=1,
    fallbacks=["anthropic/claude-sonnet-5"],
)

# Whoever answered, the shape is identical — check who it actually was:
print("answered by:", response.model)
print(response.choices[0].message.content)
