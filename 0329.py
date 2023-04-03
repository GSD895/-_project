import tkinter as tk
import os
import openai

openai.api_key = "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"

messages = []

class DialogBox:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Dialog Box")
        
        # 텍스트가 나열 될 창 만들기
        self.conversation_text = tk.Text(self.parent, height=20, width=70, font=('Malgun Gothic', 15), bg='#B0E0E6')
        self.conversation_text.pack()
        
        # 사용자 입력 창 만들기
        self.user_input = tk.Entry(self.parent, width=60, font=('Malgun Gothic', 15))
        self.user_input.pack(side=tk.LEFT, padx=5, pady=5)
        self.user_input.bind("<Return>", self.submit)
        self.user_input.focus_set()     #자동으로 커서 놓이도록
        
        # submit을 실행시키는 버튼 생성
        self.submit_button = tk.Button(self.parent, text="Submit", command=self.submit, font=('Arial', 12))
        self.submit_button.pack()
        
        # Initialize the conversation
        self.conversation = ["Hello, how can I help you?"]
        self.display_conversation() #텍스트 위젯의 업데이트

    def submit(self, event = None):
        user_input = self.user_input.get()
        messages.append({"role": "user", "content": f"{user_input}"})
        self.conversation.append("User: " + user_input)
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        
        # TODO: process user input here and generate a response
        assistant_content = completion.choices[0].message["content"].strip()
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

# Create a root window and a dialog box instance
root = tk.Tk()
dialog_box = DialogBox(root)

root.mainloop()
