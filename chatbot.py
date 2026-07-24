from config import client

# Create a chat session with memory
chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)

def ask(question):
    try:
        response = chat.send_message(question)
        return response.text

    except Exception as e:
        return f"❌ Error:\n\n{e}"