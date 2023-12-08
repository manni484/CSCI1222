# CCSI 1222 Project
# Gambling Game

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import random
import os
import time

def main():
    # Create game GUI program
    game = Game()

    # Start the GUI event loop
    game.game_tick()
    game.window.mainloop()


class Game:

    def __init__(self):
        
        ### WINDOW SET UP ###
        self.window = tk.Tk()
        self.window.title("Gambling Game")
        #self.window.iconbitmap('C:\Homework\Final Project\iconver2(1).ico')
        #self.window.iconbitmap('iconver2(1).ico')
        self.window.geometry("400x300") # Set window lenth and height
        self.window.configure(bg='#A6D8D4') # Set window background
        self.window.grid_columnconfigure(0, weight=1) # Centers row 0 items --> everything that is aligned with grid
        
        ### LABEL SET UP ###
        self.player_money_label = None # From textbook on how to initiate tkinter gui
        self.game_update_label = None
        
        ### PLAYER SET UP ###
        self.player_data = {"money":80, "times_played":0, "game_updates":0} #player data for saves
        
        # Pulls data from dictionary and into variables #
        self.player_money_amount = self.player_data["money"] # Starting money amount. game_tick will be called on start up raising starting money to 100
        self.player_times_played = self.player_data["times_played"] # User statistics for times played the lottery
        self.game_total_updates = self.player_data["game_updates"] # number of game ticks that have happened.
        
        ### CREATE WIDGETS ###
        self.create_widgets() # Create widgets
        

    def create_widgets(self):
        ### SAVE AND OPEN SAVE FILE BUTTONS ###
        self.open_save_button = tk.Button(self.window, text="Open save file", background='#8EAF9D', activebackground='#8EAF9D', relief='flat', border=1, padx=0, pady=0, anchor="nw")
        self.open_save_button.place(relx = 1, anchor = "ne")
        self.open_save_button['command'] = self.save_open
        
        self.save_to_button = tk.Button(self.window, text="Save to file", background='#8EAF9D', activebackground='#8EAF9D', relief='flat', border=1, padx=0, pady=0, anchor="ne")
        self.save_to_button.place(anchor = "nw")
        self.save_to_button['command'] = self.save_save
        
        ### LABELS FOR MONEY AND GAME EVENTS ###
        self.player_money_label = tk.Label(self.window, text=f"You have ${self.player_money_amount}",background='#A6D8D4',anchor='center',pady=40) # the label telling the player how much money they have
        self.player_money_label.configure(foreground='#000000')
        self.player_money_label.grid(row=1,column=0)    

        self.game_update_label = tk.Label(self.window, text="Click one of the buttons to buy a lottery ticket!",background='#A6D8D4') # game events label
        self.game_update_label.grid(row=2, column=0,pady=(2,30))

        ### LOTTERY TICKET BUTTONS ###
        self.lottery_ticket_1_button = tk.Button(self.window, text="Buy a $5 lottery ticket!", background='#D7DAE5', activebackground='#B9CDDA', relief='flat', width='30', border=1) # Button 1
        self.lottery_ticket_1_button.grid(row=3, column=0)
        self.lottery_ticket_1_button['command'] = self.lottery_ticket_1_buy

        self.lottery_ticket_2_button = tk.Button(self.window, text="Buy a $10 lottery ticket!", background='#D7DAE5', activebackground='#B9CDDA', relief='flat', width='30',border=1) # Button 2
        self.lottery_ticket_2_button.grid(row=4, column=0)
        self.lottery_ticket_2_button['command'] = self.lottery_ticket_2_buy
        
        self.lottery_ticket_3_button = tk.Button(self.window, text="Buy a $20 lottery ticket!", background='#D7DAE5', activebackground='#B9CDDA', relief='flat', width='30',border=1) # Button 3
        self.lottery_ticket_3_button.grid(row=5, column=0)
        self.lottery_ticket_3_button['command'] = self.lottery_ticket_3_buy
        
        
    def game_tick(self):
        ### PAY PLAYER ###
        self.game_total_updates +=1
        self.player_money_amount = self.player_money_amount + 20 # Give player $20
        self.player_money_label['text'] = f"You have ${self.player_money_amount}" # Updates label with new money amount
        
        if self.game_total_updates > 1: # Hides the first paycheck so player has time to see instructions on how to play
            self.game_update_label['text'] = "You got your paycheck! +$20!!" # Otherwise tell player they got paid
        
        self.window.after(10000, self.game_tick) # from textbook in timer events, repeats game_tick every 10 seconds


    def select_file(self): # from text book, ask user for file
        my_filetypes = [('text files', '.txt')]
        answer = filedialog.askopenfilename(parent=self.window, initialdir=os.getcwd(), title="Please select or create a file:", filetypes=my_filetypes)
        return answer
    
    def save_open(self): # Opens txt file, reads it, and saves contents to variables
        file_open_save = open(self.select_file())
        user_data = eval(file_open_save.read()) # I did not want to use JSON so this will run the code from the opened text file found https://stackoverflow.com/questions/11026959/writing-a-dict-to-txt-file-and-reading-it-back
        file_open_save.close() # Close file
        
        self.player_data = user_data # set player data to the save file data
        
        ### UPDATE PLAYER VARIABLES TO PLAYER DATA ###
        self.player_money_amount = self.player_data["money"] 
        self.player_times_played = self.player_data["times_played"] 
        self.game_total_updates = self.player_data["game_updates"] 
        
        ### UPDATE LABLES ###
        self.player_money_label['text'] = f"You have ${self.player_money_amount}"
        self.game_update_label['text'] = "Successfully loaded save!"
        
        
    def save_save(self): # Saves player data to a text file.
        file_save_save = open(self.select_file(), 'w') # open file in write mode
        
        ### UPDATE PLAYER DATA TO CURRENT AMOUNTS ###
        self.player_data["money"] = self.player_money_amount 
        self.player_data["times_played"] = self.player_times_played
        self.player_data["game_updates"] = self.game_total_updates
        
        ### WRITE TO TEXT FILE ###
        file_save_save.writelines(str(self.player_data))
        file_save_save.close()
        
        ### UPDATE GAME UPDATE LABEL ###
        self.game_update_label['text'] = "Successfully saved save file!"
        
        
    # function for tickets. Could be optimised further but this works for now.
    def lottery_ticket_1_buy(self):
        if self.player_money_amount >= 5: # Check if player has enought money to play the lottery
            self.player_money_amount = self.player_money_amount - 5 # Subtract ticket cost from players money
            self.player_money_label['text'] = f"You have ${self.player_money_amount}" # Update money label
            self.player_times_played +=1 # update user statistics for times played lottery

            random_chance_1 = random.randint(1,3) # Player has 1 in 3 chance of winning lottery
            random_win_amount = random.randint(1,20) # Amount player can potentially win

            if random_chance_1 == 3: 
                self.player_money_amount = self.player_money_amount + random_win_amount # give player the money they won
                self.player_money_label['text'] = f"You have ${self.player_money_amount}"
                #print(f"You Won ${random_win_amount}! Profit = ${random_win_amount-5}!")
                self.game_update_label['text'] = f"You Won ${random_win_amount}! Profit: +${random_win_amount-5}!"
            else:
                #print(f"You almost won ${random_win_amount} :(") # Tell the player how much the "almost" won to keep them hooked
                self.game_update_label['text'] = f"You almost won ${random_win_amount}!"
        else:
            #print("You dont have enough money to play the lottery :(")
            self.game_update_label['text'] = f"You don't have enough money to play the lottery :("

    def lottery_ticket_2_buy(self): 
            if self.player_money_amount >= 10:# Check if player has enought money to play the lottery
                self.player_money_amount = self.player_money_amount - 10 # Subtract ticket cost from players money
                self.player_money_label['text'] = f"You have ${self.player_money_amount}"
                self.player_times_played +=1 # update user statistics for times played lottery

                random_chance_1 = random.randint(1,4) # Player has 1 in 3 chance of winning lottery
                random_win_amount = random.randint(5,40) # Amount player can potentially win

                if random_chance_1 == 3:
                    self.player_money_amount = self.player_money_amount + random_win_amount # give player the money they won
                    self.player_money_label['text'] = f"You have ${self.player_money_amount}"
                    #print(f"You Won ${random_win_amount}! Profit = ${random_win_amount-10}!")
                    self.game_update_label['text'] = f"You Won ${random_win_amount}! Profit: +${random_win_amount-10}!"
                else:
                    #print(f"You almost won ${random_win_amount} :(") # Tell the player how much the "almost" won to keep them hooked
                    self.game_update_label['text'] = f"You almost won ${random_win_amount}!"
            else:
                #print("You dont have enough money to play the lottery :(")
                self.game_update_label['text'] = f"You don't have enough money to play the lottery :("
                
    def lottery_ticket_3_buy(self): 
                if self.player_money_amount >= 20:# Check if player has enought money to play the lottery
                    self.player_money_amount = self.player_money_amount - 20 # Subtract ticket cost from players money
                    self.player_money_label['text'] = f"You have ${self.player_money_amount}"
                    self.player_times_played +=1 # update user statistics for times played lottery

                    random_chance_1 = random.randint(1,4) # Player has 1 in 3 chance of winning lottery
                    random_win_amount = random.randint(10,60) # Amount player can potentially win

                    if random_chance_1 == 3:
                        self.player_money_amount = self.player_money_amount + random_win_amount # give player the money they won
                        self.player_money_label['text'] = f"You have ${self.player_money_amount}"
                        #print(f"You Won ${random_win_amount}! Profit = ${random_win_amount-10}!")
                        self.game_update_label['text'] = f"You Won ${random_win_amount}! Profit: +${random_win_amount-20}!"
                    else:
                        #print(f"You almost won ${random_win_amount} :(") # Tell the player how much the "almost" won to keep them hooked
                        self.game_update_label['text'] = f"You almost won ${random_win_amount}!"
                else:
                    #print("You dont have enough money to play the lottery :(")
                    self.game_update_label['text'] = f"You don't have enough money to play the lottery :("


if __name__ == "__main__":
    main()
