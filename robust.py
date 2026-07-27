"""one_gateway — step 4: survive a bad day at the provider."""
from dotenv import load_dotenv
import litellm
from litellm import completion

load_dotenv()


def ask(model: str, prompt: str) -> str:
    """One call with retries, a timeout, and honest error handling."""
    try:
        response = completion(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            num_retries=2,  # retry transient failures (rate limits, network blips)
            timeout=30,     # seconds before we give up on a hung request
        )
        return response.choices[0].message.content
    except litellm.RateLimitError:
        return "[busy] The provider is rate-limiting us — try again shortly."
    except litellm.AuthenticationError:
        return "[config] API key missing or wrong — check your .env file."
    except litellm.APIConnectionError:
        return "[down] Could not reach the provider at all."


if __name__ == "__main__":
    print(ask("gpt-5", "Why do networks fail? Answer in one sentence."))
