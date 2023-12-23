import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from boba_fett import boba_fett

def show_question():
    question = boba_fett[current_question]
    qs_label.config(text=question["question"])
    choices = question["choices"]

    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    feedback_label.config(text="")
    next_btn.config(state="disabled")

def check_answer(choice):
    question = boba_fett[current_question]
    selected_choice = choice_btns[choice].cget("text")

    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(boba_fett)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

def next_question():
    global current_question
    current_question +=1

    if current_question < len(boba_fett):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed", "Quiz Completed! Final score: {}/{}".format(score, len(boba_fett)))
        root.destroy()

root = tk.Tk()
root.title("QuizShik - Tkinter Edition")
root.geometry("600x550")
style = Style(theme="flatly")

style.configure("TLabel", font=("Times New Roman", 20))
style.configure("TButton", font=("Verdana", 16))

qs_label = ttk.Label(root, anchor="center", wraplength=500, padding=10)
qs_label.pack(pady=10)

choice_btns = []
for i in range(4):
    button = ttk.Button(root, command=lambda i=i: check_answer(i))
    button.pack(pady=5)
    choice_btns.append(button)

feedback_label = ttk.Label(root, anchor="center", padding=10)
feedback_label.pack(pady=10)

score = 0
score_label = ttk.Label(root, text="Score: 0/{}".format(len(boba_fett)), anchor="center", padding=10)
score_label.pack(pady=10)

next_btn = ttk.Button(root, text="Next", command=next_question, state="disabled")
next_btn.pack(pady=10)

current_question = 0

show_question()

root.mainloop()