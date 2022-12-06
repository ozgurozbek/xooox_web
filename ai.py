# AI is ALWAYS 1, PLAYER is ALWAYS 2
starter = [1,1,2,3,3,3,5,3,3,3,3,3,1]
experienced = [1,1,2,4,4,4,5,5,5,5,3,3,1]
master = [1,1,2,4,4,5,9,11,9,7,5,3,1]
computer = [1,1,3,11,17,15,13,11,9,7,5,3,1]


def runMinimax(board, depthInc, diffSlc, depthSlc):
    """Runs Minimax with the input button, returns index from board array. Board defines
    the game board. DepthInc is for depth increase, to keep track of AI Turns. Slc values
    are player selected values. diffSlc is for difficulty (1-2-3) and depthSlc is for
    ai depth advancements (starter, experienced, master, computer)."""
    difficulty = diffSlc

    if depthSlc == 4:
        instanceDepth = computer
    elif depthSlc == 3:
        instanceDepth = master
    elif depthSlc == 2:
        instanceDepth = experienced
    else:
        instanceDepth = starter

    def countPoints(value):
        score = 0

        #region Easy, Grade Board
        if (difficulty >= 1):
            score += 3 if board[0] == value else 0
            score += 2 if board[1] == value else 0
            score += 6 if board[2] == value else 0
            score += 2 if board[3] == value else 0
            score += 3 if board[4] == value else 0

            score += 2 if board[5] == value else 0
            score += 4 if board[6] == value else 0
            score += 4 if board[7] == value else 0
            score += 4 if board[8] == value else 0
            score += 2 if board[9] == value else 0

            score += 6 if board[10] == value else 0
            score += 4 if board[11] == value else 0
            score += 12 if board[12] == value else 0
            score += 4 if board[13] == value else 0
            score += 6 if board[14] == value else 0

            score += 2 if board[15] == value else 0
            score += 4 if board[16] == value else 0
            score += 4 if board[17] == value else 0
            score += 4 if board[18] == value else 0
            score += 2 if board[19] == value else 0

            score += 3 if board[20] == value else 0
            score += 2 if board[21] == value else 0
            score += 6 if board[22] == value else 0
            score += 2 if board[23] == value else 0
            score += 3 if board[24] == value else 0
        #endregion

        #region Medium, Make Combo
        if (difficulty >= 2):
            score += 2 if (len(set([board[0],board[5],board[10],value]))==1) else 0
            score += 2 if (len(set([board[1],board[6],board[11],value]))==1) else 0
            score += 4 if (len(set([board[2],board[7],board[12],value]))==1) else 0
            score += 2 if (len(set([board[3],board[8],board[13],value]))==1) else 0
            score += 2 if (len(set([board[4],board[9],board[14],value]))==1) else 0

            score += 2 if (len(set([board[10],board[15],board[20],value]))==1) else 0
            score += 2 if (len(set([board[11],board[16],board[21],value]))==1) else 0
            score += 4 if (len(set([board[12],board[17],board[22],value]))==1) else 0
            score += 2 if (len(set([board[13],board[18],board[23],value]))==1) else 0
            score += 2 if (len(set([board[14],board[19],board[24],value]))==1) else 0

            score += 2 if (len(set([board[0],board[1],board[2],value]))==1) else 0
            score += 2 if (len(set([board[5],board[6],board[7],value]))==1) else 0
            score += 4 if (len(set([board[10],board[11],board[12],value]))==1) else 0
            score += 2 if (len(set([board[15],board[16],board[17],value]))==1) else 0
            score += 2 if (len(set([board[20],board[21],board[22],value]))==1) else 0

            score += 2 if (len(set([board[2],board[3],board[4],value]))==1) else 0
            score += 2 if (len(set([board[7],board[8],board[9],value]))==1) else 0
            score += 4 if (len(set([board[12],board[13],board[14],value]))==1) else 0
            score += 2 if (len(set([board[17],board[18],board[19],value]))==1) else 0
            score += 2 if (len(set([board[22],board[23],board[24],value]))==1) else 0

            score += 2 if (len(set([board[0],board[6],board[12],value]))==1) else 0
            score += 2 if (len(set([board[4],board[8],board[12],value]))==1) else 0
            score += 2 if (len(set([board[12],board[16],board[20],value]))==1) else 0
            score += 2 if (len(set([board[12],board[18],board[24],value]))==1) else 0

            score += 2 if (len(set([board[2],board[6],board[10],value]))==1) else 0
            score += 2 if (len(set([board[2],board[8],board[14],value]))==1) else 0
            score += 2 if (len(set([board[10],board[16],board[22],value]))==1) else 0
            score += 2 if (len(set([board[14],board[18],board[22],value]))==1) else 0
        #endregion

        #region Hard, Block Enemy
        if (difficulty >= 3):
            score += 3 if (board[0]==value and board[5]==2 and board[10]==2) else 0
            score += 3 if (board[0]==value and board[6]==2 and board[12]==2) else 0
            score += 3 if (board[0]==value and board[1]==2 and board[2]==2) else 0

            score += 3 if (board[1]==value and board[0]==2 and board[2]==2) else 0
            score += 3 if (board[1]==value and board[6]==2 and board[11]==2) else 0

            score += 3 if (board[2]==value and board[0]==2 and board[2]==2) else 0
            score += 3 if (board[2]==value and board[6]==2 and board[10]==2) else 0
            score += 3 if (board[2]==value and board[7]==2 and board[12]==2) else 0
            score += 3 if (board[2]==value and board[8]==2 and board[14]==2) else 0
            score += 3 if (board[2]==value and board[3]==2 and board[4]==2) else 0

            score += 3 if (board[3]==value and board[2]==2 and board[4]==2) else 0
            score += 3 if (board[3]==value and board[8]==2 and board[13]==2) else 0

            score += 3 if (board[4]==value and board[2]==2 and board[3]==2) else 0
            score += 3 if (board[4]==value and board[8]==2 and board[12]==2) else 0
            score += 3 if (board[4]==value and board[9]==2 and board[14]==2) else 0

            score += 3 if (board[5]==value and board[0]==2 and board[10]==2) else 0
            score += 3 if (board[5]==value and board[6]==2 and board[7]==2) else 0

            score += 3 if (board[6]==value and board[0]==2 and board[12]==2) else 0
            score += 3 if (board[6]==value and board[1]==2 and board[11]==2) else 0
            score += 3 if (board[6]==value and board[2]==2 and board[10]==2) else 0
            score += 3 if (board[6]==value and board[5]==2 and board[7]==2) else 0

            score += 3 if (board[7]==value and board[5]==2 and board[6]==2) else 0
            score += 3 if (board[7]==value and board[2]==2 and board[12]==2) else 0
            score += 3 if (board[7]==value and board[8]==2 and board[9]==2) else 0

            score += 3 if (board[8]==value and board[2]==2 and board[14]==2) else 0
            score += 3 if (board[8]==value and board[3]==2 and board[13]==2) else 0
            score += 3 if (board[8]==value and board[4]==2 and board[12]==2) else 0
            score += 3 if (board[8]==value and board[7]==2 and board[9]==2) else 0

            score += 3 if (board[9]==value and board[4]==2 and board[14]==2) else 0
            score += 3 if (board[9]==value and board[7]==2 and board[8]==2) else 0

            score += 3 if (board[10]==value and board[0]==2 and board[5]==2) else 0
            score += 3 if (board[10]==value and board[2]==2 and board[6]==2) else 0
            score += 3 if (board[10]==value and board[11]==2 and board[12]==2) else 0
            score += 3 if (board[10]==value and board[16]==2 and board[22]==2) else 0
            score += 3 if (board[10]==value and board[15]==2 and board[20]==2) else 0

            score += 3 if (board[11]==value and board[1]==2 and board[6]==2) else 0
            score += 3 if (board[11]==value and board[10]==2 and board[12]==2) else 0
            score += 3 if (board[11]==value and board[16]==2 and board[21]==2) else 0

            score += 3 if (board[12]==value and board[0]==2 and board[6]==2) else 0
            score += 3 if (board[12]==value and board[2]==2 and board[7]==2) else 0
            score += 3 if (board[12]==value and board[4]==2 and board[8]==2) else 0
            score += 3 if (board[12]==value and board[10]==2 and board[11]==2) else 0
            score += 3 if (board[12]==value and board[13]==2 and board[14]==2) else 0
            score += 3 if (board[12]==value and board[16]==2 and board[20]==2) else 0
            score += 3 if (board[12]==value and board[17]==2 and board[22]==2) else 0
            score += 3 if (board[12]==value and board[18]==2 and board[24]==2) else 0

            score += 3 if (board[13]==value and board[12]==2 and board[14]==2) else 0
            score += 3 if (board[13]==value and board[3]==2 and board[8]==2) else 0
            score += 3 if (board[13]==value and board[18]==2 and board[23]==2) else 0

            score += 3 if (board[14]==value and board[2]==2 and board[8]==2) else 0
            score += 3 if (board[14]==value and board[4]==2 and board[9]==2) else 0
            score += 3 if (board[14]==value and board[12]==2 and board[13]==2) else 0
            score += 3 if (board[14]==value and board[18]==2 and board[22]==2) else 0
            score += 3 if (board[14]==value and board[19]==2 and board[24]==2) else 0

            score += 3 if (board[15]==value and board[10]==2 and board[20]==2) else 0
            score += 3 if (board[15]==value and board[16]==2 and board[17]==2) else 0

            score += 3 if (board[16]==value and board[10]==2 and board[22]==2) else 0
            score += 3 if (board[16]==value and board[11]==2 and board[21]==2) else 0
            score += 3 if (board[16]==value and board[12]==2 and board[20]==2) else 0
            score += 3 if (board[16]==value and board[15]==2 and board[17]==2) else 0

            score += 3 if (board[17]==value and board[12]==2 and board[22]==2) else 0
            score += 3 if (board[17]==value and board[15]==2 and board[16]==2) else 0
            score += 3 if (board[17]==value and board[18]==2 and board[19]==2) else 0

            score += 3 if (board[18]==value and board[12]==2 and board[24]==2) else 0
            score += 3 if (board[18]==value and board[13]==2 and board[23]==2) else 0
            score += 3 if (board[18]==value and board[14]==2 and board[22]==2) else 0
            score += 3 if (board[18]==value and board[17]==2 and board[19]==2) else 0

            score += 3 if (board[19]==value and board[14]==2 and board[24]==2) else 0
            score += 3 if (board[19]==value and board[17]==2 and board[18]==2) else 0

            score += 3 if (board[20]==value and board[10]==2 and board[15]==2) else 0
            score += 3 if (board[20]==value and board[12]==2 and board[16]==2) else 0
            score += 3 if (board[20]==value and board[21]==2 and board[22]==2) else 0

            score += 3 if (board[21]==value and board[20]==2 and board[22]==2) else 0
            score += 3 if (board[21]==value and board[11]==2 and board[16]==2) else 0

            score += 3 if (board[22]==value and board[20]==2 and board[21]==2) else 0
            score += 3 if (board[22]==value and board[10]==2 and board[16]==2) else 0
            score += 3 if (board[22]==value and board[12]==2 and board[17]==2) else 0
            score += 3 if (board[22]==value and board[14]==2 and board[18]==2) else 0
            score += 3 if (board[22]==value and board[23]==2 and board[24]==2) else 0

            score += 3 if (board[23]==value and board[13]==2 and board[18]==2) else 0
            score += 3 if (board[23]==value and board[22]==2 and board[24]==2) else 0

            score += 3 if (board[24]==value and board[22]==2 and board[23]==2) else 0
            score += 3 if (board[24]==value and board[12]==2 and board[18]==2) else 0
            score += 3 if (board[24]==value and board[14]==2 and board[19]==2) else 0
        #endregion

        return score

    def workerMinimax(_board, depth, isMaxing, alpha, beta):
        if depth == instanceDepth[depthInc]:
            return countPoints(1)

        if (isMaxing):
            bestScore = -9999
            for i in range(25):
                if _board[i] == 0:
                    _board[i] = 1
                    score = workerMinimax(_board, depth+1, False, alpha, beta)
                    _board[i] = 0
                    if score > bestScore:
                        bestScore = score
                    alpha = max(alpha, bestScore)
                    if beta <= alpha:
                        break
            return bestScore
        else:
            bestScore = 9999
            for i in range(25):
                if _board[i] == 0:
                    _board[i] = 2
                    score = workerMinimax(_board, depth+1, True, alpha, beta)
                    _board[i] = 0
                    if score < bestScore:
                        bestScore = score
                    beta = min(beta, bestScore)
                    if beta <= alpha:
                        break
            return bestScore

    def nextTurn(_board):
        bestScore = -9999
        bestMove = 0
        for i in range(25):
            if _board[i] == 0:
                _board[i] = 1
                score = workerMinimax(_board, 0, False, -9999, 9999)
                _board[i] = 0
                if score > bestScore:
                    bestScore = score
                    bestMove = i
        _board[bestMove] = 1

        return _board

    return nextTurn(board)

def getResult(board):
    pScore, aiScore, pTileCount, aiTileCount = 0,0,0,0

    # Get score
    pScore += 1 if (len(set([board[0],board[5],board[10],2]))==1) else 0
    pScore += 1 if (len(set([board[1],board[6],board[11],2]))==1) else 0
    pScore += 2 if (len(set([board[2],board[7],board[12],2]))==1) else 0
    pScore += 1 if (len(set([board[3],board[8],board[13],2]))==1) else 0
    pScore += 1 if (len(set([board[4],board[9],board[14],2]))==1) else 0

    pScore += 1 if (len(set([board[10],board[15],board[20],2]))==1) else 0
    pScore += 1 if (len(set([board[11],board[16],board[21],2]))==1) else 0
    pScore += 2 if (len(set([board[12],board[17],board[22],2]))==1) else 0
    pScore += 1 if (len(set([board[13],board[18],board[23],2]))==1) else 0
    pScore += 1 if (len(set([board[14],board[19],board[24],2]))==1) else 0

    pScore += 1 if (len(set([board[0],board[1],board[2],2]))==1) else 0
    pScore += 1 if (len(set([board[5],board[6],board[7],2]))==1) else 0
    pScore += 2 if (len(set([board[10],board[11],board[12],2]))==1) else 0
    pScore += 1 if (len(set([board[15],board[16],board[17],2]))==1) else 0
    pScore += 1 if (len(set([board[20],board[21],board[22],2]))==1) else 0

    pScore += 1 if (len(set([board[2],board[3],board[4],2]))==1) else 0
    pScore += 1 if (len(set([board[7],board[8],board[9],2]))==1) else 0
    pScore += 2 if (len(set([board[12],board[13],board[14],2]))==1) else 0
    pScore += 1 if (len(set([board[17],board[18],board[19],2]))==1) else 0
    pScore += 1 if (len(set([board[22],board[23],board[24],2]))==1) else 0

    pScore += 1 if (len(set([board[0],board[6],board[12],2]))==1) else 0
    pScore += 1 if (len(set([board[4],board[8],board[12],2]))==1) else 0
    pScore += 1 if (len(set([board[12],board[16],board[20],2]))==1) else 0
    pScore += 1 if (len(set([board[12],board[18],board[24],2]))==1) else 0

    pScore += 1 if (len(set([board[2],board[6],board[10],2]))==1) else 0
    pScore += 1 if (len(set([board[2],board[8],board[14],2]))==1) else 0
    pScore += 1 if (len(set([board[10],board[16],board[22],2]))==1) else 0
    pScore += 1 if (len(set([board[14],board[18],board[22],2]))==1) else 0

    aiScore += 1 if (len(set([board[0],board[5],board[10],1]))==1) else 0
    aiScore += 1 if (len(set([board[1],board[6],board[11],1]))==1) else 0
    aiScore += 2 if (len(set([board[2],board[7],board[12],1]))==1) else 0
    aiScore += 1 if (len(set([board[3],board[8],board[13],1]))==1) else 0
    aiScore += 1 if (len(set([board[4],board[9],board[14],1]))==1) else 0

    aiScore += 1 if (len(set([board[10],board[15],board[20],1]))==1) else 0
    aiScore += 1 if (len(set([board[11],board[16],board[21],1]))==1) else 0
    aiScore += 2 if (len(set([board[12],board[17],board[22],1]))==1) else 0
    aiScore += 1 if (len(set([board[13],board[18],board[23],1]))==1) else 0
    aiScore += 1 if (len(set([board[14],board[19],board[24],1]))==1) else 0

    aiScore += 1 if (len(set([board[0],board[1],board[2],1]))==1) else 0
    aiScore += 1 if (len(set([board[5],board[6],board[7],1]))==1) else 0
    aiScore += 2 if (len(set([board[10],board[11],board[12],1]))==1) else 0
    aiScore += 1 if (len(set([board[15],board[16],board[17],1]))==1) else 0
    aiScore += 1 if (len(set([board[20],board[21],board[22],1]))==1) else 0

    aiScore += 1 if (len(set([board[2],board[3],board[4],1]))==1) else 0
    aiScore += 1 if (len(set([board[7],board[8],board[9],1]))==1) else 0
    aiScore += 2 if (len(set([board[12],board[13],board[14],1]))==1) else 0
    aiScore += 1 if (len(set([board[17],board[18],board[19],1]))==1) else 0
    aiScore += 1 if (len(set([board[22],board[23],board[24],1]))==1) else 0

    aiScore += 1 if (len(set([board[0],board[6],board[12],1]))==1) else 0
    aiScore += 1 if (len(set([board[4],board[8],board[12],1]))==1) else 0
    aiScore += 1 if (len(set([board[12],board[16],board[20],1]))==1) else 0
    aiScore += 1 if (len(set([board[12],board[18],board[24],1]))==1) else 0

    aiScore += 1 if (len(set([board[2],board[6],board[10],1]))==1) else 0
    aiScore += 1 if (len(set([board[2],board[8],board[14],1]))==1) else 0
    aiScore += 1 if (len(set([board[10],board[16],board[22],1]))==1) else 0
    aiScore += 1 if (len(set([board[14],board[18],board[22],1]))==1) else 0

    # Get tile count
    pTileCount += 3 if (len(set([board[0],board[5],board[10],2]))==1) else 0
    pTileCount += 3 if (len(set([board[1],board[6],board[11],2]))==1) else 0
    pTileCount += 3 if (len(set([board[2],board[7],board[12],2]))==1) else 0
    pTileCount += 3 if (len(set([board[3],board[8],board[13],2]))==1) else 0
    pTileCount += 3 if (len(set([board[4],board[9],board[14],2]))==1) else 0

    pTileCount += 3 if (len(set([board[10],board[15],board[20],2]))==1) else 0
    pTileCount += 3 if (len(set([board[11],board[16],board[21],2]))==1) else 0
    pTileCount += 3 if (len(set([board[12],board[17],board[22],2]))==1) else 0
    pTileCount += 3 if (len(set([board[13],board[18],board[23],2]))==1) else 0
    pTileCount += 3 if (len(set([board[14],board[19],board[24],2]))==1) else 0

    pTileCount += 3 if (len(set([board[0],board[1],board[2],2]))==1) else 0
    pTileCount += 3 if (len(set([board[5],board[6],board[7],2]))==1) else 0
    pTileCount += 3 if (len(set([board[10],board[11],board[12],2]))==1) else 0
    pTileCount += 3 if (len(set([board[15],board[16],board[17],2]))==1) else 0
    pTileCount += 3 if (len(set([board[20],board[21],board[22],2]))==1) else 0

    pTileCount += 3 if (len(set([board[2],board[3],board[4],2]))==1) else 0
    pTileCount += 3 if (len(set([board[7],board[8],board[9],2]))==1) else 0
    pTileCount += 3 if (len(set([board[12],board[13],board[14],2]))==1) else 0
    pTileCount += 3 if (len(set([board[17],board[18],board[19],2]))==1) else 0
    pTileCount += 3 if (len(set([board[22],board[23],board[24],2]))==1) else 0

    pTileCount += 3 if (len(set([board[0],board[6],board[12],2]))==1) else 0
    pTileCount += 3 if (len(set([board[4],board[8],board[12],2]))==1) else 0
    pTileCount += 3 if (len(set([board[12],board[16],board[20],2]))==1) else 0
    pTileCount += 3 if (len(set([board[12],board[18],board[24],2]))==1) else 0

    pTileCount += 3 if (len(set([board[2],board[6],board[10],2]))==1) else 0
    pTileCount += 3 if (len(set([board[2],board[8],board[14],2]))==1) else 0
    pTileCount += 3 if (len(set([board[10],board[16],board[22],2]))==1) else 0
    pTileCount += 3 if (len(set([board[14],board[18],board[22],2]))==1) else 0

    aiTileCount += 3 if (len(set([board[0],board[5],board[10],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[1],board[6],board[11],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[2],board[7],board[12],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[3],board[8],board[13],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[4],board[9],board[14],1]))==1) else 0

    aiTileCount += 3 if (len(set([board[10],board[15],board[20],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[11],board[16],board[21],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[12],board[17],board[22],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[13],board[18],board[23],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[14],board[19],board[24],1]))==1) else 0

    aiTileCount += 3 if (len(set([board[0],board[1],board[2],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[5],board[6],board[7],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[10],board[11],board[12],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[15],board[16],board[17],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[20],board[21],board[22],1]))==1) else 0

    aiTileCount += 3 if (len(set([board[2],board[3],board[4],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[7],board[8],board[9],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[12],board[13],board[14],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[17],board[18],board[19],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[22],board[23],board[24],1]))==1) else 0

    aiTileCount += 3 if (len(set([board[0],board[6],board[12],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[4],board[8],board[12],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[12],board[16],board[20],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[12],board[18],board[24],1]))==1) else 0

    aiTileCount += 3 if (len(set([board[2],board[6],board[10],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[2],board[8],board[14],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[10],board[16],board[22],1]))==1) else 0
    aiTileCount += 3 if (len(set([board[14],board[18],board[22],1]))==1) else 0
    #Get count
    return(pScore, aiScore, pTileCount, aiTileCount)