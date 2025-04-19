from flask import Flask, render_template, request, jsonify
from utils.local_bot import get_response
from utils.deepseek_api import ask_deepseek  # OpenRouter fallback

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_reply():
    user_input = request.json.get("message")
    
    # 1. Try local response first
    reply = get_response(user_input)

    # 2. If local AI doesn't understand, use OpenRouter
    if "I don't know" in reply or reply.startswith("Hmm"):
        print("→ Using OpenRouter fallback...")
        fallback = ask_deepseek(user_input)

        # 3. If OpenRouter fails, handle it
        if "OpenRouter error" in fallback or "something went wrong" in fallback:
            reply = "BroBot's external brain is sleeping — try a simpler question!"
        else:
            reply = fallback

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5050)