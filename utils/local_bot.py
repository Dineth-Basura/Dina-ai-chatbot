import json
import pickle
import random
import os

# Load trained model and vectorizer
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
vectorizer_path = os.path.join(os.path.dirname(__file__), "vectorizer.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

# Load intents
with open("intents.json") as f:
    intents = json.load(f)["intents"]

# Load memory
def load_memory():
    with open("memory.json") as f:
        return json.load(f)

def save_memory(data):
    with open("memory.json", "w") as f:
        json.dump(data, f, indent=2)

# ==== Core AI Reply Function ====
def get_response(user_input):
    memory = load_memory()

    X = vectorizer.transform([user_input.lower()])

    # Confidence check
    probs = model.predict_proba(X)[0]
    confidence = max(probs)
    if confidence < 0.5:
        return "Hmm, I don't know what you mean."

    tag = model.predict(X)[0]

    for intent in intents:
        if intent["tag"] == tag:
            response = random.choice(intent["responses"])

            if "{name}" in response:
                name = memory.get("name", "Unknown")
                return response.replace("{name}", name)

            if tag == "memory_set":
                words = user_input.split()
                possible_name = words[-1]
                memory["name"] = possible_name
                save_memory(memory)
                return response.replace("{name}", possible_name)

            return response

    return "Hmm, I don't know what you mean."