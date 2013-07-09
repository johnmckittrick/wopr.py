import os
import random

class TicTacToe:
	players = 0
	movesmade = 0

	def printboard(self, moves):
		if os.name == "nt":
			os.system("cls")
		else:
			os.system("clear")

		board = "         |         |\n"
		board += "    %s    |    %s    |   %s\n" % (moves[0], moves[1], moves[2])
		board += "         |         |         \n"
		board += "----1----|----2----|----3----\n"
		board += "         |         |\n"
		board += "    %s    |    %s    |   %s\n" % (moves[3], moves[4], moves[5])
		board += "         |         |\n"
		board += "----4----|----5----|----6----\n"
		board += "         |         |\n"
		board += "    %s    |    %s    |   %s\n" % (moves[6], moves[7], moves[8])
		board += "         |         |\n"
		board += "    7         8         9\n"
		print(board)

	def getplayers(self):
		players = input("No. of players: ")

	def makehumanmove(self, playerno, squareno, moves):
		pos = squareno - 1
		self.movesmade += 1
		if (moves[pos] == " "):
			if (playerno == 1):
				moves[pos] = "X"
			else:
				moves[pos] = "O"			

	def getrandomnumber(self, initpos):
		newpos = initpos
		while (newpos == initpos):
			newpos = random.sample([0,1,2,3,4,5,6,7,8], 1)[0]
		return newpos

	def makecomputermove(self, moves):
		if (self.movesmade == 1):
			if (moves[4] == " "):
				moves[4] = "O"
				self.movesmade += 1
			elif (moves[0] == "X"):
				moves[self.getrandomnumber(0)] = "O"
				self.movesmade += 1
			elif (moves[2] == "X"):
				moves[self.getrandomnumber(2)] = "O"
				self.movesmade += 1
			elif (moves[4] == "X"):
				moves[self.getrandomnumber(4)] = "O"
				self.movesmade += 1
			else:
				moves[self.getrandomnumber(moves.index("X"))] = "O"
				self.movesmade += 1
		elif (self.movesmade == 3):
			if ((moves[4] == moves[8] == "X") and (moves[0] == " ")):
				moves[0] = "O"
				self.movesmade += 1
			elif ((moves[0] == moves[2] == "X") and (moves[1] == " ")):
				moves[1] = "O"
				self.movesmade += 1
			elif ((moves[4] == moves[8] == "X") and (moves[2] == " ")):
				moves[2] = "O"
				self.movesmade += 1
			elif ((moves[0] == moves[6] == "X") and (moves[3] == " ")):
				moves[3] = "O"
				self.movesmade += 1
			elif ((moves[0] == moves[8] == "X") and (moves[4] == " ")):
				moves[4] = "O"
				self.movesmade += 1
			elif ((moves[2] == moves[8] == "X") and (moves[5] == " ")):
				moves[5] = "O"
				self.movesmade += 1
			elif ((moves[6] == moves[8] == "X") and (moves[7] == " ")):
				moves[7] = "O"
				self.movesmade += 1
			elif ((moves[0] == moves[4] == "X") and (moves[8] == " ")):
				moves[8] = "O"
				self.movesmade += 1
			else:
				for i in range (0, 8):
					if (moves[i] == " "):
						moves[i] = "O"
						self.movesmade += 1
						break
		elif (self.movesmade == 7):
			if ((moves[6] == moves[8] == "X") and (moves[7] == " ")):
				moves[7] = "0"
				self.movesmade += 1
		else:
			for i in range (0, 8):
				if (moves[i] == " "):
					moves[i] = "O"
					self.movesmade += 1
					break

	def checkforwinner(self, moves):
		if ((moves[0] == moves[1] == moves[2]) and moves[0] != " "):
			return 1
		elif ((moves[0] == moves[3] == moves[6]) and moves[0] != " "):
			return 1
		elif ((moves[0] == moves[4] == moves[8]) and moves[0] != " "):
			return 1
		elif ((moves[1] == moves[4] == moves[7]) and moves[1] != " "):
			return 1
		elif ((moves[2] == moves[5] == moves[8]) and moves[2] != " "):
			return 1
		elif ((moves[2] == moves[4] == moves[6]) and moves[2] != " "):
			return 1
		elif ((moves[3] == moves[4] == moves[5]) and moves[3] != " "):
			return 1
		elif ((moves[6] == moves[7] == moves[8]) and moves[6] != " "):
			return 1
		else:
			return 0

if __name__ == "__main__":
	TicTacToe = TicTacToe()

	playagain = "y"

	while playagain != "n":
		moves = [" "] * 9
		winner = 0
		
		TicTacToe.printboard(moves)
		TicTacToe.getplayers()
	
		while not winner:
			squarepos = input("Select square: ")
			TicTacToe.makehumanmove(1, int(squarepos), moves)
			if (TicTacToe.checkforwinner(moves) == 1):
				TicTacToe.printboard(moves)
				winner = 1
				pass
			else:
				TicTacToe.makecomputermove(moves)
				TicTacToe.printboard(moves)
				if (TicTacToe.checkforwinner(moves) == 1):
					winner = 1
					pass
				else:
					TicTacToe.printboard(moves)
		
		playagain = input("Would you like to play again (Y/N): ")		
		