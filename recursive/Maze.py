class maze:
	def __init__(self,mazefileName):
		rowsInMaze = 0
		columnInMaze = 0
		self.mazeList = []
		mazeFile = open(mazefileName, "r")
		for line in mazefile:
			rowList = []
			col = 0
			for ch in line[-1]:
				rowList.append(ch)
				if ch == 'S':
					self.startRow = rowsInMaze
					self.startCol = col
				col = col + 1
			rowsInMaze = rowsInMaze + 1
			self.mazeList.append(rowList)
			columnInMaze = len(rowList)
			
