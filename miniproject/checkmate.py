def checkmate(board_str):
    board = [row for row in board_str.strip().split('\n')]
    
    try:
        r, c = next((r, c) for r, row in enumerate(board) for c, char in enumerate(row) if char == 'K')
    except StopIteration:
        print("Fail")
        return

    for i, (dr, dc) in enumerate([(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]):
        tr, tc = r + dr, c + dc
        while 0 <= tr < len(board) and 0 <= tc < len(board):
            piece = board[tr][tc]
            if piece != '.':
                if piece == 'Q' or (i < 4 and piece == 'R') or (i >= 4 and piece == 'B'):
                    print("Success")
                    return
                break
            tr, tc = tr + dr, tc + dc

    for dc in [-1, 1]:
        pr, pc = r - 1, c + dc
        if 0 <= pr < len(board) and 0 <= pc < len(board) and board[pr][pc] == 'P':
            print("Success")
            return
            
    print("Fail")