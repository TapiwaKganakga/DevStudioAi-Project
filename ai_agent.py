

# Responsible for formatting prompts and calling the LLM.
# Replace OpenAI call with your provider as needed.

import os
import json

try:
    import openai
except Exception:
    openai = None

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY and openai:
    openai.api_key = OPENAI_API_KEY


def build_prompt(filename: str, code: str, linter_output: str = "") -> str:
    prompt = f"""You are an expert senior software engineer and reviewer.

Filename: {filename}

Linter output:
{linter_output}


Tasks (be concise):
1. Provide a short summary (1-2 lines) of what the code does.
2. List up to 5 prioritized issues (bugs/security/performance/style), each with a suggested fix.
3. Generate 2-3 pytest unit tests that exercise the main functions in the code. Provide tests only (no explanation).
4. Provide a patch/diff if the fix is small (apply minimal edits).

Return a JSON object with keys: summary, issues, tests, diff (diff is optional).
"""
    return prompt


def call_llm(prompt: str, max_tokens: int = 800) -> dict:
    # If no API key is present, return a mocked response for demo
    if not OPENAI_API_KEY or not openai:
        return {
            "summary": "Mock summary: simple module",
            "issues": [{"issue": "No input validation", "fix": "Add type checks"}],
            "tests": "import pytest\n\nfrom module import func\n\ndef test_func():\n    assert func(2) == 4\n",
            "diff": ""
        }

    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=max_tokens
    )
    text = resp['choices'][0]['message']['content']
    try:
        parsed = json.loads(text)
        return parsed
    except Exception:
        return {"raw": text}
