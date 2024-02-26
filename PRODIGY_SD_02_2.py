'''
Author : Joelle Kuyula
Guessing Game program.

'''

import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Guessing Game")
        self.geometry("300x150")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(self, text="Guess a number between 1 and 100:", font='arial')
        self.label.pack(pady=5)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)

        self.button = tk.Button(self, text="Submit", bg='red' , font='arial',command=self.check_guess)
        self.button.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get()
        self.clear_text()
        try:
            guess = int(guess)
            self.attempts += 1

            if guess == self.secret_number:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")
                self.reset_game()
            elif guess < self.secret_number:
                messagebox.showinfo("Too Low", "Try guessing higher!")
            else:
                messagebox.showinfo("Too High", "Try guessing lower!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def clear_text(self):
        self.entry.delete(0, 'end')

if __name__ == "__main__":
    pgm = GuessingGame()
    pgm.mainloop()
