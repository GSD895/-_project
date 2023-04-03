import tkinter as tk
import os
import openai

openai.api_key = "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"

messages = []

class DialogBox:
    def __init__(self, parent, switch_frame_callback):
        self.parent = parent
        self.switch_frame_callback = switch_frame_callback
        self.parent.title("Dialog Box")

        # Create a window where the text will be listed
        self.conversation_text = tk.Text(self.parent, height=20, width=70, font=('Malgun Gothic', 15), bg='#B0E0E6')
        self.conversation_text.pack()

        # Create a user input window
        self.user_input = tk.Entry(self.parent, width=60, font=('Malgun Gothic', 15))
        self.user_input.pack(side=tk.LEFT, padx=5, pady=5)
        self.user_input.bind("<Return>", self.submit)
        self.user_input.focus_set() #set cursor automatically

        # Create a button that triggers submit
        self.submit_button = tk.Button(self.parent, text="Submit", command=self.submit, font=('Arial', 12))
        self.submit_button.pack()

        # Initialize the conversation
        self.conversation = ["Hello, how can I help you?"]
        self.display_conversation() #update text widget

    def submit(self, event = None):
        user_input = self.user_input.get()
        messages.append({"role": "user", "content": f"{user_input}"})
        self.conversation.append("User: " + user_input)
        completion = openai.Completion.create(engine="davinci", prompt=f"Conversation with the user:\n{self.conversation[-1]}\n\nBot:")
        assistant_content = completion.choices[0].text.strip()
        messages.append({"role": "assistant", "content": f"{assistant_content}"})
        self.conversation.append("Bot: " + assistant_content)
        self.user_input.delete(0, tk.END)
        self.display_conversation()

    def display_conversation(self):
        self.conversation_text.config(state=tk.NORMAL)
        self.conversation_text.delete("1.0", tk.END)
        for line in self.conversation:
            self.conversation_text.insert(tk.END, line + "\n")
        self.conversation_text.config(state=tk.DISABLED)
        self.conversation_text.see(tk.END)
        
class NewScreen:
    def __init__(self, parent, switch_frame_callback):
        self.parent = parent
        self.switch_frame_callback = switch_frame_callback
        self.parent.title("New Screen")
        
        # Create a label to display some text
        self.label = tk.Label(self.parent, text="This is a new screen!", font=('Arial', 20))
        self.label.pack(padx=50, pady=50)
        
        # Create a button that switches back to the dialog box
        self.back_button = tk.Button(self.parent, text="Back to Dialog Box", command=self.switch_to_dialog_box, font=('Arial', 12))
        self.back_button.pack()

    def switch_to_dialog_box(self):
        self.switch
# Create a root window and a dialog box instance
root = tk.Tk()
dialog_box = DialogBox(root)

root.mainloop()