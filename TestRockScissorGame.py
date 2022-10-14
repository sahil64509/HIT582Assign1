import unittest
from enum import IntEnum

from MainGame import MainGame


class Input(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3


# @patch('builtins.print')
class UnitTestMainGame(unittest.TestCase):

    def test_unitTestPaperWinsAgnstRock(self):
        # rock[0], paper[1], scissors[2]
        mainGame = MainGame()
        user_action = 2
        computer_action = 1
        mainGame.compareChoices(user_action, computer_action, 'paper', 'Rock')
        assert mainGame.playerWins == 1

    def test_unitTestRockWinsAgainstScissor(self):
        mainGame = MainGame()
        user_action = 1
        computer_action = 3
        mainGame.compareChoices(user_action, computer_action, 'Rock', 'scissor')
        assert mainGame.playerWins == 1

    def test_unitTestScissorWinsAgainstPaper(self):
        mainGame = MainGame()
        user_action = 3
        computer_action = 2
        mainGame.compareChoices(user_action, computer_action, 'scissor', 'paper')
        assert mainGame.playerWins == 1

    def test_unitTestComputerRandomlyPicksOptions(self):
        # breakpoint()
        mainGame = MainGame()
        assert (mainGame.takeComputerInput() != '') == True

    def testWinnerGetsOnePoint(self):
        mainGame = MainGame()
        user_action = 3
        computer_action = 2
        mainGame.compareChoices(user_action, computer_action, 'scissor', 'paper')
        assert mainGame.playerWins == 1
        assert mainGame.computerWins == 0

    def testGameWinsWithFivePoints(self):
        mainGame = MainGame()
        mainGame.playerWins = 4
        mainGame.computerWins = 0
        assert mainGame.doAnyWinTheGame() != True

        mainGame.playerWins = 5
        assert mainGame.doAnyWinTheGame() != False


if __name__ == "__main__":
    unittest.main()
