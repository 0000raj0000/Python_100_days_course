import random

class Game:
    """ "Rock Paper and Scissors Game"""

    def __init__(self):
        self.choice = None
        self.rock = """
                _______
            ---'   ____)
m                (_____)
                 (_____)
                  (____)
            ---.__(___)
            """
        self.paper = """
                _______
            ---'    ____)____
                    ______)
                    _______)
                    _______)
            ---.__________)
            """

        self.scissors = """
                _______
            ---'   ____)____
                      ______)
                  __________)
                  (____)
            ---.__(___)
            """

        self.graphics = [self.rock, self.paper, self.scissors]
        self.com_choice = None
        self.get_choice()
        self.computer_choice()
        self.winlist = [[0,2], [2,1], [1,0]]
        self.result()

    def get_choice(self):
        while True:
            try:
                self.choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scrissors.\n"))
            except ValueError:
                print("Wrong Value! try again")
            else:
                print(self.graphics[int(self.choice)])
                break

    def computer_choice(self):
        self.com_choice = random.randint(0, 2)
        print("Computer chose:\n", self.graphics[self.com_choice])
    
    def result(self):
        if [self.choice, self.com_choice] in self.winlist:
            print("\n You Win")
        elif self.choice == self.com_choice:
            print("It's a draw")
        else:
            print("you lost")

if __name__ == "__main__":
    game1 = Game()