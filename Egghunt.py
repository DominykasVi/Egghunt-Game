# Create classes
class egg_class:
    #Class initiation
    def __init__(self, egg_position):
        self.postion = egg_position
        self.dictionary = {}
        self.guesses = []
        self.create_dictionary()
        self.assign_egg()
    #Creates dictionary with which the program can know the egg positon
    def create_dictionary(self):
        for i in range(1,13):
            self.dictionary[i] = 0
    #The position in which the egg will be placed will be marked 1 instead of 0, this function places ir
    def assign_egg(self):
        self.dictionary[self.postion] = 1
    #Counts player guesses
    def add_guess(self, guess):
        self.guesses.append(guess)
        
class game_board:
    #Class initiation
    def __init__(self):
        self.board = {}
        self.create_board()
    #Creates the board which player will see
    def create_board(self):
        for i in range(1,13):
            self.board[i] = i
    #Prints the board
    def print_board(self):
        print("#####################")
        for i in range(1,13):
            print(self.board[i], end =" ")
            if i%4==0:
                print()
    #Marks bad guesses
    def enter_guess(self, position):    
        self.board[position] = "x"
        
#Creates functions
def select_location(board):
    #lets the player choose egg position, runs while a valid position is chosen
    temp = True
    board.print_board()
    while temp:
        try:
            egg_position = int(input("Please enter egg position number from the board: "))
            if egg_position < 1 or egg_position > 12:
                print("Please enter a valid option")
            else:
                print("The egg is placed")
                temp = False
        except:
            print("Please enter a number")
    return egg_position

#Calculates the difference between player guess and the egg location, helps to find the egg more easily
def difference(egg, guess):
    #Finds where to egg is placed
    for k, v in egg.dictionary.items():
        if v == 1:
            correct_key = k
    #Calculates new difference, it may be a negative, in that case reverses it
    new_dif = correct_key - guess
    if new_dif < 0:
        new_dif = 0 - new_dif
        return new_dif
    else:
        return new_dif
# Calculates difference between guesses
def calculate_difference(old_dif, new_dif):
    if old_dif ==0:
        pass
    elif new_dif<=old_dif:
        print("Getting closer")
    else:
        print("Getting further")
#Game play function
def play_game(egg, board):
    temp = True
    # Runs until players guesses right, executes mentioned functions
    while temp:
        try:
            board.print_board()
            guess = int(input("Guess the location of the egg: "))
            if egg.dictionary[guess] == 1:
                print("You won!\nCongratulations!!! ")
                print("It took you", len(egg.guesses), "guesses to find the egg")
                print("Wrong guesses:", sorted(egg.guesses))
                temp = False
            else:
                if len(egg.guesses) == 0:
                    old_dif = 0
                board.enter_guess(guess)
                egg.add_guess(guess)
                new_dif = difference(egg, guess)
                calculate_difference(old_dif, new_dif)
                old_dif = new_dif
        except:
            print("Please enter a number")  
#Prints the rules     
def print_rules():
    print("Hi, this is an egghunt game.\nThe egg is hidden in one of the 12 positions, you have to guess where the egg is placed.\n"
          "You can choose to either to place the egg in a position yourself or have it assigned automatically\n"
          "After each guess, if it is not correct, an x will be placed in the position you guessed\n"
          "Good luck!")

#Run time
print_rules()
print("#####################")
greeting_message = "Do you want to hide the egg?(Y/N): "
temp = True
while temp:
    choice = input(greeting_message)
    #Executes if the players wants to place the egg manually
    if choice.lower() == "y":
        #Creates board class object:
        board = game_board()
        #Creates egg class object:
        egg = egg_class(select_location(board))
        play_game(egg, board)
        temp = False
    #Executes if the player wants randomly placed egg, works the same as above, only assigns egg to a random position
    elif choice.lower() == "n":
        board = game_board()
        from random import randint
        egg = egg_class(randint(1, 12))
        play_game(egg, board)
        temp = False
    else:
        print("Please enter a valid option")
    