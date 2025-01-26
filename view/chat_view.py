import gradio as gr

def send_message(message, chat_history):
    chat_history.append(
        gr.ChatMessage(role="user", content=message)
    )

    # Call endpoint or function to generate conversation
    if message.strip().lower() == "hello":
        bot_reply = "Hi there! How can I help you today?"
    else:
        bot_reply = f"You said: {message}"
    
    
    # Add user message and bot reply to the chat history
    chat_history.append(
        gr.ChatMessage(role="assistant", content=bot_reply)
    )
    return chat_history, ""


# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## AI-Powered Chatbot")
    chat = gr.Chatbot(label="AI Inventory bot", type="messages")
    message_input = gr.Textbox(placeholder="Type your message here...")
    reload_button = gr.Button("New conversation")
    
    # Gradio state to matain chat history
    chat_history = gr.State([])

    message_input.submit(send_message, 
                         inputs=[message_input, chat_history],
                         outputs=[chat, message_input])
    
    # Clear message history
    chat.clear(
        None,
        js="window.location.reload()"
    )
    reload_button.click(
        None, 
        js="window.location.reload()"
    )

# Launch the app
if __name__ == "__main__":
    demo.launch(pwa=True)
