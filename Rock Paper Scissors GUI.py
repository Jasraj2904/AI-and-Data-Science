from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x500")
root.config(bg="lightblue")

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    computer_label.config(text="Computer Chose: " + computer_choice)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text="Your Score: " + str(user_score) +
             "    Computer Score: " + str(computer_score)
    )

heading = Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 22, "bold"),
    bg="lightblue",
    fg="darkblue"
)
heading.pack(pady=20)

instruction = Label(
    root,
    text="Choose Rock, Paper or Scissors",
    font=("Arial", 14),
    bg="lightblue"
)
instruction.pack(pady=10)

rock_btn = Button(
    root,
    text="Rock",
    font=("Arial", 14),
    width=12,
    command=lambda: play("Rock")
)
rock_btn.pack(pady=10)

paper_btn = Button(
    root,
    text="Paper",
    font=("Arial", 14),
    width=12,
    command=lambda: play("Paper")
)
paper_btn.pack(pady=10)

scissors_btn = Button(
    root,
    text="Scissors",
    font=("Arial", 14),
    width=12,
    command=lambda: play("Scissors")
)
scissors_btn.pack(pady=10)

computer_label = Label(
    root,
    text="Computer Chose: ",
    font=("Arial", 14),
    bg="lightblue"
)
computer_label.pack(pady=20)

result_label = Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="lightblue",
    fg="red"
)
result_label.pack(pady=10)

score_label = Label(
    root,
    text="Your Score: 0    Computer Score: 0",
    font=("Arial", 14),
    bg="lightblue"
)
score_label.pack(pady=20)

exit_btn = Button(
    root,
    text="Exit Game",
    font=("Arial", 12),
    bg="red",
    fg="white",
    command=root.destroy
)
exit_btn.pack(pady=20)

root.mainloop()