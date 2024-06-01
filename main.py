import tkinter as tk
from tkinter import messagebox
from get_Players import get_unique_player_groups  # Ensure the correct casing
import random

# Initialize the unique player groups and titles
unique_player_groups, group_titles = get_unique_player_groups()

# Flatten the player groups into a single list and shuffle the order
all_players = [player for group in unique_player_groups for player in group]
random.shuffle(all_players)

class PlayerGridApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basketball Player Groups")
        self.geometry("600x600")

        self.selected_players = set()
        self.correct_selections = set()

        self.create_widgets()

    def create_widgets(self):
        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack(pady=20)

        self.buttons = []
        for i, player in enumerate(all_players):
            btn = tk.Button(self.grid_frame, text=player, width=15, height=2, font=('Helvetica', 10, 'bold'),
                            bg="white", fg="black",
                            command=lambda p=player, b=i: self.select_player(p, b))
            btn.grid(row=i//4, column=i%4, padx=5, pady=5)
            self.buttons.append(btn)

        self.submit_btn = tk.Button(self, text="Submit", command=self.check_selection, state=tk.DISABLED, font=('Helvetica', 12, 'bold'))
        self.submit_btn.pack(pady=10)

        self.group_titles_frame = tk.Frame(self)
        self.group_titles_frame.pack(pady=20)
        for title in group_titles:
            label = tk.Label(self.group_titles_frame, text=title, font=('Helvetica', 12, 'bold'))
            label.pack()

    def select_player(self, player, btn_index):
        if player in self.selected_players:
            self.selected_players.remove(player)
            self.buttons[btn_index].config(bg="white", fg="black", relief=tk.RAISED)
        elif len(self.selected_players) < 4:
            self.selected_players.add(player)
            self.buttons[btn_index].config(bg="lightblue", fg="darkblue", relief=tk.SUNKEN)
        else:
            messagebox.showwarning("Selection Error", "You can only select 4 players at a time.")
            return

        self.update_button_states()

    def update_button_states(self):
        if len(self.selected_players) == 4:
            self.submit_btn.config(state=tk.NORMAL)
        else:
            self.submit_btn.config(state=tk.DISABLED)

    def check_selection(self):
        if len(self.selected_players) != 4:
            messagebox.showwarning("Selection Error", "Please select exactly 4 players.")
            return

        correct = False
        correct_group_title = ""
        for group, title in zip(unique_player_groups, group_titles):
            if all(player in group for player in self.selected_players):
                correct = True
                correct_group_title = title
                self.correct_selections.update(self.selected_players)
                break

        if correct:
            messagebox.showinfo("Success", f"Correct selection! You correctly selected the group: {correct_group_title}")
            for btn in self.buttons:
                if btn.cget("text") in self.selected_players:
                    btn.config(bg="green", fg="green", state="disabled", relief=tk.FLAT)
            self.selected_players.clear()
        else:
            messagebox.showerror("Error", "Incorrect selection, try again.")
            for player in self.selected_players:
                for btn in self.buttons:
                    if btn.cget("text") == player:
                        btn.config(bg="white", fg="black", relief=tk.RAISED)
            self.selected_players.clear()

        self.update_button_states()

if __name__ == "__main__":
    app = PlayerGridApp()
    app.mainloop()



