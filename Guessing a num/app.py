import tkinter as tk
import random

class GuessingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" Guessing Game")
        self.root.geometry("400x300")
        
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        # Title
        self.label_title = tk.Label(root, text=" Guess the Number (1-100)", font=("Arial", 14, "bold"))
        self.label_title.pack(pady=10)

        # Entry
        self.entry_guess = tk.Entry(root, font=("Arial", 12))
        self.entry_guess.pack(pady=5)

        # Button
        self.button_submit = tk.Button(root, text="Submit Guess", font=("Arial", 12), command=self.check_guess)
        self.button_submit.pack(pady=10)

        # Feedback
        self.label_feedback = tk.Label(root, text="", font=("Arial", 12))
        self.label_feedback.pack(pady=5)

        # Attempts
        self.label_attempts = tk.Label(root, text="Attempts: 0", font=("Arial", 12))
        self.label_attempts.pack(pady=5)

        # Reset Button
        self.button_reset = tk.Button(root, text="Reset Game", font=("Arial", 12), command=self.reset_game)
        self.button_reset.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.label_feedback.config(text="Too Low! Try again.", fg="blue")
            elif guess > self.number_to_guess:
                self.label_feedback.config(text="Too High! Try again.", fg="red")
            else:
                self.label_feedback.config(
                    text=f" Correct! You guessed it in {self.attempts} attempts.", fg="green"
                )

            self.label_attempts.config(text=f"Attempts: {self.attempts}")
        except ValueError:
            self.label_feedback.config(text=" Please enter a valid number.", fg="orange")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.label_feedback.config(text="", fg="black")
        self.label_attempts.config(text="Attempts: 0")
        self.entry_guess.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameApp(root)
    root.mainloop()
