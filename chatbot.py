import tkinter as tk
from tkinter import scrolledtext

from nltk.chat import Chat
from nltk.chat.iesha import reflections


class ChatGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot GUI")

        # Create and configure the text widget
        self.chat_display = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=15,font=('serif',20))
        self.chat_display.pack(padx=10, pady=10)

        # Create and configure the entry widget
        self.user_input_entry = tk.Entry(master, width=50,font=('serif',20))
        self.user_input_entry.pack(padx=10, pady=10)

        # Create and configure the send button
        self.send_button = tk.Button(master, text="Send", command=self.send_message, font=(20))
        self.send_button.pack(pady=5)

        # Create chatbot
        self.chatbot_patterns = [
            (r'Hi|Hello|Hey', ['Hello!',
                               'Hi there!',
                               'Hey!']),

            (r'How are you', ['I am doing well, thank you!',
                              'I am good. How about you?',
                              'Not bad, thanks for asking.']),

            (r'What is your name', ['I am a chatbot. and you ',
                                    'You can call me Nova. and you',
                                    'I don\'t have a name, but you can just call me chatbot. and you']),

            (r'Bye|goodbye', ['Goodbye!',
                              'See you later!',
                              'Bye!']),

            (r'I need (.*)', ["Why do you need %1?",
                              "Would it really help you to get %1?",
                              "Are you sure you need %1?", ]),

            (r"Why don't you (.*)", ["Do you really think I don't %1?",
                                     "Perhaps eventually I will %1.",
                                     "Do you really want me to %1?", ]),

            (r"Why can't i (.*)", ["Do you think you should be able to %1?",
                                   "If you could %1, what would you do?",
                                   "I don't know -- why can't you %1?",
                                   "Have you really tried?", ]),

            (r"I can't (.*)", ["How do you know you can't %1?",
                               "Perhaps you could %1 if you tried.",
                               "What would it take for you to %1?", ]),

            (r"I am (.*)", ["Did you come to me because you are %1?",
                            "How long have you been %1?",
                            "How do you feel about being %1?", ]),

            (r"I\'m (.*)", ["How does being %1 make you feel?",
                            "Do you enjoy being %1?",
                            "Why do you tell me you're %1?",
                            "Why do you think you're %1?", ]),

            (r"Are you (.*)", ["Why does it matter whether I am %1?",
                               "Would you prefer it if I were not %1?",
                               "Perhaps you believe I am %1.",
                               "I may be %1 -- what do you think?", ]),

            (r"What (.*)", ["Why do you ask?",
                            "How would an answer to that help you?",
                            "What do you think?", ]),

            (r"How (.*)", ["How do you suppose?",
                           "Perhaps you can answer your own question.",
                           "What is it you're really asking?", ]),

            (r"Because (.*)", ["Is that the real reason?",
                               "What other reasons come to mind?",
                               "Does that reason apply to anything else?",
                               "If %1, what else must be true?", ]),

            (r"(.*) sorry (.*)", ["There are many times when no apology is needed.",
                                  "What feelings do you have when you apologize?", ]),

            (r"Hello(.*)", ["Hello... I'm glad you could drop by today.",
                            "Hi there... how are you today?",
                            "Hello, how are you feeling today?", ]),

            (r"(.*) friend (.*)", ["Tell me more about your friends.",
                                   "When you think of a friend, what comes to mind?",
                                   "Why don't you tell me about a childhood friend?", ]),

            (r"I think (.*)", ["Do you doubt %1?",
                               "Do you really think so?",
                               "But you're not sure %1?"]),

            (r"Yes", ["You seem quite sure.",
                      "OK, but can you elaborate a bit?"]),

            (r"(.*) computer(.*)", ["Are you really talking about me?",
                                    "Does it seem strange to talk to a computer?",
                                    "How do computers make you feel?",
                                    "Do you feel threatened by computers?", ]),

            (r"Is it (.*)", ["Do you think it is %1?",
                             "Perhaps it's %1 -- what do you think?",
                             "If it were %1, what would you do?",
                             "It could well be that %1.", ]),

            (r"It is (.*)", ["You seem very certain.",
                             "If I told you that it probably isn't %1, what would you feel?", ]),

            (r"Can you (.*)", ["What makes you think I can't %1?",
                               "If I could %1, then what?",
                               "Why do you ask if I can %1?", ]),

            (r"Can I (.*)", ["Perhaps you don't want to %1.",
                             "Do you want to be able to %1?",
                             "If you could %1, would you?", ]),

            (r"You are (.*)", ["Why do you think I am %1?",
                               "Does it please you to think that I'm %1?",
                               "Perhaps you would like me to be %1.",
                               "Perhaps you're really talking about yourself?", ]),

            (r"You\'re (.*)", ["Why do you say I am %1?",
                               "Why do you think I am %1?",
                               "Are we talking about you, or me?", ]),

            (r"I don't (.*)", ["Don't you really %1?",
                               "Why don't you %1?",
                               "Do you want to %1?"]),

            (r"No| Not | Not sure", ["ok not problem...."]),

            (r"My name is (.*)", ["Ooo i see , hello %1?"])
             ]
        self.chatbot = Chat(self.chatbot_patterns, reflections)

        # Welcome message
        self.display_message("Chatbot: Hello! Ask me anything or say goodbye to end the conversation.")

    def send_message(self):
        user_input = self.user_input_entry.get().lower()
        self.display_message(f"You: {user_input}")
        self.user_input_entry.delete(0, tk.END)  # Clear the entry

        if user_input == 'goodbye':
            self.display_message("Chatbot: Goodbye! Have a great day!")
            self.master.after(2000, self.master.destroy)  # Close the window after 2 seconds
        else:
            response = self.chatbot.respond(user_input)
            self.display_message(f"Chatbot: {response}")

    def display_message(self, message):
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.yview(tk.END)  # Auto-scroll to the bottom

if __name__ == "__main__":
    root = tk.Tk()
    chat_gui = ChatGUI(root)
    root.mainloop()

