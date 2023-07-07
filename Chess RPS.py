import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("rock paper scissors CHESS!")
font = pygame.font.SysFont("comic sans", 20)
big_font = pygame.font.SysFont("comic sans", 50)
timer = pygame.time.Clock()
fps = 60

white_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook",
                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
white_location  = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                   (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)] 
black_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook",
                "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
black_location  = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                   (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)] 

captured_black_pieces=[]
captured_white_pieces=[]

turn_step = 0
selection = 100
valid_moves = []

black_king = pygame.image.load("White_King.png")
black_king = pygame.transform.scale(black_king, (80,80))
black_king_small = pygame.transform.scale(black_king, (45,45))
black_queen = pygame.image.load("White_Queen.png")
black_queen = pygame.transform.scale(black_queen, (80,80))
black_queen_small = pygame.transform.scale(black_queen, (45,45))
black_rook = pygame.image.load("White_Rook.png")
black_rook = pygame.transform.scale(black_rook, (80,80))
black_rook_small = pygame.transform.scale(black_rook, (45,45))
black_bishop = pygame.image.load("White_Bishop.png")
black_bishop = pygame.transform.scale(black_bishop, (80,80))
black_bishop_small = pygame.transform.scale(black_bishop, (45,45))
black_knight = pygame.image.load("White_Knight.png")
black_knight = pygame.transform.scale(black_knight, (80,80))
black_knight_small = pygame.transform.scale(black_knight, (45,45))
black_pawn = pygame.image.load("White_Pawn.png")
black_pawn = pygame.transform.scale(black_pawn, (80,80))
black_pawn_small = pygame.transform.scale(black_pawn, (45,45))
white_king = pygame.image.load("Black_King.png")
white_king = pygame.transform.scale(white_king, (80,80))
white_king_small = pygame.transform.scale(white_king, (45,45))
white_queen = pygame.image.load("Black_Queen.png")
white_queen = pygame.transform.scale(white_queen, (80,80))
white_queen_small = pygame.transform.scale(white_queen, (45,45))
white_rook = pygame.image.load("Black_Rook.png")
white_rook = pygame.transform.scale(white_rook, (80,80))
white_rook_small = pygame.transform.scale(white_rook, (45,45))
white_bishop = pygame.image.load("Black_Bishop.png")
white_bishop = pygame.transform.scale(white_bishop, (80,80))
white_bishop_small = pygame.transform.scale(white_bishop, (45,45))
white_knight = pygame.image.load("Black_Knight.png")
white_knight = pygame.transform.scale(white_knight, (80,80))
white_knight_small = pygame.transform.scale (white_knight, (45,45))
white_pawn = pygame.image.load("Black_Pawn.png")
white_pawn = pygame.transform.scale(white_pawn, (65,65))
white_pawn_small = pygame.transform.scale(white_pawn, (45,45))

white_images = [white_rook, white_king, white_queen, white_knight, white_bishop, white_pawn]
white_images_small = [white_rook_small, white_king_small, white_queen_small, white_knight_small, white_bishop_small, white_pawn_small]
black_images = [black_rook, black_king, black_queen, black_knight, black_bishop, black_pawn]
black_images_small = [black_rook_small, black_king_small, black_queen_small, black_knight_small, black_bishop_small, black_pawn_small]

piece_list = ["rook", "king", "queen", "knight", "bishop", "pawn"]

def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if (row % 2 == 0):
            pygame.draw.rect(screen, "light gray", [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, "light gray", [700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, "dark gray", [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, "black", [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, "black", [800, 0, 200, HEIGHT], 5)
        status_text = ["WHITE, SELECT A PIECE!", "WHITE, SELECT A MOVE!",
                       "BLACK, SELECT A PIECE!", "BLACK, SELECT A MOVE!"]
        screen.blit(big_font.render(status_text[turn_step], True, "Black"), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, "black", (0, 100 * i), (800, 100 * i))
            pygame.draw.line(screen, "black", (100 * i, 0), (100 * i, 800))

def draw_pieces():
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == "pawn":
            screen.blit(black_pawn, (black_location[i][0] * 100 + 10, black_location[i][1] * 100 + 15))
        else:
            screen.blit(black_images[index], (black_location[i][0] * 100 + 10, black_location[i][1] * 100 + 10))
    
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, "red", [black_location[i][0] * 100 + 1, black_location[i][1] * 100 + 1,
                                 100, 100], 2)
    
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == "pawn":
            screen.blit(white_pawn, (white_location[i][0] * 100 + 22, white_location[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_location[i][0] * 100 + 10, white_location[i][1] * 100 + 10))
        
        if turn_step >= 2:    
            if selection == i:
                pygame.draw.rect(screen, "blue", [white_location[i][0] * 100 + 1, white_location[i][1] * 100 + 1,
                                 100, 100], 2)

def check_options():
    pass

run = True
while run:
    timer.tick(fps)
    screen.fill("dark gray")

    draw_board()
    draw_pieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_location:
                    selection = black_location.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    black_location[selection] = click_coords
                    if click_coords in white_location:
                        white_piece = white_location.index(click_coords)
                        captured_black_pieces.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(black_piece)
                        white_location.pop(black_piece)
                    white_options = check_options(white_pieces, white_location, 'white')
                    black_options = check_options(black_pieces, black_location, 'black')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'dark'
                if click_coords in white_location:
                    selection = white_location.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    white_location[selection] = click_coords
                    if click_coords in black_location:
                        black_piece = black_location.index(click_coords)
                        captured_white_pieces.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_location.pop(black_piece)
                    white_options = check_option(white_pieces, white_location, 'white')
                    black_options = check_option(black_pieces, black_location, 'black')
                    turn_step = 0
                    selection = 100
                    valid_moves = []


    pygame.display.flip()
pygame.quit()