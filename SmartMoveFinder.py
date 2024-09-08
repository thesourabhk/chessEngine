import random

pieceScore = {"K": 0, "Q":10, "R":5,"B":3, "N":3, "p":1}
CHECKMATE = 1000
STALEMATE = 0

def findRandomMove(validMoves):
    return validMoves[random.randint(0, len(validMoves)-1)]

'''
Find the best move based on material alone.
'''
def findBestMove(gs, validMoves):
    turnMultiplier = 1 if gs.whiteToMove else -1
    opponentMinMaxScore = CHECKMATE
    bestPlayerMove = None
    random.shuffle(validMoves)
    for playerMove in validMoves:
        gs.makeMove(playerMove)
        opponentMoves = gs.getValidMoves()
        opponentMaxScore = -CHECKMATE
        for opponentMove in opponentMoves:
            gs.makeMove(opponentMove)
            if gs.checkmate:
                score = -turnMultiplier * CHECKMATE
            elif gs.stalemate:
                score = STALEMATE
            score = -turnMultiplier* scoreMaterial(gs.board)
            if score > opponentMaxScore:
                opponentMaxScore = score
            gs.undoMove()

        if opponentMaxScore < opponentMinMaxScore:
            opponentMinMaxScore, bestPlayerMove = opponentMaxScore, playerMove
        gs.undoMove()
    return bestPlayerMove


'''
Score the board based on material.
'''
def scoreMaterial(board):
    score = 0
    for row in board:
        for square in row:
            if square[0] == 'w':
                score += pieceScore[square[1]]
            elif square[0] == 'b':
                score -= pieceScore[square[1]]
    return score