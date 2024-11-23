from flask import Flask, render_template, request, jsonify
import json
import random
from datetime import datetime

app = Flask(__name__)

# Enhanced conversation patterns and responses
CONVERSATIONS = {
    "greetings": {
        "patterns": ["hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"],
        "responses": [
            "Hello! How are you today?",
            "Hi there! It's great to hear from you!",
            "Hey! How can I help you today?"
        ]
    },
    "how_are_you": {
        "patterns": ["how are you", "how're you", "how you doing", "how do you do", "what's up"],
        "responses": [
            "I'm doing great, thanks for asking! How about you?",
            "I'm excellent! Always happy to chat with someone new. How are you?",
            "I'm wonderful! It's a great day for learning and conversation!"
        ]
    },
    "doing_well": {
        "patterns": ["good", "great", "fine", "wonderful", "fantastic", "amazing", "excellent"],
        "responses": [
            "That's wonderful to hear! What would you like to discuss?",
            "Excellent! I'm here if you want to know about any of my areas of expertise.",
            "Great to hear that! Feel free to ask me anything about tech!"
        ]
    },
    "doing_bad": {
        "patterns": ["bad", "not good", "terrible", "awful", "sad", "not well"],
        "responses": [
            "I'm sorry to hear that. I hope our conversation can help cheer you up!",
            "Things will get better! Let's talk about something interesting to lift your spirits.",
            "I hope your day gets better! What would you like to discuss?"
        ]
    },
    "thank_you": {
        "patterns": ["thank", "thanks", "appreciate", "grateful"],
        "responses": [
            "You're welcome! Is there anything else you'd like to know?",
            "Glad I could help! Feel free to ask more questions!",
            "My pleasure! What else would you like to discuss?"
        ]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "talk to you later", "cya"],
        "responses": [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! Feel free to come back if you have more questions!"
        ]
    }
}

# Technical expertise responses
EXPERTISE = {
    "data_science": {
        "patterns": ["data", "analysis", "visualization", "statistics", "pandas", "numpy", "analytics"],
        "responses": [
            "I specialize in data analysis and visualization using Python libraries like pandas and numpy.",
            "I work with large datasets and create insightful visualizations to extract meaningful patterns.",
            "Data science is my forte - from statistical analysis to predictive modeling."
        ]
    },
    "machine_learning": {
        "patterns": ["ml", "machine learning", "model", "algorithm", "training", "prediction"],
        "responses": [
            "I work with various ML algorithms and frameworks like scikit-learn and TensorFlow.",
            "I develop and optimize machine learning models for real-world applications.",
            "Machine learning is my passion - from basic algorithms to advanced neural networks."
        ]
    },
    "ai": {
        "patterns": ["ai", "artificial intelligence", "neural networks", "deep learning"],
        "responses": [
            "I'm deeply involved in AI research and development, especially in NLP and computer vision.",
            "I work on cutting-edge AI technologies and stay updated with the latest developments.",
            "AI is revolutionizing technology, and I'm excited to be part of this transformation."
        ]
    },
    "full_stack": {
        "patterns": ["web", "frontend", "backend", "full stack", "development"],
        "responses": [
            "I develop full-stack applications using modern frameworks like React and Node.js.",
            "I create scalable web applications with clean, maintainable code.",
            "Full-stack development allows me to build complete solutions from frontend to backend."
        ]
    },
    "cybersecurity": {
        "patterns": ["security", "cyber", "protection", "encryption", "vulnerability"],
        "responses": [
            "I implement robust security measures and conduct thorough security audits.",
            "I specialize in identifying and mitigating security vulnerabilities.",
            "Cybersecurity is crucial in modern applications, and I ensure all my projects are secure."
        ]
    }
}

def get_best_response(message):
    message = message.lower()
    words = message.split()
    
    # Check for conversational patterns first
    for category, content in CONVERSATIONS.items():
        if any(pattern in message for pattern in content["patterns"]):
            return random.choice(content["responses"])
    
    # Check for expertise-related questions
    for area, content in EXPERTISE.items():
        if any(pattern in message for pattern in content["patterns"]):
            return random.choice(content["responses"])
    
    # Default responses
    return random.choice([
        "I can tell you about my expertise in data science, machine learning, "
        "artificial intelligence, full-stack development, and cybersecurity. "
        "What would you like to know more about?",
        "I'm knowledgeable about various tech domains. Feel free to ask about any specific area!",
        "I can discuss various technical topics. What interests you the most?"
    ])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message', '')
    response = get_best_response(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
