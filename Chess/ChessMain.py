import pygame as p
from Chess import ChessEngine

p.init()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
Initialize a global dict of images. Will be called once in the  main
'''


def load_images():
    pieces = ['wp', 'wR', 'wN', 'wK', 'wQ', 'wB', 'bp', 'bR', 'bN', 'bK', 'bQ', 'bB']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+".png"), (SQ_SIZE, SQ_SIZE))


def main(): # Initialization of the Game
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    load_images()
    sqSelected = ()
    playerClicks = []
    validMoves = gs.getPossibleMoves()
    for move in validMoves:
        print(move.getChessNotation())
    moveMade = False
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    print(playerClicks)
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.make_move(move)
                    moveMade = True
                    playerClicks = []
                    sqSelected = ()
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undo_move()
                    moveMade = True
        if moveMade:
            validMoves = gs.getPossibleMoves()
            for move in validMoves:
                print(move.getChessNotation())
            moveMade = False
            gs.print_board()

        clock.tick(MAX_FPS)
        draw_board_state(screen, gs)
        p.display.flip()


def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_board_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)


if __name__ == "__main__":
    main()