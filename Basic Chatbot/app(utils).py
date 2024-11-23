from flask import Flask, render_template, request, jsonify
import spacy
import datetime
import json
import random
from chatbot_utils import get_response, load_intents, get_greeting

app = Flask(__name__)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load intents
intents = load_intents()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def bot_response():
    user_message = request.json['message']
    
    # Get current time for greeting
    current_hour = datetime.datetime.now().hour
    
    # Process the message with spaCy
    doc = nlp(user_message.lower())
    
    # Get appropriate response
    response = get_response(doc, intents)
    
    # If it's a greeting, add time-appropriate greeting
    if any(token.text in ['hi', 'hello', 'hey'] for token in doc):
        greeting = get_greeting(current_hour)
        response = f"{greeting}! {response}"
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
