import os
from anthropic import Anthropic
from dotenv import load_dotenv
from query import get_inventory

class ClaudeChatbot:
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)
        self.conversation_history = []
        self.load_context()

    def load_context(self):
        # Replace with query result
        inventory = get_inventory()

        context_prompt = f'You are an AI chatbot designed to provide insights on the stock status of an inventory based on structured data. The inventory includes the following entities and relationships: Stakeholder: Represents stakeholders associated with brands (e.g., name).  Brand: Represents brands and their stakeholders (e.g., name, stakeholder). Tag: Represents tags that categorize or classify inventory items (e.g., name). Product Type: Represents categories of products (e.g., name). Product: Represents individual products linked to a brand and product type (e.g., name, brand, product type). Product Tag: Tags assigned to specific products for further categorization (e.g., name). Inventory: Represents stock levels for each product (e.g., product, quantity). Response Guidelines: Focus only on the specific query asked by the customer and provide clear, concise, and organized information. Group responses logically by stakeholder, brand, product type, or tag, depending on the query. Do not provide irrelevant information or speculate outside the dataset. Example Queries and Responses: Product-Specific Query: Query: "What is the stock quantity of [product name]?" Response: "There is a total of [quantity] unit of [product name] in stock" Brand-Specific Query: Query: "Show the inventory status for all products under [brand name]." Response: "Stock status of [brand name] products: [list of [product name]: [quantity]]" Tag-Specific Query: Query: "List all products tagged with [tag name] and their stock quantities." Response: "Products tagged with [tag name]: [product name]" Stakeholder-Specific Query: Query: "Show the inventory managed by [stakeholder name]." Response: "Inventory of [stakeholder name]: [list of brand and products]" Product Type Query: Query: "What is the total stock quantity of [product type]?" Response: "There are in stock [number of products] products of type [product type]" The inventory information to answer all the questions from customer is the following: {inventory}'

        print(context_prompt)
        self.conversation_history.append({
            "role": "user", 
            "content": context_prompt
        })

    def send_message(self, user_message):
        # Add user message to conversation history
        self.conversation_history.append({
            "role": "user", 
            "content": user_message
        })

        # Send message to Claude
        response = self.client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            messages=self.conversation_history
        )

        # Extract and store Claude's response
        claude_message = response.content[0].text
        self.conversation_history.append({
            "role": "assistant", 
            "content": claude_message
        })

        return claude_message

    def reset_conversation(self):
        self.conversation_history = []

# def main():
#     load_dotenv()
#     api_key = os.getenv("ANTHROPIC_API_KEY")
#     chatbot = ClaudeChatbot(api_key)

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ['exit', 'quit']:
#             break
        
#         response = chatbot.send_message(user_input)
#         print("Bot:", response)

# if __name__ == "__main__":
#     main()