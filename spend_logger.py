"""one_gateway — step 6: know what every call costs."""
import json
import time

from dotenv import load_dotenv
import litellm
from litellm import completion, completion_cost

load_dotenv()

LOG_PATH = "spend_log.jsonl"


def logged_ask(model: str, prompt: str) -> str:
    """Call the model, then append one JSON line of spend accounting."""
    response = completion(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    cost_usd = completion_cost(completion_response=response)

    entry = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "model": response.model,
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "cost_usd": round(cost_usd, 6),
    }
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")

    return response.choices[0].message.content


if __name__ == "__main__":
    # LiteLLM ships a cost map: per-token prices for thousands of models.
    pricing = litellm.model_cost["gpt-5"]
    print("input  $/token:", pricing["input_cost_per_token"])
    print("output $/token:", pricing["output_cost_per_token"])

    print(logged_ask("gpt-5", "Define 'unit economics' in one sentence."))
    print(logged_ask("anthropic/claude-sonnet-5", "Same question — second opinion?"))
