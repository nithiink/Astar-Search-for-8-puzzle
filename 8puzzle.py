import copy

class State: 
    def __init__(self, board, gval, fval):
        self.board = board
        self.gval = gval
        self.fval = fval
        self.blankX, self.blankY = self.find()

    
    def find(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return i,j

    def canMoveLeft(self):
        self.blankX, self.blankY = self.find()
        if self.blankY == len(self.board[0]) - 1:
            return False
        return True
    
    def canMoveRight(self):
        self.blankX, self.blankY = self.find()
        if self.blankY == 0:
            return False
        return True
    
    def canMoveUp(self):
        self.blankX, self.blankY = self.find()
        if self.blankX == len(self.board) - 1:
            return False
        return True
    
    def canMoveDown(self):
        self.blankX, self.blankY = self.find()
        if self.blankX == 0:
            return False
        return True

    def moveLeft(self):
        self.board[self.blankX][self.blankY] = self.board[self.blankX][self.blankY + 1]
        self.board[self.blankX][self.blankY + 1] = 0
 
    def moveRight(self):
        self.board[self.blankX][self.blankY] = self.board[self.blankX][self.blankY - 1]
        self.board[self.blankX][self.blankY - 1] = 0
 
    def moveUp(self):
        self.board[self.blankX][self.blankY] = self.board[self.blankX + 1][self.blankY]
        self.board[self.blankX + 1][self.blankY] = 0
 
    def moveDown(self):
        self.board[self.blankX][self.blankY] = self.board[self.blankX - 1][self.blankY]
        self.board[self.blankX - 1][self.blankY] = 0

    def printState(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                print(self.board[i][j], end=" ")
            print()


class Puzzle:
    def __init__(self, initial, goal) -> None:
        self.initial = initial
        self.goal = goal
        self.openList = PriorityQueue()
        self.closedList = set()
    
    def findShortestPath(self):
        self.openList.insert(self.initial)

        while self.openList:
            state = self.openList.delete()

            if self.getSetHash(state.board) in self.closedList:
                # print('hi')
                continue

            print("----------------")
            print("Next State:")
            state.printState()
            print(state.fval)

            if self.h(state.board) == 0:
                return

            if state.canMoveUp():
                newState = State(copy.deepcopy(state.board), state.gval + 1, state.fval)
                newState.moveUp()
                self.setf(newState)
                self.openList.insert(newState)

            if state.canMoveDown():
                newState = State(copy.deepcopy(state.board), state.gval + 1, state.fval)
                newState.moveDown()
                self.setf(newState)
                self.openList.insert(newState)

            if state.canMoveLeft():
                newState = State(copy.deepcopy(state.board), state.gval + 1, state.fval)
                newState.moveLeft()
                self.setf(newState)
                self.openList.insert(newState)

            if state.canMoveRight():
                newState = State(copy.deepcopy(state.board), state.gval + 1, state.fval)
                newState.moveRight()
                self.setf(newState)
                self.openList.insert(newState)

            self.closedList.add(self.getSetHash(state.board))

    def getSetHash(self, board):
        hashVal = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                hashVal *= 10
                hashVal += board[i][j]
        return hashVal

    def setf(self, state):    
        state.fval = self.h(state.board) + state.gval
        return state.fval
    
    def h(self, board):
        hVal = -1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != self.goal[i][j]:
                    hVal += 1
        if hVal == -1:
            hVal = 0
        return hVal

class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []
    
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    def isEmpty(self):
        return len(self.queue) == 0
 
    def insert(self, data):
        self.queue.append(data)
 
    def delete(self):
        try:
            min_val = 0
            for i in range(len(self.queue)):
                if self.queue[i].fval < self.queue[min_val].fval:
                    min_val = i
            item = self.queue[min_val]
            del self.queue[min_val]
            return item
        except IndexError:
            print()
            exit()



inputArr = [[1, 2, 3], [7, 0, 4], [8, 6, 5]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
initial = State(inputArr, 0, 0)
puzzle = Puzzle(initial, goal)
puzzle.setf(initial)
puzzle.findShortestPath()
