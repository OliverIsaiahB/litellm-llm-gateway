# LiteLLM | One API for Every Model

A beginner project built on LiteLLM, the most-starred open-source LLM gateway. You call OpenAI and Anthropic through one completion() interface and swap providers by changing a single string, reading one normalized OpenAI-format response no matter who answered. Then you make the calls production-honest — typed exceptions, automatic retries, timeouts, and fallbacks so a provider outage fails over instead of failing. You meter spend per call with the built-in cost map and a tiny JSONL spend logger. You finish by standing up the LiteLLM proxy server from a config.yaml so a whole team shares one gateway — model aliases, virtual keys, budgets, and rate limits included.

Built step-by-step with [KhwajaLabs Build](https://khwajalabs.com).

## Stack
- Python
- LiteLLM
- OpenAI API
- Anthropic API
- YAML
