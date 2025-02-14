# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob

# Defining the ChatBot class for interaction.
intents = {
    "hours": {
        "keywords": ["hours", "open", "close"],
        "response": "We are open from 9am to 5pm, Monday to Friday"
    },
    "return": {
        "keywords": ["return", "refund", "money back"],
        "response": "I'd be happy to help with you're return process. I'll transfer you to a live agent."
    }

}

def get_response(message):
    message = message.lower()

    for intent in intents.values():
        if any(word in message for word in intent["keywords"]):
            return intent["response"]
    
    # Analyzing the sentiment of the user's message.
    sentiment = TextBlob(message).sentiment.polarity

    # Generating the chatbot's response based on sentiment.
    return ("That's great" 
        if sentiment > 0 
        else "I'm sorry to hear that, how can i help?" 
        if sentiment < 0 
        else "I see, can you provide more information?"
        )

    # Printing the chatbot's response and sentiment.
          
def chat():
    print("Hi, how can i help you today?")

    while (user_message := input("You: ").strip().lower()) not in ["exit", "quit", "bye"]:
        print(f"\nChatbot: {get_response(user_message)}")

if __name__ == "__main__":
    chat()
