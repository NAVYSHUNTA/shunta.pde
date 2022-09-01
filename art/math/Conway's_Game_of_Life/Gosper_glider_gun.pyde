# このコードは、Processingの中にあるPythonモードで実行してください。

def setup():
    global GRID_W, GRID_H, data_set, cell_size, cellList
    size(800, 800)
    GRID_W = GRID_H = 80
    cell_size = width // GRID_W + 1
    data_set = [[0, 0], [0, 1], [1, 0], [1, 1],
                [9, 1],[10, 0], [10, 1], [10, 2], [11, -1], [11, 0], [11, 1], [11, 2], [11, 3], [12, -2], [12, -1], [12, 3], [12, 4],
                [16, 0], [16, 1], [16, 2], [17, 0], [17, 1], [17, 2],
                [19, 3], [20, 2], [20, 4], [21, 1], [21, 5], [22, 2], [22, 3], [22, 4], [23, 0], [23, 1], [23, 5], [23, 6],
                [34, 3], [34, 4], [35, 3], [35, 4]]
    for data in data_set:
        data[0] += GRID_W // 8
        data[1] += GRID_H // 2 + 2
    cellList = getCellList()

def draw():
    global cellList
    frameRate(1000)
    cellList = update(cellList)
    for row_data_set in cellList:
        for cell_data in row_data_set:
            cell_data.printCell()

class Cell:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    def printCell(self):
        if self.state == 1:
            fill(0, 255, 0)
        else:
            fill(0)
        rect(cell_size * self.y, cell_size * self.x, cell_size, cell_size)

    def getNextCell(self):
        cell_cnt = 0
        for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
            try:
                if cellList[self.y + dy][self.x + dx].state == 1:
                    cell_cnt += 1
            except IndexError:
                continue
        if self.state == 1:
            if cell_cnt in [2, 3]:
                return 1
            return 0
        if cell_cnt == 3:
            return 1
        return 0

def getCellList():
    newList = [[] for _ in range(GRID_H)]
    for y in range(GRID_H):
        for x in range(GRID_W):
            if [y, x] in data_set:
                newList[y].append(Cell(x, y, 1))
            else:
                newList[y].append(Cell(x, y, 0))
    return newList

def update(cellList):
    nextList = [[] for _ in range(len(cellList))]
    for y, row_data_set in enumerate(cellList):
        for x, cell_data in enumerate(row_data_set):
            nextList[y].append(Cell(x, y, cell_data.getNextCell()))
    return nextList
