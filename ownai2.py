from google import genai

# Initialize the client with your Google AI Studio key
client = genai.Client(api_key="PASTE_YOUR_GEMINI_API_KEY_HERE")

print("AI Chatbot started! Type 'exit' to quit.\n")

while True:
    message = input("You: ")
    
    if message.lower() == "exit":
        print("Goodbye!")
        break

    # Send the message to Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message,
    )

    print(f"AI: {response.text}\n")