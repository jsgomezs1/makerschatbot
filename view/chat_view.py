import gradio as gr
import requests

def send_message(message, chat_history, chat_id=None):
    backend_url = "http://127.0.0.1:8000"
    user_url = f"{backend_url}/core/users/"

    response = requests.get(user_url)
    if response.status_code == 200:
        user_id = response.json()[0]["id"]
    else:
        return

    chat_url = f"{backend_url}/chat/claude"
    payload = {
        "prompt": message,
        "created_by": user_id
    }

    if chat_id:
        payload["chat_id"] = chat_id

    print(payload)
    headers = {"Content-Type": "application/json"}
    response = requests.post(chat_url, json=payload, headers=headers)
    if response.status_code == 201:
        bot_reply = response.json()["response"]
    else:
        bot_reply = f"Error:{response}"


    chat_history.append(
        gr.ChatMessage(role="user", content=message)
    )
    
    chat_history.append(
        gr.ChatMessage(role="assistant", content=bot_reply)
    )
    return chat_history, ""


# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## AI-Powered Chatbot")
    chat = gr.Chatbot(label="AI Inventory bot", type="messages")
    message_input = gr.Textbox(label="Ask something",placeholder="Type your message here...")
    reload_button = gr.Button("Clear chat")
    
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
