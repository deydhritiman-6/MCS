import random
import tkinter as tk

facts_list = [
    "The 1st Ballon D'Or was won by Stanley Matthews in 1956",
    "Real Madrid have the most UEFA Champions Leagues",
    (
        "The 2026 Ballon D'Or was won by Harry Kane who is english and plays"
        " for Bayern Munchen "
    ),
]


def show_fact():
    selected_fact = random.choice(facts_list)
    facts_label.config(text=selected_fact)


app = tk.Tk()
app.configure(bg="light blue")
app.geometry("400x300")
app.title("Football Facts")

title_label = tk.Label(
    app,
    text="Random Football Facts",
    font=("Arial", 16, "bold"),
    bg="light blue",
    fg="#333333",
)
title_label.pack(pady=20)

facts_label = tk.Label(
    app,
    text="Click the button below to see a fact.",
    font=("Arial", 11),
    wraplength=350,
    justify="center",
    bg="light blue",
)
facts_label.pack(pady=20, padx=30)

btn = tk.Button(
    app,
    text="Get a New fact",
    font=("Arial", 12),
    bg="#ffffff",
    command=show_fact,
)
btn.pack(pady=10)  # this was missing, so the button never appeared

app.mainloop()  # this was missing, so the window never stayed open