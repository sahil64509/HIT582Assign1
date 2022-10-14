# random imported to use the Random function
# that computer uses to pick value randomly
import random


class MainGame:

    def __init__(self):
        self.playerWins = 0
        self.computerWins = 0

    def takeUserAndComputerInputs(self):

        # if p != '':
        #     if 1 > int(p) > 3:
        #         print("Invalid input! Please enter values within 1 to 3")
        # else:
        p = int(input("Enter your choice: "))
        print("Player input is ", p)

        if p == 1:
            playerChoiceName = 'Rock'
        elif p == 2:
            playerChoiceName = 'paper'
        else:
            playerChoiceName = 'scissor'

        print("Player choice is ", playerChoiceName)

        # if computerInput == '':
        computerInput = random.randint(1, 3)

        while computerInput == p:
            computerInput = random.randint(1, 3)

        print("Computer choice is ", computerInput)

        if computerInput == 1:
            computerChoiceName = 'Rock'
        elif computerInput == 2:
            computerChoiceName = 'paper'
        else:
            computerChoiceName = 'scissor'

        print("Computer Choice is: ", computerChoiceName + " " + str(computerInput))
        self.compareChoices(p, computerInput, playerChoiceName, computerChoiceName)

        # self.takeComputerInput(playerChoiceName, p, '')

    def takeComputerInput(self):

        # if computerInput == '':
        computerInput = random.randint(1, 3)

        # while computerInput == playerInput:
        #     computerInput = random.randint(1, 3)

        print("Computer choice is ", computerInput)

        if computerInput == 1:
            computerChoiceName = 'Rock'
        elif computerInput == 2:
            computerChoiceName = 'paper'
        else:
            computerChoiceName = 'scissor'

        print("Computer Choice is: ", computerChoiceName + " " + str(computerInput))
        # self.compareChoices(playerInput, computerInput, playerChoiceName, computerChoiceName)

    def compareChoices(self, p, c, playerChoiceName, computerChoiceName):

        # global playerWins, computerWins
        # print("fefefef")
        print(playerChoiceName + "  " + str(p) + " V/s " + computerChoiceName + " " + str(c))
        # we need to check of a draw
        if p == c:
            print("Draw=> ", end="")
            result = "Draw"

        # condition for winning
        if ((p == 1 and c == 2) or
                (p == 2 and c == 1)):
            print("paper wins => ", end="")
            result = "paper"

        elif ((p == 1 and c == 3) or
              (p == 3 and c == 1)):
            print("** Rock wins this round **", end="")
            result = "Rock"

        elif ((p == 2 and c == 3) or
              (p == 3 and c == 2)):
            print("** Scissor wins this round **", end="")
            result = "scissor"
        # Printing who wins or draw
        if result == "Draw":
            print("!!!! Its a tie !!!!")

        if result == playerChoiceName:
            self.playerWins = self.playerWins + 1
            print("**** Player wins this round *****", self.playerWins)
        else:
            self.computerWins = self.computerWins + 1
            print("**** Computer wins this round ****", self.computerWins)
        # self.playGame()
        # if playerWins >= 5 or computerWins >= 5:
        #     if playerWins >= 5:
        #         print("**** Player wins this game ****")
        #     elif computerWins >= 5:
        #         print("**** Computer wins this game ****")
        #
        #     print("Do you want to Quit(Q) or Restart(R) the game? "
        #           "Please enter Q/R !")
        #     ansMain = input().casefold()
        #
        #     if ansMain == 'q':
        #         print("Thanks for playing")
        #     else:
        #         playerWins = 0
        #         computerWins = 0
        #
        # elif playerWins < 5 and computerWins < 5:
        #     print("Do you want to play again? (Y/N)")
        #     ansSub = input().casefold()
        #     if ansSub != 'y':
        #         print("Thanks for playing")
        #     else:
        #         self.takeUserInputs('')

    def playGame(self):
        print("inside playGame")

        while self.playerWins < 5 and self.computerWins < 5:

            self.takeUserAndComputerInputs()
            if self.playerWins >= 5 or self.computerWins >= 5:
                break
            print("Do you want to play again? (Y/N)")
            ansSub = input().casefold()
            if ansSub != 'y':
                print("Thanks for playing")
                break

        if self.playerWins >= 5 or self.computerWins >= 5:
            if self.playerWins >= 5:
                print("**** Player wins this game ****")
            elif self.computerWins >= 5:
                print("**** Computer wins this game ****")

            print("Do you want to Quit(Q) or Restart(R) the game? "
                  "Please enter Q/R !")
            ansMain = input().casefold()

            if ansMain != 'r':
                print("Thanks for playing..You are now quitting")
                exit()
            else:
                self.playerWins = 0
                self.computerWins = 0
                self.playGame()

    def doAnyWinTheGame(self):
        # return true is the player beats the computer
        # winning conditions: r > s, s > p, p > r
        if self.playerWins >= 5 or self.computerWins >= 5:
            return True
        return False


if __name__ == '__main__':
    object1 = MainGame()
    object1.playGame()
