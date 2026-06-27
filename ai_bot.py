import os
from openai import OpenAI

# 1. Initialize the client.
# It automatically picks up the "OPENAI_API_KEY" environment variable,
# or you can pass it directly: client = OpenAI(api_key="your-key-here")
client = OpenAI(api_key=os.environ.get("REMOVED_API_KEY"))

def start_chatbot():
    print("🤖 AI Bot: Hello! I am ready. Type 'exit' to end the chat.\n")
    
    # 2. System prompt defines the bot's identity/personality
    messages = [
        {"role": "system", "content": "You are a helpful, clever, and slightly witty AI assistant."}
    ]
    
    while True:
        # Get input from the user
        user_input = input("You: ")
        
        # Check for break condition
        if user_input.lower() == 'exit':
            print("🤖 AI Bot: Goodbye!")
            break
            
        if not user_input.strip():
            continue
            
        # 3. Append user message to memory history
        messages.append({"role": "user", "content": user_input})
        
        try:
            # 4. Request a completion from the model
            # We use gpt-4o-mini here as it is fast and cost-effective
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages,
                temperature=0.7
            )
            
            # Extract the bot's response text
            bot_reply = response.choices[0].message.content
            print(f"\n🤖 AI Bot: {bot_reply}\n")
            
            # 5. Append the bot's own reply back to the memory history
            messages.append({"role": "assistant", "content": bot_reply})
            
        except Exception as e:
            print(f"\n❌ Error: Could not fetch response. {e}\n")

if __name__ == "__main__":
    start_chatbot()
