import os

class Tic_Tac_Toe:

    def __init__(self):
        self.Player_A = ""
        self.Player_B = ""
        self.board = [1,2,3,4,5,6,7,8,9]

    def User_Input(self):

        self.Player_A = input("Enter Your Choice \n'X' or 'O' = ").upper()

        if self.Player_A == "X" or self.Player_A == "x":
            self.Player_B = "O"
            print(f"Then Player B is {self.Player_B}")

        elif self.Player_A == "O" or self.Player_A == "o":
            self.Player_B = "X"
            print(f"Then Player B is {self.Player_B}")

        else:
            print("Enter A Valid Choice As per The Instruction")
            self.User_Input()

def Game_Board(self):

    print("------------------------------------")
    print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
    print("------------------------------------")
    print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
    print("------------------------------------")
    print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
    print("------------------------------------")


    def Game_Logic(self):

        self.board
        print("Use the num-pad to play the game ✌️")

        self.Player_A = int(input("Enter Your Choice From 1 to 9 = "))
        # if self.Player_A


    def Play_Game(self):

        self.User_Input()
        self.Game_Board()
        self.Game_Logic()

Game = Tic_Tac_Toe()
Game.self.Play_Game()