# CCSI 1222 Project
# Gambling Game

import tkinter as tk
from tkinter import ttk
import random
import time

def main():
    # Create game GUI program
    game = Game()

    #game.paycheck() # paycheck function

    # Start the GUI event loop
    game.window.mainloop()


class Game:

    def __init__(self):
        self.window = tk.Tk()
        self.player_money_label = None
        self.player_money_amount = 100
        self.create_widgets()

    def create_widgets(self):
        self.player_money_label = ttk.Label(self.window, text=f"You have {self.player_money_amount}")
        self.player_money_label.grid(row=0,column=0)    
        # the label telling the player how much money they have

        lottery_ticket_1_button = ttk.Button(self.window, text="Buy a $5 lottery ticket!")
        lottery_ticket_1_button.grid(row=1, column=0)
        lottery_ticket_1_button['command'] = self.lottery_ticket_1_buy
        # the first button to buy a lottery ticket

        lottery_ticket_2_button = ttk.Button(self.window, text="Buy a $10 lottery ticket!")
        lottery_ticket_2_button.grid(row=2, column=0)
        lottery_ticket_2_button['command'] = self.lottery_ticket_2_buy
        # the first button to buy a lottery ticket


    def lottery_ticket_1_buy(self):
        if self.player_money_amount >= 5:
            self.player_money_amount = self.player_money_amount - 5
            self.player_money_label['text'] = self.player_money_amount

            random_chance_1 = random.randint(1,3) # Player has 1 in 3 chance of winning lottery
            random_win_amount = random.randint(1,20) # Amount player can potentially win

            if random_chance_1 == 3:
                self.player_money_amount = self.player_money_amount + random_win_amount
                self.player_money_label['text'] = self.player_money_amount
                print(f"You Won ${random_win_amount}! Profit = ${random_win_amount-5}!")
            else:
                print(f"You almost won ${random_win_amount} :(") # Tell the player how much the "almost" won to keep them hooked
        else:
            print("You dont have enough money to play the lottery :(")

    def lottery_ticket_2_buy(self):
            if self.player_money_amount >= 10:
                self.player_money_amount = self.player_money_amount - 10
                self.player_money_label['text'] = self.player_money_amount

                random_chance_1 = random.randint(1,4) # Player has 1 in 3 chance of winning lottery
                random_win_amount = random.randint(5,40) # Amount player can potentially win

                if random_chance_1 == 3:
                    self.player_money_amount = self.player_money_amount + random_win_amount
                    self.player_money_label['text'] = self.player_money_amount
                    print(f"You Won ${random_win_amount}! Profit = ${random_win_amount-10}!")
                else:
                    print(f"You almost won ${random_win_amount} :(") # Tell the player how much the "almost" won to keep them hooked
            else:
                print("You dont have enough money to play the lottery :(")
    def paycheck(self):
        self.player_money_amount = self.player_money_amount + 20
        time.sleep(5)
        self.paycheck()
            
if __name__ == "__main__":
    main()