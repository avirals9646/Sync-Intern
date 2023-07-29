from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

class UniversityChatbot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("United University Chatbot")
        self.geometry("400x500")
        self.iconbitmap(r"favicons.ico")
        self.config(bg='lightyellow')

        self.background_image = PhotoImage(file="Chatbot.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        

        
        self.chat_log = tk.Text(self, wrap="word", bg="white", font=("Arial", 12), padx=10, pady=10)
        self.chat_log.pack(fill="both", expand=True)
        
        self.user_input = tk.Entry(self, font=("Arial", 12))
        self.user_input.pack(fill="x", padx=10, pady=10)
        self.user_input.bind("<Return>", self.on_user_input)
        
        self.add_chatbot_response("University: Hello! I'm your virtual assistant. How can I assist you?")
        
    def add_chatbot_response(self, response):
        self.chat_log.insert("end", "\n" + response)
        self.chat_log.see("end")
        
    def on_user_input(self, event):
        user_message = self.user_input.get()
        self.add_chatbot_response("You: " + user_message)
        self.user_input.delete(0, "end")
        self.process_user_input(user_message.lower())
        
    def process_user_input(self, user_message):
        if "course" in user_message:
            self.add_chatbot_response("University: We offer various courses such as Computer Science, Business Administration, and Psychology.")
        elif "fee" in user_message or "fees" in user_message:
            self.add_chatbot_response("University: The fee for each course depends on the program and may vary. Please visit our website for detailed fee information.")
        elif "facility" in user_message or "faculty" in user_message:
            self.add_chatbot_response("University: We offer world class education with experienced faculty and provides you all the facilities.")
        else:
            self.add_chatbot_response("University: I'm sorry, but I didn't understand your question. Could you please rephrase it?")
        
if __name__ == "__main__":
    app = UniversityChatbot()
    app.mainloop()
