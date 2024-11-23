document.addEventListener('DOMContentLoaded', function() {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const themeSwitch = document.getElementById('theme-switch');
    let isProcessing = false;

    // Theme handling with smooth transition
    function setTheme(isDark) {
        const root = document.documentElement;
        root.style.setProperty('--transition-speed', '0.5s');
        document.body.classList.toggle('dark-mode', isDark);
        document.body.classList.toggle('light-mode', !isDark);
        localStorage.setItem('darkMode', isDark);
        
        setTimeout(() => {
            root.style.setProperty('--transition-speed', '0.3s');
        }, 500);
    }

    // Check for saved theme preference or system preference
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const savedTheme = localStorage.getItem('darkMode');
    setTheme(savedTheme !== null ? savedTheme === 'true' : prefersDark);

    // Theme switch with animation
    themeSwitch.addEventListener('click', () => {
        const isDark = !document.body.classList.contains('dark-mode');
        themeSwitch.style.transform = 'scale(0.8) rotate(180deg)';
        setTimeout(() => {
            themeSwitch.style.transform = 'scale(1) rotate(360deg)';
            setTheme(isDark);
        }, 200);
    });

    // System theme change listener
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
        if (localStorage.getItem('darkMode') === null) {
            setTheme(e.matches);
        }
    });

    function formatTime() {
        const now = new Date();
        return now.toLocaleTimeString('en-US', { 
            hour: 'numeric', 
            minute: '2-digit',
            hour12: true 
        }).toLowerCase();
    }

    function addMessage(message, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
        
        const bubbleDiv = document.createElement('div');
        bubbleDiv.className = 'message-content ios-bubble';
        bubbleDiv.textContent = message;
        
        const timeDiv = document.createElement('div');
        timeDiv.className = 'message-time';
        timeDiv.textContent = formatTime();
        
        messageDiv.appendChild(bubbleDiv);
        messageDiv.appendChild(timeDiv);
        chatMessages.appendChild(messageDiv);
        
        // Smooth scroll with spring effect
        chatMessages.scrollTo({
            top: chatMessages.scrollHeight,
            behavior: 'smooth'
        });
        
        // Add haptic feedback if supported
        if (window.navigator && window.navigator.vibrate) {
            window.navigator.vibrate(isUser ? 10 : 8);
        }

        // Message animation
        requestAnimationFrame(() => {
            bubbleDiv.style.transform = 'scale(0.8) translateY(20px)';
            bubbleDiv.style.opacity = '0';
            requestAnimationFrame(() => {
                bubbleDiv.style.transition = 'transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.3s ease';
                bubbleDiv.style.transform = 'scale(1) translateY(0)';
                bubbleDiv.style.opacity = '1';
            });
        });
    }

    async function sendMessage() {
        if (isProcessing) return;
        
        const message = userInput.value.trim();
        if (message === '') return;
        
        isProcessing = true;
        userInput.value = '';
        
        // Send button animation
        sendBtn.style.transform = 'scale(0.8) rotate(-45deg)';
        setTimeout(() => {
            sendBtn.style.transform = 'scale(1) rotate(0)';
        }, 200);
        
        addMessage(message, true);
        
        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });
            
            const data = await response.json();
            
            setTimeout(() => {
                addMessage(data.response);
                isProcessing = false;
            }, 500);
            
        } catch (error) {
            console.error('Error:', error);
            setTimeout(() => {
                addMessage('Sorry, I encountered an error. Please try again.');
                isProcessing = false;
            }, 500);
        }
    }

    // Event Listeners
    sendBtn.addEventListener('click', sendMessage);
    
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    // Input animations
    userInput.addEventListener('focus', function() {
        this.parentElement.style.transform = 'scale(1.01)';
        this.parentElement.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.1)';
    });

    userInput.addEventListener('blur', function() {
        this.parentElement.style.transform = 'scale(1)';
        this.parentElement.style.boxShadow = 'none';
    });

    // Dynamic input height
    userInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = Math.min(this.scrollHeight, 100) + 'px';
    });

    // Focus input on page load with delay for smooth animation
    setTimeout(() => {
        userInput.focus();
    }, 300);
});
