"""one_gateway — step 3: stream the reply chunk-by-chunk."""
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

stream = completion(
    model="gpt-5",
    messages=[{"role": "user", "content": "Explain streaming to a five-year-old."}],
    stream=True,
)

# Each chunk carries a small delta — often a word or part of one.
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:  # some chunks (role headers, the final chunk) carry no text
        print(delta, end="", flush=True)

print()  # finish the line once the stream ends
