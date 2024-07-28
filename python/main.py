import os
from flask import Flask, request, jsonify
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

app = Flask(__name__)

api_key = os.environ["MISTRAL_API_KEYS"]
model = "mistral-large-latest"
client = MistralClient(api_key=api_key)

@app.route('/ask', methods=['GET'])
def ask():
    user_message = request.args.get("ask", "")

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=user_message)]
    )

    response_content = chat_response.choices[0].message.content

    return jsonify({"response": response_content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
