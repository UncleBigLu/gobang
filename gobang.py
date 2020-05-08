import random
import pygame

pygame.init()

space = 60  # edge space
cell_lenth = 40
cell_num = 15  # 15*15
chess_board_lenth = cell_lenth * (cell_num) + space * 2

screencaption = pygame.display.set_caption('gobang')
screen = pygame.display.set_mode((chess_board_lenth, chess_board_lenth))

chess_arr = []
color = True  # true for black chess, false for white chess
gamestate = 0 # 0:game running 1: black win 2: white win

def chess_count(chess,dir):
    x = chess[0]
    y = chess[1]
    c = chess[2]


    count = 0
    # judge whether there're five chesses in one line
    while True:
        x += dir[0]
        y += dir[1]
        if (x,y,c) in chess_arr:
            count += 1
        else:
            break
    return count





# main
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and gamestate == 0:
            x, y = pygame.mouse.get_pos()  # 获取鼠标位置
            xi = int(round((x - space) / cell_lenth))  # 获取到x方向上取整的序号
            yi = int(round((y - space) / cell_lenth))  # 获取到y方向上取整的序号
            if 0 <= xi <= cell_num \
                    and 0 <= yi <= cell_num and \
                    (xi, yi, True) not in chess_arr and (xi, yi, False) not in chess_arr:
                chess = (xi, yi, color)
                chess_arr.append(chess)

                # count chess number in each direction
                dir = [ [(1,0), (-1,0)], [(0,1), (0,-1)], [(1,1), (-1,-1)], [(1,-1), (-1,1)] ]
                for d in dir:
                    if chess_count(chess, d[0]) + chess_count(chess, d[1]) >= 4:
                        if color == True:
                            gamestate = 2
                        else:
                            gamestate = 1
                color = not color

    # paint chess board
    screen.fill((209, 162, 89))  # set the interface to brown
    for x in range(0, chess_board_lenth - space * 2 + 1, cell_lenth):
        pygame.draw.line(screen, (255, 255, 255), (x + space, space), (x + space, chess_board_lenth - space))
    for y in range(0, chess_board_lenth - space * 2 + 1, cell_lenth):
        pygame.draw.line(screen, (255, 255, 255), (space, y + space), (chess_board_lenth - space, y + space))

    # print chess
    for x, y, c in chess_arr:
        chess_color = (0, 0, 0) if c else (255, 255, 255)
        pygame.draw.circle(screen, chess_color, (x * cell_lenth + space, y * cell_lenth + space), 16)
    if gamestate != 0:
        myfont = pygame.font.Font(None, 60)
        win_text = "%s win"%('black' if gamestate == 2 else 'white')
        textImage = myfont.render(win_text, True, (0,100,255))
        screen.blit(textImage,(260,320))
    pygame.display.update()
