import random

class DynamicBot:
    def __init__(self):
        self.greeted = False
        self.farewelled = False
        self.conversation_history = []

    def greet(self):
        self.greeted = True
        return random.choice(["Greetings!", "Hey there! How may I assist you?", "Hello! What's on your mind?"])

    def farewell(self):
        self.farewelled = True
        farewell_messages = [
            "Farewell!",
            "Wishing you a fantastic day!",
            "Until we meet again! All the best for your whole internship journey...!!, Hope you will learn a lot about many new things."
        ]
        return farewell_messages

    def handle_question(self, question):
        responses = {
            "what's your name": "My designation is DynamicBot.",
            "what can you do": "I'm equipped to engage in dialogue, provide information, and offer assistance.",
            "how are you": "I'm operating at optimal efficiency, thank you for inquiring!",
            "what's your favorite color": "I don't have personal preferences, but I admire a spectrum of colors.",
            "what's the weather like today": "In my digital realm, it's perpetually pleasant and temperate.",
            "how is your internship at nexus info going on": "As an AI, I don't have internships, but I'm here to assist you!",
        }
        return responses.get(question.lower(), "I'm uncertain how to respond to that question.")

    def ask_questions(self):
        questions = [
            "Tell me about a memorable experience you've had recently.",
            "If you could possess any superpower, what would it be and why?",
            "Share a skill or talent you're proud of.",
            "What's a goal or aspiration you're currently pursuing?",
            "How is your internship at Nexus Info going on?"
        ]
        for question in questions:
            answer = input(question + " ")
            print("That's intriguing! Thank you for sharing.")
            self.conversation_history.append(answer)
        farewell_messages = self.farewell()
        for message in farewell_messages:
            print(message)

    def process_user_input(self, user_input):
        if user_input.lower() in ["goodbye", "bye", "quit"]:
            farewell_messages = self.farewell()
            for message in farewell_messages:
                print(message)
            return ""
        elif user_input.lower().startswith(("what", "how")):
            response = self.handle_question(user_input)
            return f"DynamicBot: {response}"
        else:
            return "DynamicBot: I'm unsure how to respond. Could you rephrase your query?"

    def ask_user_question(self):
        user_question = input("Ask me a question: ")
        print("Interesting question! Let me try to answer that.")
        response = self.handle_question(user_question)
        print(f"DynamicBot: {response}")

def main():
    bot = DynamicBot()
    print(bot.greet())
    bot.ask_questions()

    while True:
        user_input = input("You: ")
        bot.conversation_history.append(user_input)

        if user_input.lower() in ["goodbye", "bye", "quit"]:
            farewell_messages = bot.farewell()
            for message in farewell_messages:
                print(message)
            break
        elif user_input.lower() == "ask":
            bot.ask_user_question()
        else:
            response = bot.process_user_input(user_input)
            print(response)

if __name__ == "__main__":
    main()
