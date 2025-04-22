from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"error": "No message received"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or another model
            messages=[
                {"role": "system", "content": "You are a friendly mental health counselor."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

##############################################

from flask import Flask, request, jsonify
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import os

app = Flask(__name__)

# Set your OpenAI API Key
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

# Create the Langchain Chat Model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

# Add Conversation Memory
memory = ConversationBufferMemory()

# Create a ConversationChain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"error": "No message received"}), 400

    try:
        response = conversation.predict(input=user_message)
        return jsonify({"reply": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
