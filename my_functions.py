import requests
import os
from dotenv import load_dotenv
load_dotenv('.env')

# Below is a function that has all that mess inside of it, and returns the response as a string. Easy to use, we'll be using that on the other notebooks.
def databricks_llm(chat_history, model_endpoint, verbose=False):
    
    """Call a Databricks serving endpoint that follows the OpenAI chat format."""
    
    DBKS_TOKEN=os.getenv("DATABRICKS_TOKEN")
    DBKS_URL=os.getenv("DATABRICKS_URL")

    if verbose:
        print("\n=== LLM CALL →", model_endpoint, "===")
        for m in chat_history:
            print(f"{m['role'].upper()}: {m['content']}")

    headers = {
        "Authorization": f"Bearer {DBKS_TOKEN}",
        "Content-Type":  "application/json"
    }
    body = {
        "messages":   chat_history,
        "temperature": 0.7,
        "max_tokens":  1000
    }

    resp = requests.post(f"{DBKS_URL}/serving-endpoints/{model_endpoint}/invocations", headers=headers, json=body)
    resp.raise_for_status()
    content = resp.json()["choices"][0]["message"]["content"]

    if verbose: print("LLM RESPONSE:", content[:300] + ("…" if len(content) > 300 else ""))
    if verbose: print("=== LLM CALL END ===")

    del DBKS_TOKEN
    del DBKS_URL

    return content
