Dina AI - Virtual Assistant by Dineth

Dina AI is a smart and visually appealing chatbot that uses both a locally trained model and fallback AI models (via OpenRouter) to answer your queries. Designed to mimic a helpful assistant, it delivers fast, intelligent responses and includes an attractive UI with a custom avatar, typing animation, and fallback logic.

![Dina AI Screenshot](images/dina-chat-preview.png)

 Features

-Locally trained chatbot** with intent recognition  
-OpenRouter fallback** (Mistral, OpenChat, LLaMA2) for complex questions  
- Sleek, modern UI with:
 - Avatar
 - Typing animation
 - Responsive layout
- Memory support (remembers your name!)
- Built using **Python + Flask**

 Demo

Try asking things like:
- `Who are you?`
- `Write a poem about the stars`
- `Tell me a joke`
- `What’s the capital of Mars?`

If Dina doesn’t understand, she’ll escalate it to smarter fallback models — automatically.

Installation

bash
git clone https://github.com/Dineth-Basura/Dina-ai-chatbot.git
cd Dina-ai-chatbot
pip install -r requirements.txt

Run the Bot:

python train_bot.py    # optional - re-train local AI
python app.py

Visit: http://127.0.0.1:5050/ in your browser.

Folder Structure

Dina-ai-chatbot/
├── app.py
├── train_bot.py
├── requirements.txt
├── intents.json
├── memory.json
├── static/
│   ├── style.css
│   └── dinaAi.jpeg
├── templates/
│   └── index.html
├── utils/
│   ├── local_bot.py
│   └── deepseek_api.py
└── images/
    └── dina-chat-ui.png   ← your screenshots here!

Preview



Connect With Me

Author: Dineth Basura
LinkedIn Profile :  https://www.linkedin.com/in/dineth-basura-00711035a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app



![Dina UI](https://github.com/user-attachments/assets/c6f87d87-c3e4-4f65-8594-38262fc30d17)
![dinaAi](https://github.com/user-attachments/assets/791ba9f6-d4e3-4d45-b640-be8dafffe0a4)


