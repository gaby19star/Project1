import tkinter as tk
from tkinter import messagebox

class VoteApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Voting System")
        self.root.geometry("500x300")

        self.john_votes = 0
        self.jane_votes = 0

        self.create_widgets()

    def create_widgets(self):
        self.vote_label = tk.Label(self.root, text="VOTE MENU")
        self.vote_label.pack()

        self.vote_button = tk.Button(self.root, text="Vote", command=self.vote_menu)
        self.vote_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack()

        self.vote_tracker_label = tk.Label(self.root, text="Votes: John - 0 Jane - 0")
        self.vote_tracker_label.pack()

    def vote_menu(self):
        vote_menu_window = tk.Toplevel(self.root)
        vote_menu_window.title("Vote")

        vote_label = tk.Label(vote_menu_window, text="Select a candidate:")
        vote_label.pack()

        john_button = tk.Button(vote_menu_window, text="Vote for John",
                                command=lambda: self.vote_for_candidate(1, vote_menu_window))
        john_button.pack()

        jane_button = tk.Button(vote_menu_window, text="Vote for Jane",
                                command=lambda: self.vote_for_candidate(2, vote_menu_window))
        jane_button.pack()

    def vote_for_candidate(self, candidate_option, vote_menu_window):
        if candidate_option == 1:
            self.john_votes += 1
        elif candidate_option == 2:
            self.jane_votes += 1

        vote_menu_window.destroy()

        self.update_vote_tracker()

    def update_vote_tracker(self):
        tracker_text = f"Votes: John - {self.john_votes}, Jane - {self.jane_votes}"
        self.vote_tracker_label.config(text=tracker_text)

    def run(self):
        self.root.mainloop()

    def display_results(self):
        total_votes = self.john_votes + self.jane_votes
        messagebox.showinfo("Results", f"John: {self.john_votes}\nJane: {self.jane_votes}\nTotal Votes: {total_votes}")
