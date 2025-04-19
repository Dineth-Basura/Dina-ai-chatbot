import requests

DEEPSEEK_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxx"  # your OpenRouter key

def ask_deepseek(message):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mistral-7b-instruct",  # fixed valid model ID
        "messages": [
            {"role": "user", "content": message}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    
    try:
        result = response.json()
        print("→ OpenRouter raw response:", result)

        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        else:
            error_message = result.get("error", {}).get("message", "Unknown error")
            return f"OpenRouter error: {error_message}"
    except Exception as e:
        print("→ OpenRouter parsing error:", e)
        return "Sorry, something went wrong with OpenRouter."