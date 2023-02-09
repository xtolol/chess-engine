class GameState():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []

    def print_board(self):
        for row in self.board:
            print(row)


    def make_move(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove


    def undo_move(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    def getValidMoves(self):
        return self.getPossibleMoves()

    def getRookMoves(self):
        #

    def getPawnmoves(self, row: int, column: int, moves: list):
        color = self.board[row][column][0]
        print(column)
        print("row: "+str(row)+".")
        if self.whiteToMove:
        # Case Black (Guard Clause)
            if color == "w":
                # Case Starting Pawn
                if row == 6:
                    if self.board[row - 1][column] == "--":
                        moves.append(Move((row, column), (row - 1, column), self.board))
                    if self.board[row - 2][column] == "--":
                        moves.append(Move((row, column), (row - 2, column), self.board))
                    if row - 1 >= 0 and column - 1 >= 0:
                        if self.board[row - 1][column - 1] != "--":
                            moves.append(Move((row, column), (row - 1, column - 1), self.board))
                    if row - 1 >= 0 and column + 1 <= 7:
                        if self.board[row - 1][column + 1] != "--":
                            moves.append(Move((row, column), (row - 1, column + 1), self.board))
                else:
                    if self.board[row - 1][column] == "--":
                        moves.append(Move((row, column), (row - 1, column), self.board))
                    if (row - 1) >= 0 and (column - 1) >= 0:
                        if self.board[row - 1][column - 1] != "--":
                            moves.append(Move((row, column), (row - 1, column - 1), self.board))
                    if row - 1 >= 0 and column + 1 <= 7:
                        if self.board[row - 1][column + 1] != "--":
                            moves.append(Move((row, column), (row - 1, column + 1), self.board))

        else:
            if color == "b":
                if row == 1:
                    if self.board[row + 1][column] == "--":
                        moves.append(Move((row, column), (row + 1, column), self.board))
                    if self.board[row + 2][column] == "--":
                        moves.append(Move((row, column), (row + 2, column), self.board))
                    if row + 1 <= 7 and column + 1 <= 7:
                        if self.board[row + 1][column + 1] != "--":
                            moves.append(Move((row, column), (row + 1, column + 1), self.board))
                    if row + 1 <= 7 and column - 1 >= 0:
                        if self.board[row + 1][column - 1] != "--":
                            moves.append(Move((row, column), (row + 1, column - 1), self.board))
                else:
                    if self.board[row + 1][column] == "--":
                        moves.append(Move((row, column), (row + 1, column), self.board))
                    if row + 1 <= 7 and column + 1 <= 7:
                        if self.board[row + 1][column + 1] != "--":
                            moves.append(Move((row, column), (row + 1, column + 1), self.board))
                    if row + 1 <= 7 and column - 1 >= 0:
                        if self.board[row + 1][column - 1] != "--":
                            moves.append(Move((row, column), (row + 1, column - 1), self.board))
        

    def getPossibleMoves(self) -> list:
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if self.whiteToMove or not self.whiteToMove:
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.getPawnmoves(r, c, moves)
        return moves


class Move():
    ranks = {"1": 7,
             "2": 6,
             "3": 5,
             "4": 4,
             "5": 3,
             "6": 2,
             "7": 1,
             "8": 0}
    rows = {v: k for k, v in ranks.items()}

    files = {"a": 0,
             "b": 1,
             "c": 2,
             "d": 3,
             "e": 4,
             "f": 5,
             "g": 6,
             "h": 7}
    cols = {v: k for k, v in files.items()}

    def __init__(self, startSQ, endSQ, board):
        self.startRow = startSQ[0]
        self.startCol = startSQ[1]
        self.endRow = endSQ[0]
        self.endCol = endSQ[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.cols[c] + self.rows[r]


