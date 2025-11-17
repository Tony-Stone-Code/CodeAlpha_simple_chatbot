# Groq API Integration Guide

## Overview
This chatbot now uses the Groq API to provide intelligent, context-aware responses powered by advanced language models. The integration includes a fallback mechanism to ensure the chatbot remains functional even without an API key.

## Getting Your Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in to your account
3. Navigate to the API Keys section
4. Click "Create API Key"
5. Copy your new API key

## Setup Instructions

### 1. Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file and add your API key
# You can use any text editor, for example:
nano .env
# or
vim .env
```

Add your Groq API key to the `.env` file:
```
GROQ_API_KEY=your_actual_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

### 2. Available Models

You can configure which Groq model to use by setting the `GROQ_MODEL` environment variable. Popular options include:

- `llama-3.3-70b-versatile` (default) - Best for general conversation
- `mixtral-8x7b-32768` - Good for complex tasks
- `gemma2-9b-it` - Fast and efficient

### 3. Test Your Setup

```bash
# Make sure you're in the Basic Chatbot directory
cd "Basic Chatbot"

# Run the application
python3 app.py
```

You should see:
```
✓ Groq API initialized successfully
```

If you see an error message, check:
- Your API key is correct
- The .env file is in the correct directory
- You have internet connectivity

## How It Works

### Response Flow

1. **User sends a message** → Flask receives the request
2. **Try Groq API** → If API key is configured, get AI response
3. **Fallback** → If Groq API fails, use rule-based responses
4. **Return response** → Send back to user

### System Prompt

The chatbot is configured with a custom system prompt that gives it context about Tony's expertise:

- Data Science & Analytics
- Machine Learning
- Artificial Intelligence
- Full Stack Development
- Cybersecurity

This ensures responses are aligned with the chatbot's intended personality and knowledge areas.

### API Parameters

The integration uses these parameters for optimal performance:

- **temperature**: 0.7 (balanced creativity and coherence)
- **max_tokens**: 500 (concise but informative responses)
- **top_p**: 1 (standard sampling)
- **stream**: False (complete response at once)

## Error Handling

The chatbot gracefully handles various error scenarios:

- **No API key**: Falls back to rule-based responses
- **Invalid API key**: Falls back to rule-based responses
- **Network errors**: Falls back to rule-based responses
- **API rate limits**: Falls back to rule-based responses

## Troubleshooting

### Issue: "GROQ_API_KEY not found"
**Solution**: Make sure you've created a `.env` file with your API key.

### Issue: "Failed to initialize Groq API"
**Solution**: Check that your API key is valid and you have internet connectivity.

### Issue: API responses are slow
**Solution**: Try switching to a faster model like `gemma2-9b-it` in your `.env` file.

### Issue: API quota exceeded
**Solution**: Check your Groq account usage limits. The chatbot will automatically fall back to rule-based responses.

## Security Best Practices

✅ **DO:**
- Keep your API key in the `.env` file
- Add `.env` to `.gitignore` (already done)
- Regenerate your API key if it's accidentally exposed
- Use environment variables for all sensitive data

❌ **DON'T:**
- Commit your `.env` file to git
- Share your API key publicly
- Hardcode your API key in source code
- Use the same API key across multiple projects

## Benefits of Groq API

- ⚡ **Lightning-fast inference** - Responses in milliseconds
- 🧠 **Advanced AI models** - State-of-the-art language understanding
- 💰 **Cost-effective** - Competitive pricing
- 🔄 **Easy integration** - Simple Python SDK
- 📊 **Multiple models** - Choose the right model for your needs

## Next Steps

After successful integration, you can:

1. Customize the system prompt in `app.py`
2. Adjust temperature for different response styles
3. Increase max_tokens for longer responses
4. Add conversation history for context-aware chats
5. Implement streaming responses for real-time output

## Support

If you encounter issues:
1. Check the Groq API [documentation](https://console.groq.com/docs)
2. Review the error messages in the console
3. Ensure all dependencies are installed: `pip install -r requirements.txt`
4. Open an issue on the GitHub repository
