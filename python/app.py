from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure the Generative AI API
genai.configure(api_key="AIzaSyCrS86qv4pF6mZHsTNyuVEWuyuDJU5KVyE")
model = genai.GenerativeModel('gemini-1.5-flash')

# Stores the conversation context
context = ""

# Function to generate AI response
def generate_ai_response(context, user_message):
    prompt = f"Context: {context}. Respond to this user message as a friendly professional.\nUser Message: {user_message}"
    response = model.generate_content(prompt)
    try:
        candidate = response.candidates[0]
        content = candidate.content
        text_content = content.parts[0].text
        return text_content
    except (IndexError, AttributeError):
        return "Sorry, I couldn't generate a response. Please try again."

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    global context
    user_message = request.json.get("message")
    ai_reply = generate_ai_response(context, user_message)
    context += f"\nUser: {user_message}\nAI: {ai_reply}"
    return jsonify({"user_message": user_message, "ai_reply": ai_reply})

if __name__ == "__main__":
    app.run(debug=True)
