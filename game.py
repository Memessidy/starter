import tkinter as tk
import random


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    if player_choice == "rock" and computer_choice == "scissors":
        return "player"
    elif player_choice == "scissors" and computer_choice == "paper":
        return "player"
    elif player_choice == "paper" and computer_choice == "rock":
        return "player"
    elif player_choice == computer_choice:
        return "tie"
    else:
        return "computer"


def update_result_text(result, result_text):
    result_text.set("Result: " + result)


def handle_button_click(player_choice, result_rext):
    computer_choice = get_computer_choice()
    winner = determine_winner(player_choice, computer_choice)
    if winner == "player":
        update_result_text("You win!", result_rext)
    elif winner == "computer":
        update_result_text("Computer wins!", result_rext)
    else:
        update_result_text("It's a tie!", result_rext)


def game():
    root = tk.Tk()
    root.title("Rock Paper Scissors")

    # Create the result label
    result_text = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_text)

    # Create the choice buttons
    rock_button = tk.Button(root, text="Rock", command=lambda: handle_button_click("rock", result_text))
    paper_button = tk.Button(root, text="Paper", command=lambda: handle_button_click("paper", result_text))
    scissors_button = tk.Button(root, text="Scissors", command=lambda: handle_button_click("scissors", result_text))

    # Pack the widgets
    rock_button.pack(side="left", padx=10)
    paper_button.pack(side="left", padx=10)
    scissors_button.pack(side="left", padx=10)
    result_label.pack(side="bottom", pady=10)

    # Start the main loop
    root.mainloop()


if __name__ == '__main__':
    game()
