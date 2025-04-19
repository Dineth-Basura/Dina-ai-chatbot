import json
import random
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open("intents.json") as f:
    data = json.load(f)

# Prepare training data
texts = []
labels = []
tags = []

for intent in data["intents"]:
    tag = intent["tag"]
    tags.append(tag)
    for pattern in intent["patterns"]:
        texts.append(pattern.lower().replace("*", "").strip())
        labels.append(tag)

# Vectorize text
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# Save model and vectorizer
with open("utils/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("utils/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Bot trained and saved!")