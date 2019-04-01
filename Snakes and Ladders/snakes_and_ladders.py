import pygame
import random
import time


pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
TITLE = "Snakes and Ladders"
done = False
player1_started = False
player2_started = False
dice_rolled = False
dice_value = 0
player1_square = None
player2_square = None
player1_turn = True
player2_turn = False
player1_won = False
player2_won = False
six_rolled = False
font = pygame.font.SysFont("Maiandra GD", 24, bold=True)
font_win = pygame.font.SysFont("Maiandra GD", 100, bold=True)
dice_msg1 = font.render("Press 'SPACE BAR'", True, (0, 0, 255))
dice_msg2 = font.render("to roll the dice!", True, (0, 0, 255))
turn_msg1 = font.render("Player 1's turn!", True, (0, 0, 0))
turn_msg2 = font.render("Player 2's turn!", True, (0, 0, 0))
win_msg1 = font_win.render("PLAYER 1 WON!", True, (0, 255, 0))
win_msg2 = font_win.render("PLAYER 2 WON!", True, (0, 255, 0))
six_msg1 = font.render("You rolled a 6!", True, (0, 255, 0))
six_msg2 = font.render("Roll again!", True, (0, 255, 0))


class Square:
    def __init__(self, p=0, x_coordinate=0, y_coordinate=0):
        self.position = p
        self.snake = None
        self.ladder = None
        self.next = None
        self.x = x_coordinate
        self.y = y_coordinate


class Board:
    def __init__(self):
        self.start = None

    def __getitem__(self, key):
        p = self.start
        for i in range(key - 1):
            p = p.next
        return p

    def insert(self, pos=0, x=0, y=0):
        new_square = Square(pos, x, y)
        if self.start is None:
            self.start = new_square
        else:
            p = self.start
            while p.next:
                p = p.next
            p.next = new_square


# creating an empty board
x = 250
y = 630
pos = 1
board = Board()
for i in range(10):
    if i % 2 == 0:
        for j in range(9):
            board.insert(pos, x, y)
            pos += 1
            x += 70
        board.insert(pos, x, y)
        pos += 1
    else:
        for j in range(9):
            board.insert(pos, x, y)
            pos += 1
            x -= 70
        board.insert(pos, x, y)
        pos += 1
    y -= 70
# adding snakes
board[17].snake = board[7]
board[54].snake = board[34]
board[62].snake = board[18]
board[64].snake = board[60]
board[87].snake = board[36]
board[93].snake = board[73]
board[95].snake = board[75]
board[98].snake = board[79]
# adding ladders
board[4].ladder = board[14]
board[9].ladder = board[39]
board[19].ladder = board[38]
board[21].ladder = board[42]
board[28].ladder = board[84]
board[51].ladder = board[67]
board[72].ladder = board[91]
board[80].ladder = board[99]
# turn
turn = 0
# set up the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
# set the white background
bg = pygame.image.load("bg.png")
# set the board
board_sprite = pygame.image.load("board.png")
# set the dice
dice = pygame.image.load("dice.png")
dice1 = pygame.image.load("dice1.png")
dice2 = pygame.image.load("dice2.png")
dice3 = pygame.image.load("dice3.png")
dice4 = pygame.image.load("dice4.png")
dice5 = pygame.image.load("dice5.png")
dice6 = pygame.image.load("dice6.png")
dice_list = [0, dice1, dice2, dice3, dice4, dice5, dice6]
# set the players
player1 = pygame.image.load("player1.png")
player2 = pygame.image.load("player2.png")
clock = pygame.time.Clock()
while not done:
    time.sleep(1)
    screen.blit(bg, (0, 0))
    screen.blit(board_sprite, (250, 0))
    screen.blit(dice_msg1, (10, 75))
    screen.blit(dice_msg2, (10, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_rolled = True
                dice_value = random.randint(1, 6)
            if turn % 2 == 0:
                if dice_value == 1:
                    six_rolled = False
                    player1_turn = False
                    player2_turn = True
                    if not player1_started:
                        player1_started = True
                        player1_square = board[1]
                    elif player1_square != board[100]:
                        player1_square = board[player1_square.position + 1]
                    turn += 1
                elif dice_value == 2:
                    six_rolled = False
                    player1_turn = False
                    player2_turn = True
                    if player1_started and player1_square.position <= 98:
                        player1_square = board[player1_square.position + 2]
                    turn += 1
                elif dice_value == 3:
                    six_rolled = False
                    player1_turn = False
                    player2_turn = True
                    if player1_started and player1_square.position <= 97:
                        player1_square = board[player1_square.position + 3]
                    turn += 1
                elif dice_value == 4:
                    six_rolled = False
                    player1_turn = False
                    player2_turn = True
                    if player1_started and player1_square.position <= 96:
                        player1_square = board[player1_square.position + 4]
                    turn += 1
                elif dice_value == 5:
                    six_rolled = False
                    player1_turn = False
                    player2_turn = True
                    if player1_started and player1_square.position <= 95:
                        player1_square = board[player1_square.position + 5]
                    turn += 1
                elif dice_value == 6:
                    six_rolled = True
                    if player1_started and player1_square.position <= 94:
                        player1_square = board[player1_square.position + 6]
                if player1_square == board[100]:
                    player1_won = True
            else:
                if dice_value == 1:
                    six_rolled = False
                    player2_turn = False
                    player1_turn = True
                    if not player2_started:
                        player2_started = True
                        player2_square = board[1]
                    elif player2_square != board[100]:
                        player2_square = board[player2_square.position + 1]
                    turn += 1
                elif dice_value == 2:
                    six_rolled = False
                    player2_turn = False
                    player1_turn = True
                    if player2_started and player2_square.position <= 98:
                        player2_square = board[player2_square.position + 2]
                    turn += 1
                elif dice_value == 3:
                    six_rolled = False
                    player2_turn = False
                    player1_turn = True
                    if player2_started and player2_square.position <= 97:
                        player2_square = board[player2_square.position + 3]
                    turn += 1
                elif dice_value == 4:
                    six_rolled = False
                    player2_turn = False
                    player1_turn = True
                    if player2_started and player2_square.position <= 96:
                        player2_square = board[player2_square.position + 4]
                    turn += 1
                elif dice_value == 5:
                    six_rolled = False
                    player2_turn = False
                    player1_turn = True
                    if player2_started and player2_square.position <= 95:
                        player2_square = board[player2_square.position + 5]
                    turn += 1
                elif dice_value == 6:
                    six_rolled = True
                    if player2_started and player2_square.position <= 94:
                        player2_square = board[player2_square.position + 6]
                if player2_square == board[100]:
                    player2_won = True
    if player1_turn:
        screen.blit(turn_msg1, (10, 350))
    if player2_turn:
        screen.blit(turn_msg2, (10, 350))
    if not dice_rolled or dice_value == 0:
        screen.blit(dice, (50, 150))
    else:
        screen.blit(dice_list[dice_value], (75, 150))
    if six_rolled:
        screen.blit(six_msg1, (10, 400))
        screen.blit(six_msg2, (10, 425))
    if not player1_started:
        screen.blit(player1, (50, 500))
        dice_value = 0
    else:
        if player1_square.snake and dice_value != 6:
            player1_square = player1_square.snake
        if player1_square.ladder and dice_value != 6:
            player1_square = player1_square.ladder
        pos_msg1 = font.render("Player_1 : "+str(player1_square.position), True, (0, 0, 0))
        screen.blit(pos_msg1, (960, 200))
        screen.blit(player1, (player1_square.x, player1_square.y))
        dice_value = 0
    if not player2_started:
        screen.blit(player2, (130, 500))
    else:
        if player2_square.snake and dice_value != 6:
            player2_square = player2_square.snake
        if player2_square.ladder and dice_value != 6:
            player2_square = player2_square.ladder
        pos_msg2 = font.render("Player_2 : " + str(player2_square.position), True, (0, 0, 0))
        screen.blit(pos_msg2, (960, 225))
        screen.blit(player2, (player2_square.x, player2_square.y))
        dice_value = 0
    if player1_won:
        screen.blit(win_msg1, (200, 300))
    if player2_won:
        screen.blit(win_msg2, (200, 300))
    pygame.display.flip()

pygame.quit()
