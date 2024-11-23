import json
import random
import datetime

def load_intents():
    return {
        "greetings": [
            "How can I help you today?",
            "Nice to meet you! I'm GammaCube AI Assistant.",
            "Hello! I'm here to help with your questions about data science, programming, and AI."
        ],
        "about_creator": [
            "I was created by Anthony Opoku-Acheampong (Tony for short). He's a talented data scientist and the founder of GammaCube!",
            "My creator is Tony, a data science student passionate about AI, machine learning, and cybersecurity. He's also the founder of GammaCube.",
            "I'm proud to be created by Tony, a multifaceted tech enthusiast who founded GammaCube. He specializes in data science, full stack development, and AI."
        ],
        "data_science": [
            "Data Science involves extracting insights from data using various statistical and computational techniques.",
            "The key areas of Data Science include data analysis, machine learning, and statistical modeling.",
            "Data Science combines programming, statistics, and domain expertise to solve complex problems."
        ],
        "python_programming": [
            "Python is a versatile programming language widely used in data science and AI.",
            "Python offers great libraries like pandas, numpy, and scikit-learn for data analysis and machine learning.",
            "Python's simplicity and extensive ecosystem make it perfect for both beginners and experts."
        ],
        "machine_learning": [
            "Machine Learning is a subset of AI that enables systems to learn from data.",
            "Popular ML algorithms include regression, classification, and clustering.",
            "Deep Learning is a specialized form of machine learning using neural networks."
        ],
        "ai": [
            "Artificial Intelligence aims to create systems that can simulate human intelligence.",
            "AI encompasses various fields like machine learning, natural language processing, and computer vision.",
            "Modern AI applications include chatbots, recommendation systems, and autonomous vehicles."
        ],
        "gammacube": [
            "GammaCube is an innovative tech startup founded by Tony, focusing on cutting-edge technology solutions.",
            "At GammaCube, we're passionate about advancing technology through AI and data science.",
            "GammaCube combines expertise in data science, AI, and cybersecurity to create innovative solutions."
        ]
    }

def get_greeting(hour):
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

def get_response(doc, intents):
    # Basic intent matching based on keywords
    if any(token.text in ['who', 'creator', 'made', 'tony'] for token in doc):
        return random.choice(intents["about_creator"])
    
    elif any(token.text in ['data', 'science', 'analysis'] for token in doc):
        return random.choice(intents["data_science"])
    
    elif any(token.text in ['python', 'programming', 'code'] for token in doc):
        return random.choice(intents["python_programming"])
    
    elif any(token.text in ['machine', 'learning', 'ml'] for token in doc):
        return random.choice(intents["machine_learning"])
    
    elif any(token.text in ['ai', 'artificial', 'intelligence'] for token in doc):
        return random.choice(intents["ai"])
    
    elif any(token.text in ['gammacube', 'company', 'startup'] for token in doc):
        return random.choice(intents["gammacube"])
    
    elif any(token.text in ['hi', 'hello', 'hey'] for token in doc):
        return random.choice(intents["greetings"])
    
    return "I'm not sure about that, but I'd be happy to discuss data science, Python programming, machine learning, or AI!"
