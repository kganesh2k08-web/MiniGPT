from config import client

chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)

def ask(question):
    try:
        response = chat.send_message_stream(question)
        text = ""

        for chunk in response:
            if chunk.text:
                text += chunk.text

        return text

    except Exception as e:
        return f"❌ Error:\n\n{e}"