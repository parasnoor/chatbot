import chainlit as cl  # Chainlit ko import karna

@cl.on_message  # Jab user message bheje, toh yeh function chalega
async def main(message: cl.Message):
    # Yeh chatbot user ka message wapas bhej raha hai
    await cl.Message(
        content=f"Received: {message.content}"
    ).send()
