'''
Write a class called Rock_paper_scissors that implements the logic of the game Rock paper-
scissors. For this game the user plays against the computer for a certain number of rounds.
Your class should have fields for the how many rounds there will be, the current round number,
and the number of wins each player has. There should be methods for getting the computer’s
choice, finding the winner of a round, and checking to see if someone has won the (entire)
game. You may want more methods.
'''
import random
class rock_paper_scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ["rock", "paper", "scissors"]

    def computer(self):
        return random.choice(self.choices)

    def find_winner(self, user, computer):
        if user == computer:
            return "draw"
        elif (user == "rock" and computer == "scissors")or(user == "paper" and computer == "rock")or(user == "scissors" and computer == "paper"):
            self.user_wins += 1
            return "user"
        else:
            self.computer_wins += 1
            return "computer"
        
    def has_winner(self):
        return self.user_wins > self.rounds // 2 or self.computer_wins > self.rounds // 2
    
    def play_game(self):
        print("Welcome to Rock Paper Scissors! Best of", self.rounds ,"rounds.")

        while self.current_round < self.rounds and not self.has_winner():
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            computer_choice = self.computer()
            print("Computer chose: " ,computer_choice)
            winner = self.find_winner(user_choice, computer_choice)

            if winner == "draw":
                print("It's a draw!")
            elif winner == "user":
                print("You win this round!")
            else:
                print("Computer wins this round!")

            self.current_round += 1
            print(f"Score: You {self.user_wins} - {self.computer_wins} Computer\n")

        if self.user_wins > self.computer_wins:
            print("Congratulations! You won the game!")
        elif self.computer_wins > self.user_wins:
            print("Computer wins the game! Better luck next time.")
        else:
            print("It's a tie game!")
game = rock_paper_scissors(int(input("Enter number of rounds: ")))
game.play_game()
