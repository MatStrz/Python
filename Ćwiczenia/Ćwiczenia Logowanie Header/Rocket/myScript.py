from classRocket import RocketBoard
from classRocket import Rocket


board = RocketBoard(5)
board2 = RocketBoard()


print(RocketBoard.measure_distance(board[2], board[0]))


for rocket in board:
    print(rocket.Id)
