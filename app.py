import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Get Hugging Face token from environment variable
HF_TOKEN = os.environ.get('HF_TOKEN')
HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

@app.route('/')
def home():
    """Serve the frontend interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
    try:
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"error": "No message provided"}), 400
        
        # Craft the prompt
        prompt = f"""You are a health assistant. Give a short, friendly tip about longevity or fitness. 
        Respond in 1-2 sentences. User request: {user_message}"""
        
        # Call Hugging Face API
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
        
        # Handle potential API errors
        if response.status_code != 200:
            return jsonify({"error": "Model API failed"}), 500
            
        full_text = response.json()[0]['generated_text']
        
        # Extract assistant's response
        assistant_response = full_text.split(prompt)[-1].strip()
        
        return jsonify({"reply": assistant_response})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/test')
def test():
    return "Works!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
