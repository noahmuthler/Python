import random

board = [
		["-","-","-"],
		["-","-","-"],
		["-","-","-"]
		]

def printBoard(b):
	for i in b:
		print(i)

def tie(b):
	x = ''
	for i in b:
		for j in i:
			x += j
	if '-' not in x:
		return True
	else:
		return False

def xWinGame(b):
	for i in b:
		if i[0] == "x" and i[1] == "x" and i[2] == "x":
			return True
	row = ""
	for k in b:
		for j in k:
			row+=j
	if (row[0] == 'x' and row[3] == 'x' and row[6] == 'x') or (row[1] == 'x' and row[4] == 'x' and row[7] == 'x') or (row[2] == 'x' and row[5] == 'x' and row[8] == 'x'):
		return True
	elif (row[0] == 'x' and row[4] == 'x' and row[8] == 'x') or (row[2] == 'x' and row[4] == 'x' and row[6] == 'x'):
		return True
	else:
		return False

def oWinGame(b):
	for i in b:
		if i[0] == "o" and i[1] == "o" and i[2] == "o":
			return True
	row = ""
	for k in b:
		for j in k:
			row+=j
	if (row[0] == 'o' and row[3] == 'o' and row[6] == 'o') or (row[1] == 'o' and row[4] == 'o' and row[7] == 'o') or (row[2] == 'o' and row[5] == 'o' and row[8] == 'o'):
		return True
	elif (row[0] == 'o' and row[4] == 'o' and row[8] == 'o') or (row[2] == 'o' and row[4] == 'o' and row[6] == 'o'):
		return True
	else:
		return False

def choiceAndUpdate(b):
	userChoice = int(input("Input which row: "))
	userCol = int(input("Input which column: "))
	b[userChoice-1][userCol-1] = "x"

def emptySpaces(b):
	e = 0
	empty = []
	for i in b:
		for j in i:
			if j == "-":
				empty.append(e)
				e+=1
			else:
				e+=1
	return empty

lst = []

def userGamePoint(b):
	#row
	rowCount=0
	#lst = []
	for i in b:
		if i[0] == "x" and i[1] == "x":
			if((str(rowCount) + "2") not in lst):
				lst.append(str(rowCount) + "2")
				print(lst)
				return str(rowCount) + "2"
		if i[0] == "x" and i[2] == "x":
			if((str(rowCount) + "1") not in lst):
				lst.append(str(rowCount) + "1")
				return str(rowCount) + "1"
		if i[1] == "x" and i[2] == "x":
			if((str(rowCount) + "0") not in lst):
				lst.append(str(rowCount) + "0")
				return str(rowCount) + "0"
		rowCount+=1
	row = ""
	for k in b:
		for j in k:
			row+=j
	#column
	if (row[0] == 'x' and row[3] == 'x'):
		if "20" not in lst:
			lst.append("20")
			return "20"
	elif (row[3] == 'x' and row[6] == 'x'):
		if "00" not in lst:
			lst.append("00")
			return "00"
	elif (row[0] == 'x' and row[6] == 'x'):
		if "10" not in lst:
			lst.append("10")
			return "10"
	elif (row[1] == 'x' and row[4] == 'x'):
		if "21" not in lst:
			lst.append("21")
			return "21"
	elif (row[1] == 'x' and row[7] == 'x'):
		if "11" not in lst:
			lst.append("11")
			return "11"
	elif (row[4] == 'x' and row[7] == 'x'):
		if "01" not in lst:
			lst.append("01")
			return "01"
	elif (row[2] == 'x' and row[5] == 'x'):
		if "22" not in lst:
			lst.append("22")
			return "22"
	elif (row[2] == 'x' and row[8] == 'x'):
		if "12" not in lst:
			lst.append("12")
			return "12"
	elif (row[5] == 'x' and row[8] == 'x'):
		if "02" not in lst:
			lst.append("02")
			return "02"
	#diagonal
	elif (row[0] == 'x' and row[4] == 'x'):
		if "22" not in lst:
			lst.append("22")
			return "22"
	elif (row[0] == 'x' and row[8] == 'x'):
		if "11" not in lst:
			lst.append("11")
			return "11"
	elif (row[4] == 'x' and row[8] == 'x'):
		if "00" not in lst:
			lst.append("00")
			return "00"
	elif (row[2] == 'x' and row[4] == 'x'):
		if "20" not in lst:
			lst.append("20")
			return "20"
	elif (row[2] == 'x' and row[6] == 'x'):
		if "11" not in lst:
			lst.append("11")
			return "11"
	elif (row[4] == 'x' and row[6] == 'x'):
		if "02" not in lst:
			lst.append("02")
			return "02"
	return ''

cLst = []
def computerGamePoint(b):
	#row
	rowCount=0
	print(cLst)
	for i in b:
		if i[0] == "o" and i[1] == "o":
			if((str(rowCount) + "2") not in lst):
				cLst.append(str(rowCount) + "2")
				print(lst)
				return str(rowCount) + "2"
		if i[0] == "o" and i[2] == "o":
			if((str(rowCount) + "1") not in lst):
				cLst.append(str(rowCount) + "1")
				return str(rowCount) + "1"
		if i[1] == "o" and i[2] == "o":
			if((str(rowCount) + "0") not in lst):
				cLst.append(str(rowCount) + "0")
				return str(rowCount) + "0"
		rowCount+=1
	row = ""
	for k in b:
		for j in k:
			row+=j
	#column
	if (row[0] == 'o' and row[3] == 'o'):
		if "20" not in lst:
			cLst.append("20")
			return "20"
	elif (row[3] == 'o' and row[6] == 'o'):
		if "00" not in lst:
			cLst.append("00")
			return "00"
	elif (row[0] == 'o' and row[6] == 'o'):
		if "10" not in lst:
			cLst.append("10")
			return "10"
	elif (row[1] == 'o' and row[4] == 'o'):
		if "21" not in lst:
			cLst.append("21")
			return "21"
	elif (row[1] == 'o' and row[7] == 'o'):
		if "11" not in lst:
			cLst.append("11")
			return "11"
	elif (row[4] == 'o' and row[7] == 'o'):
		if "01" not in lst:
			cLst.append("01")
			return "01"
	elif (row[2] == 'o' and row[5] == 'o'):
		if "22" not in lst:
			cLst.append("22")
			return "22"
	elif (row[2] == 'o' and row[8] == 'o'):
		if "12" not in lst:
			cLst.append("12")
			return "12"
	elif (row[5] == 'o' and row[8] == 'o'):
		if "02" not in lst:
			cLst.append("02")
			return "02"
	#diagonal
	elif (row[0] == 'o' and row[4] == 'o'):
		if "22" not in lst:
			cLst.append("22")
			return "22"
	elif (row[0] == 'o' and row[8] == 'o'):
		if "11" not in lst:
			cLst.append("11")
			return "11"
	elif (row[4] == 'o' and row[8] == 'o'):
		if "00" not in lst:
			cLst.append("00")
			return "00"
	elif (row[2] == 'o' and row[4] == 'o'):
		if "20" not in lst:
			cLst.append("20")
			return "20"
	elif (row[2] == 'o' and row[6] == 'o'):
		if "11" not in lst:
			cLst.append("11")
			return "11"
	elif (row[4] == 'o' and row[6] == 'o'):
		if "02" not in lst:
			cLst.append("02")
			return "02"
	return ''

def computerChoiceAndUpdate(b):
	#gp is game point
	ugp = ""
	ugp = userGamePoint(b)
	cgp = ""
	cpg = computerGamePoint(b)
	print(ugp)
	if ugp == "" and cpg == "":
		emptyList = emptySpaces(b)
		num = random.choice(emptyList)
		if num == 0:
			b[0][0] = "o"
		if num == 1:
			b[0][1] = "o"
		if num == 2:
			b[0][2] = "o"
		if num == 3:
			b[1][0] = "o"
		if num == 4:
			b[1][1] = "o"
		if num == 5:
			b[1][2] = "o"
		if num == 6:
			b[2][0] = "o"
		if num == 7:
			b[2][1] = "o"
		if num == 8:
			b[2][2] = "o"
	elif cpg != "":
		r = int(cpg[0])
		c = int(cpg[1])
		b[r][c] = "o"
	elif ugp != "":
		r = int(ugp[0])
		c = int(ugp[1])
		b[r][c] = "o"

while True:
	print("--------------------")

	if tie(board):
		printBoard(board)
		print("Tie game!")
		break

	if xWinGame(board):
		printBoard(board)
		print("You won!")
		break

	if oWinGame(board):
		printBoard(board)
		print("You lost!")
		break

	printBoard(board)
	choiceAndUpdate(board)
	computerChoiceAndUpdate(board)