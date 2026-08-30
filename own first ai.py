from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key="sk-your-real-api-key-goes-here")

print("AI Chatbot started! Type 'exit' to quit.\n")

while True:
    message = input("You: ")
    
    if message.lower() == "exit":
        print("Goodbye!")
        break

    # Send the message to the model using the correct chat completions endpoint
    response = client.chat.completions.create(
        model="gpt-4o-mini", # Using a fast, standard model
        messages=[{"role": "user", "content": message}]
    )

    # Extract and print the assistant's reply
    ai_reply = response.choices[0].message.content
    print(f"AI: {ai_reply}\n")