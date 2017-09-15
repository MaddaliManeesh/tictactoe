import datetime
import random
import pygame
import copy
from pygame.locals import *
# def printing(screen,row,row2,coloumn,coloumn2,x,o,ant,bat,cat,dog,eat,fish,goat,hat,ink,jug,knife,lamp,man,nill,oil,pant,quit,rat,a1,a2,b1,b2,c1,c2,d1,d2,e1,e2,f1,f2,g1,g2,h1,h2,i1,i2):
def screen_print(tic,screen,x,o):
    if tic[0][0] == 'x':
        screen.blit(x, (0, 0))
    if tic[0][0] == 'o':
        screen.blit(o, (0, 0))
    if tic[0][1] == 'x':
        screen.blit(x, (92, 0))
    if tic[0][1] == 'o':
        screen.blit(o, (92, 0))
    if tic[0][2] == 'x':
        screen.blit(x, (182, 0))
    if tic[0][2] == 'o':
        screen.blit(o, (182, 0))
    if tic[1][0] == 'x':
        screen.blit(x, (0, 92))
    if tic[1][0] == "o":
        screen.blit(o, (0, 92))
    if tic[1][1] == "x":
        screen.blit(x, (92, 92))
    if tic[1][1] == "o":
        screen.blit(o, (92, 92))
    if tic[1][2] == "x":
        screen.blit(x, (182, 92))
    if tic[1][2] == "o":
        screen.blit(o, (182, 92))
    if tic[2][0] == "x":
        screen.blit(x, (0, 182))
    if tic[2][0] == "o":
        screen.blit(o, (0, 182))
    if tic[2][1] == "x":
        screen.blit(x, (92, 182))
    if tic[2][1] == "o":
        screen.blit(o, (92, 182))
    if tic[2][2] == "x":
        screen.blit(x, (182, 182))
    if tic[2][2] == "o":
        screen.blit(o, (182, 182))
def play(tic,row1,coloumn1,count,count1,check,store):
    print "--------------------------"
    if tic[row1 - 1][coloumn1 - 1] != "x" and tic[row1 - 1][coloumn1 - 1] != "o":
        tic[row1 - 1][coloumn1 - 1] = "x"
    else:
        print "Error"
    for i in range(3):
        check = ""
        for j in tic:
            check = check + str(j[i])
            if check == "xxx" or check == "ooo":
                count = count + 1
                break
    check = ""
    if count > 0:
        print "PLAYER1 WON"
    for j in tic:
        check = ""
        for i in range(3):
            check = check + str(j[i])
            if check == "xxx" or check == "ooo":
                count = count + 1
                break
    check = ""
    if count > 0:
        print "PLAYER1 WON"
    n = 0
    while n < 3:
        check = check + str(tic[n][n])
        n = n + 1
    if check == "xxx" or check == "ooo":
        count = count + 1
    check = ""
    if count > 0:
        print "PLAYER1 WON"
    n = 2
    f = 0
    while n >= 0 and f < 3:
        check = check + str(tic[f][n])
        n = n - 1
        f = f + 1
    if check == "xxx" or check == "ooo":
        count = count + 1
    check = ""
    if count > 0:
        print "PLAYER1 WON"
    count1 = 0
    for i in tic:
        for j in i:
            if j == "x" or j == 'o':
                count1 = count1 + 1
    if count1 == 9:
        print "Draw"
    return row1,coloumn1,count,count1,store
def start():
    tic = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    check = ""
    count = 0
    count1 = 0
    store=[]
    width, height = 270, 270
    screen = pygame.display.set_mode((width, height))
    board = pygame.image.load("tick.png")
    x = pygame.image.load("x.jpg")
    o = pygame.image.load("o.jpg")
    row = row2 = 0
    coloumn = coloumn2 = 0
    return tic,check,count,count1,screen,board,x,o,row,row2,coloumn,coloumn2,store
def computer_play(tic,check,count,store):
    n = 1
    while n > 0:
        row2 = (random.randint(1, 3))
        coloumn2 = (random.randint(1, 3))
        if tic[row2 - 1][coloumn2 - 1] != "x" and tic[row2 - 1][coloumn2 - 1] != "o":
            tic[row2 - 1][coloumn2 - 1] = "o"
            store.append(copy.deepcopy(tic))
            break
        n = n + 1
    for i in tic:
        print i
    print "------------------------"
    for i in range(3):
        check = ""
        for j in tic:
            check = check + str(j[i])
        if check == "xxx" or check == "ooo":
            count = count + 2
            break
    check = ""
    if count > 0:
        print "PLAYER2 WON"
    n = 0
    while n < 3:
        check = check + str(tic[n][n])
        n = n + 1
    if check == "xxx" or check == "ooo":
        count = count + 2
    check = ""
    if count > 0:
        print "PLAYER2 WON"
    n = 2
    f = 0
    while n >= 0 and f < 3:
        check = check + str(tic[f][n])
        n = n - 1
        f = f + 1
    if check == "xxx" or check == "ooo":
        count = count + 2
    check = ""
    if count > 0:
        print "PLAYER2 WON"
    for i in tic:
        check = ""
        for j in range(3):
            check = check + str(i[j])
        if check == "xxx" or check == "ooo":
            count = count + 2
            print count, "-"
    check = ""
    if count > 0:
        print "PLAYER2 WON"
    count1 = 0
    for i in tic:
        for j in i:
            if j == "x" or j == 'o':
                count1 = count1 + 1
    if count1 == 9:
        print "Draw"
    for i in tic:
        print i
    return row2,coloumn2,count,count1,store
def rect(board):
    box1 = pygame.draw.rect(board, (255, 255, 255), (0, 0, 86, 86))
    box2 = pygame.draw.rect(board, (255, 255, 255), (92, 0, 86, 86))
    box3 = pygame.draw.rect(board, (255, 255, 255), (182, 0, 86, 86))
    box4 = pygame.draw.rect(board, (255, 255, 255), (0, 92, 86, 86))
    box5 = pygame.draw.rect(board, (255, 255, 255), (92, 92, 86, 86))
    box6 = pygame.draw.rect(board, (255, 255, 255), (182, 92, 86, 86))
    box7 = pygame.draw.rect(board, (255, 255, 255), (0, 182, 86, 86))
    box8 = pygame.draw.rect(board, (255, 255, 255), (92, 182, 86, 86))
    box9 = pygame.draw.rect(board, (255, 255, 255), (182, 182, 86, 86))
    return box1,box2,box3,box4,box5,box6,box7,box8,box9
def replay(board,store,screen,x,o):
    screen.blit(board,(0,0))
    for i in range(len(store)):
        if store[i][0][0] == 'x':
            screen.blit(x, (0, 0))
        if store[i][0][0] == 'o':
            screen.blit(o, (0, 0))
        if store[i][0][1] == 'x':
            screen.blit(x, (92,0))
        if store[i][0][1] == 'o':
            screen.blit(o, (92, 0))
        if store[i][0][2] == 'x':
            screen.blit(x, (182,0))
        if store[i][0][2] == 'o':
            screen.blit(o, (182, 0))
        if store[i][1][0] == 'x':
            screen.blit(x, (0, 92))
        if store[i][1][0] == "o":
            screen.blit(o, (0, 92))
        if store[i][1][1] == "x":
            screen.blit(x, (92, 92))
        if store[i][1][1] == "o":
            screen.blit(o, (92, 92))
        if store[i][1][2] == "x":
            screen.blit(x, (182, 92))
        if store[i][1][2] == "o":
            screen.blit(o, (182, 92))
        if store[i][2][0] == "x":
            screen.blit(x, (0, 182))
        if store[i][2][0] == "o":
            screen.blit(o, (0, 182))
        if store[i][2][1] == "x":
            screen.blit(x, (92, 182))
        if store[i][2][1] == "o":
            screen.blit(o, (92, 182))
        if store[i][2][2] == "x":
            screen.blit(x, (182, 182))
        if store[i][2][2] == "o":
            screen.blit(o, (182, 182))
def click(pos,box1,box2,box3,box4,box5,box6,box7,box8,box9,row,coloumn):
    if box1.collidepoint(pos):
        row = 1
        row1 = row
        coloumn = 1
        coloumn1 = coloumn
    if box2.collidepoint(pos):
        row = 1
        row1 = row
        coloumn = 2
        coloumn1 = coloumn
    if box3.collidepoint(pos):
        row = 1
        row1 = row
        coloumn = 3
        coloumn1 = coloumn
    if box4.collidepoint(pos):
        row = 2
        row1 = row
        coloumn = 1
        coloumn1 = coloumn
    if box5.collidepoint(pos):
        row = 2
        row1 = row
        coloumn = 2
        coloumn1 = coloumn
    if box6.collidepoint(pos):
        row = 2
        row1 = row
        coloumn = 3
        coloumn1 = coloumn
    if box7.collidepoint(pos):
        row = 3
        row1 = row
        coloumn = 1
        coloumn1 = coloumn
    if box8.collidepoint(pos):
        row = 3
        row1 = row
        coloumn = 2
        coloumn1 = coloumn
    if box9.collidepoint(pos):
        row = 3
        row1 = row
        coloumn = 3
        coloumn1 = coloumn
    return row,row1,coloumn,coloumn1
def test_play(score,youwon,youlose,draw,restart,font1):
    pygame.init()
    tic, check, count, count1, screen, board, x, o, row, row2, coloumn, coloumn2,store=start()
    ant = bat = cat = dog = eat = fish = goat = hat = ink = jug = knife = lamp = man = nill = oil = pant = quit = rat = a1 = a2 = b1 = b2 = c1 = c2 = d1 = d2 = e1 = e2 = f1 = f2 = g1 = g2 = h1 = h2 = i1 = i2 = (
    271, 271)
    store.append(copy.deepcopy(tic))
    tic = store[len(store)-1]
    running = 1
    while running:
        tic = store[len(store) - 1]
        pygame.display.set_caption("Tic Tac Toe")
        screen.fill(0)
        box1, box2, box3, box4, box5, box6, box7, box8, box9 = rect(board)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_BACKSPACE:
                    del store[len(store)-1]
                    print store
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print "--------------------------"
                n = 1
                while n > 0:
                    row = (random.randint(1, 3))
                    coloumn = (random.randint(1, 3))
                    if tic[row - 1][coloumn - 1] != "x" and tic[row - 1][coloumn - 1] != "o":
                        tic[row - 1][coloumn - 1] = "x"
                        store.append(copy.deepcopy(tic))
                        break
                    n = n + 1
                else:
                    print "Error"
                    break
                print store
                for i in range(3):
                    check = ""
                    for j in tic:
                        check = check + str(j[i])
                        if check == "xxx" or check == "ooo":
                            count = count + 1
                            break
                check = ""
                if count > 0:
                    print "PLAYER1 WON"
                    break
                for j in tic:
                    check = ""
                    for i in range(3):
                        check = check + str(j[i])
                        if check == "xxx" or check == "ooo":
                            count = count + 1
                            break
                check = ""
                if count > 0:
                    print "PLAYER1 WON"
                    break
                n = 0
                while n < 3:
                    check = check + str(tic[n][n])
                    n = n + 1
                if check == "xxx" or check == "ooo":
                    count = count + 1
                check = ""
                if count > 0:
                    print "PLAYER1 WON"
                    break
                n = 2
                f = 0
                while n >= 0 and f < 3:
                    check = check + str(tic[f][n])
                    n = n - 1
                    f = f + 1
                if check == "xxx" or check == "ooo":
                    count = count + 1
                check = ""
                if count > 0:
                    print "PLAYER1 WON"
                    break
                count1 = 0
                for i in tic:
                    for j in i:
                        if j == "x" or j == 'o':
                            count1 = count1 + 1
                if count1 == 9:
                    print "Draw"
                    break
                row2, coloumn2, count, count1,store =computer_play(tic, check, count,store)
                print store
            if event.type == KEYDOWN:
                if event.key == K_r:
                    playagain()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        screen.blit(board, (0, 0))
        screen_print(tic, screen, x, o)
        pygame.display.flip()
        score = score + 1
        if count > 0 or count1 == 9:
            break
    if count == 1:
        screen.fill((0, 0, 0))
        screen.blit(youwon, (50, 25))
        screen.blit(restart, (30, 235))
        score = 100 - (score / 100)
        score1 = font1.render("Score:-" + str(score), True, (255, 255, 255))
        screen.blit(score1, (50, 100))
    if count == 2:
        screen.fill((0, 0, 0))
        screen.blit(youlose, (50, 25))
        screen.blit(restart, (30, 235))
        score = 70 - (score / 100)
        score1 = font1.render("Score:-" + str(score), True, (255, 255, 255))
        screen.blit(score1, (50, 100))
    count1 = 0
    for i in tic:
        for j in i:
            if j == "x" or j == 'o':
                count1 = count1 + 1
    if count1 == 9 and count == 0:
        screen.fill((0, 0, 0))
        screen.blit(draw, (0, 0))
        screen.blit(restart, (30, 235))
        score = 0
        score1 = font1.render("Score:-" + str(score), True, (255, 255, 255))
        screen.blit(score1, (50, 100))
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == KEYDOWN:
                if event.key == K_r:
                    playagain()
        pygame.display.flip()
def leader_board(scorelist,screen,font):
    pygame.init()
    leaderboard = []
    d = []
    c = []
    for line in scorelist:
        c.append(line[-3:])
        d.append(line)
    c.sort()
    n = 0
    while n < len(c):
        for line in d:
            if c[n] == line[-3:]:
                leaderboard.append(line)
        n = n + 1
        intermediate = pygame.surface.Surface((300, 600))
        y = 20
        f = pygame.font.Font(None, 17)
        for l in leaderboard:
            intermediate.blit(f.render(l, True, (255, 255, 255)), (10, y))
            y += 20
    clock = pygame.time.Clock()
    scroll_y=0
    running = 1
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = 0
                    playagain()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: scroll_y = min(scroll_y + 15, 0)
                if event.button == 5: scroll_y = max(scroll_y - 15, -300)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        screen.blit(intermediate,(0,scroll_y))
        back = font.render("press ESC to move back", True, (255, 255, 255))
        screen.blit(back, (100, 250))
        pygame.display.flip()
        clock.tick(60)
def Daily_Stats(scorelist,font,b):
    pygame.init()
    screen = pygame.display.set_mode((270, 270))
    date = ""
    running = 1
    while running:
        screen.fill((0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.unicode.isdigit():
                    date += event.unicode
                if event.key == K_MINUS:
                    date += "-"
                elif event.key == K_BACKSPACE:
                    date = date[:-1]
                if event.key == K_RETURN:
                    for line in scorelist:
                        if line[:8] == date:
                            b.append(line)
                if event.key == K_ESCAPE:
                    playagain()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        seendate = font.render("Enter date(DD-MM-YY)" + str(date), True, (255, 255, 255))
        for i, each in enumerate(b):
            each_val = font.render(str(each), True, (255, 255, 255))
            screen.blit(each_val, (0, (i + 1) * 20))
        if len(b) == 0:
            empty = font.render("No data found", True, (255, 255, 255))
            screen.blit(empty, (0, 20))
        back = font.render("press ESC to move back", True, (255, 255, 255))
        screen.blit(back, (100, 250))
        screen.blit(seendate, (0, 0))
        pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        pygame.display.flip()
def Single_Player(score,youwon,youlose,restart,scorelist,name,font1,draw):
    pygame.init()
    tic, check, count, count1, screen, board, x, o, row, row2, coloumn, coloumn2,store = start()
    store.append(copy.deepcopy(tic))
    tic = store[len(store)-1]
    running = 1
    while running:
        tic = store[len(store) - 1]
        pygame.display.set_caption("Tic Tac Toe")
        screen.fill(0)
        box1, box2, box3, box4, box5, box6, box7, box8, box9 = rect(board)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_BACKSPACE:
                    del store[len(store)-1]
                    print store
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, row1, coloumn, coloumn1 = click(pos, box1, box2, box3, box4, box5, box6, box7, box8, box9, row,
                                                     coloumn)
                row1, coloumn1, count, count1,store = play(tic, row1, coloumn1, count, count1, check,store)
                if count == 1 or count1==9:
                    break
                row2, coloumn2, count, count1,store = computer_play(tic, check, count,store)
            if event.type == KEYDOWN:
                if event.key == K_r:
                    playagain()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        screen.blit(board, (0, 0))
        screen_print(tic, screen, x, o)
        pygame.display.flip()
        score = score + 1
        if count > 0 or count1 == 9:
            running = 0
    if count == 1:
        screen.fill((0, 0, 0))
        screen.blit(youwon, (50, 25))
        screen.blit(restart, (30, 235))
        score = 100 - (score / 100)
        score1 = font1.render(str(name) + "Score:-" + str(score), True, (255, 255, 255))
        screen.blit(score1, (50, 100))
        score = str(score)
        scorelist.write(datetime.date.today().strftime("%d-%m-%y"))
        scorelist.write(" %s --> %s\n" % (name, score))
    if count == 2:
        screen.fill((0, 0, 0))
        screen.blit(youlose, (50, 25))
        screen.blit(restart, (30, 235))
        score = 70 - (score / 100)
        score1 = font1.render("Score:-" + str(score), True, (255, 255, 255))
        screen.blit(score1, (50, 100))
        score = str(score)
        scorelist.write(datetime.date.today().strftime("%d-%m-%y"))
        scorelist.write("%s --> %s\n" % (name, score))
    count1 = 0
    for i in tic:
        for j in i:
            if j == "x" or j == 'o':
                count1 = count1 + 1
    if count1 == 9 and count == 0:
        screen.fill((0, 0, 0))
        screen.blit(draw, (0, 0))
        screen.blit(restart, (30, 235))
        score = 0
        score1 = font1.render("Score:-" + str(score), True, (255, 255, 255))
        screen.blit(score1, (50, 100))
        score = str(score)
        scorelist.write(datetime.date.today().strftime("%d-%m-%y"))
        scorelist.write("%s --> %s\n" % (name, score))
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == KEYDOWN:
                if event.key == K_r:
                    playagain()
                if event.key == K_l:
                    replay(board,tic, screen, x, o)
        pygame.display.flip()
    return store
def playagain():
    scorelist = open("filetest.txt", "a+")
    pygame.init()
    screen = pygame.display.set_mode((270, 270))
    font = pygame.font.Font(None, 20)
    font1 = pygame.font.Font(None,30)
    font2 = pygame.font.SysFont("comicsansms",40)
    tictactoe = pygame.image.load("TicTacToe.png")
    score=0
    a=0
    name=""
    startgame=0
    b=[]
    while True:
        pygame.display.set_caption("Tic Tac Toe")
        pos = pygame.mouse.get_pos()
        pygame.event.pump()
        screen.fill((0, 0, 0))
        rect1=pygame.draw.rect(screen,(0,0,0),(90,105,100,20))
        rect2=pygame.draw.rect(screen,(0,0,0),(90,140,100,20))
        rect3=pygame.draw.rect(screen,(0,0,0),(180,0,100,20))
        rect4=pygame.draw.rect(screen,(0,0,0),(90,180,100,20))
        rect5=pygame.draw.rect(screen,(0,0,0),(180,25,100,20))
        Option1 = font.render("Single Player", True, (255,255,255))
        Option2 = font.render("Multi Player", True, (255,255,255))
        Option3 = font.render("Daily stats",False,(255,255,255))
        Option4 = font.render("Test Play",False,(255,255,255))
        Option5 = font.render("Leader Board",False,(255,255,255))
        restart =  font1.render("Press r to PLAYAGAIN",True, (176,48,96))
        youwon = font2.render("YOU WON",True,(127,255,0))
        youlose = font2.render("YOU LOSE",True,(127,255,0))
        draw = font2.render("DRAW",True,(127,255,0))
        player1 = font2.render("PLAYER1 WON",True,(127,255,0))
        player2 = font2.render("PLAYER2 WON",True,(127,255,0))
        screen.blit(tictactoe,(0,0))
        if rect1.collidepoint(pygame.mouse.get_pos()):
            Option1 = font.render("Single Player", False, (255,0,0))
        if rect2.collidepoint(pygame.mouse.get_pos()):
            Option2 = font.render("Multi Player", False, (255,0,0))
        if rect3.collidepoint(pygame.mouse.get_pos()):
            Option3 = font.render("Daily stats",False,(255,0,0))
        if rect4.collidepoint(pygame.mouse.get_pos()):
            Option4 = font.render("Test Play",False,(255,0,0))
        if rect5.collidepoint(pygame.mouse.get_pos()):
            Option5 = font.render("Leader board",False,(255,0,0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.unicode.isalpha():
                    name += event.unicode
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                if event.key == K_RETURN:
                    startgame=1
            if event.type==pygame.MOUSEBUTTONDOWN:
                if rect4.collidepoint(pygame.mouse.get_pos()):
                   test_play(score,youwon,youlose,draw,restart,font1)
                if rect5.collidepoint(pygame.mouse.get_pos()):
                    leader_board(scorelist,screen,font)
                if rect3.collidepoint(pygame.mouse.get_pos()):
                    Daily_Stats(scorelist, font,b)
                if rect1.collidepoint(pygame.mouse.get_pos()):
                    store=Single_Player(score,youwon,youlose,restart,scorelist,name,font1,draw)
                if rect2.collidepoint(pygame.mouse.get_pos()):
                    tic, check, count, count1, screen, board, x, o, row, row2, coloumn, coloumn2,store = start()
                    running=1
                    score=0
                    while running:
                        pygame.display.set_caption("Tic Tac Toe")
                        screen.fill(0)
                        screen.blit(board,(0,0))
                        box1, box2, box3, box4, box5, box6, box7, box8, box9=rect(board)
                        for event in pygame.event.get():
                            if event.type==pygame.MOUSEBUTTONDOWN:
                                if event.button==3:
                                    pos = pygame.mouse.get_pos()
                                    row, row1, coloumn, coloumn1 = click(pos, box1, box2, box3, box4, box5, box6, box7,
                                                                         box8, box9, row, coloumn)
                                    row1,coloumn1,count,count1,store=play(tic, row1, coloumn1, count, count1, check,store)

                                if event.button==1:
                                    pos = pygame.mouse.get_pos()
                                    if box1.collidepoint(pos):
                                        row2=1
                                        row3=row2
                                        coloumn2=1
                                        coloumn3=coloumn2
                                    if box2.collidepoint(pos):
                                        row2=1
                                        row3=row2
                                        coloumn2=2
                                        coloumn3=coloumn2
                                    if box3.collidepoint(pos):
                                        row2=1
                                        row3=row2
                                        coloumn2=3
                                        coloumn3=coloumn2
                                    if box4.collidepoint(pos):
                                        row2=2
                                        row3=row2
                                        coloumn2=1
                                        coloumn3=coloumn2
                                    if box5.collidepoint(pos):
                                        row2=2
                                        row3=row2
                                        coloumn2=2
                                        coloumn3=coloumn2
                                    if box6.collidepoint(pos):
                                        row2=2
                                        row3=row2
                                        coloumn2=3
                                        coloumn3=coloumn2
                                    if box7.collidepoint(pos):
                                        row2=3
                                        row3=row2
                                        coloumn2=1
                                        coloumn3=coloumn2
                                    if box8.collidepoint(pos):

                                        row2=3
                                        row3=row2
                                        coloumn2=2
                                        coloumn3=coloumn2
                                    if box9.collidepoint(pos):

                                        row2=3
                                        row3=row2
                                        coloumn2=3
                                        coloumn3=coloumn2
                                    if tic[row3-1][coloumn3-1]!="x"and tic[row3-1][coloumn3-1]!= "o":
                                        tic[row3-1][coloumn3-1]="o"
                                    for i in tic:
                                        print i
                                    print "------------------------"
                                    for i in range(3):
                                        check=""
                                        for j in tic:
                                            check=check+str(j[i])
                                        if check == "xxx" or check == "ooo":
                                            count=count+2
                                            break
                                    check=""
                                    if count>0:
                                        print "PLAYER2 WON"
                                        break
                                    n=0
                                    while n<3:
                                        check=check+str(tic[n][n])
                                        n=n+1
                                    if check == "xxx" or check == "ooo":
                                        count=count+2
                                    check=""
                                    if count>0:
                                        print "PLAYER2 WON"
                                        break
                                    n=2
                                    f=0
                                    while n>=0 and f<3:
                                        check=check+str(tic[f][n])
                                        n=n-1
                                        f=f+1
                                    if check == "xxx" or check == "ooo":
                                        count=count+2
                                    check=""
                                    if count>0:
                                        print "PLAYER2 WON"
                                        break
                                    for i in tic:
                                        check=""
                                        for j in range(3):
                                            check=check+str(i[j])
                                        if check == "xxx" or check == "ooo":
                                            count=count+2
                                            print count,"-"
                                    check=""
                                    if count>0:
                                        print "PLAYER2 WON"
                                        break
                                    count1=0
                                    for i in tic:
                                        for j in i:
                                            if j=="x" or j=='o':
                                                count1=count1+1
                                    if count1==9:
                                        print "Draw"
                                        break
                                    for i in tic:
                                        print i

                            if event.type == pygame.QUIT:
                                pygame.quit()
                                exit(0)
                        screen_print(tic, screen, x, o)
                        pygame.display.flip()
                        score=score+1
                        if count>0:
                            running=0
                        if count1==9:
                            running=0
                    if count==1:
                        screen.fill((0,0,0))
                        screen.blit(player1,(0,0))
                        screen.blit(restart,(30,235))
                        score=100-(score/100)
                        score1=font1.render("Score:-"+str(score),True,(255,255,255))
                        screen.blit(score1,(50,100))
                        score=str(score)
                        scorelist.write("%s --> %s\n"%(name,score))
                    if count==2:
                        screen.fill((0,0,0))
                        screen.blit(player2,(0,0))
                        screen.blit(restart,(30,235))
                        score=70-(score/100)-5
                        score1=font1.render("Score:-"+str(score),True,(255,255,255))
                        screen.blit(score1,(50,100))
                        score=str(score)
                        scorelist.write("%s --> %s\n"%(name,score))
                    count1=0
                    for i in tic:
                        for j in i:
                            if j=="x" or j=='o':
                                count1=count1+1
                    if count1==9 and count==0:
                        screen.fill((0,0,0))
                        screen.blit(draw,(0,0))
                        screen.blit(restart,(30,235))
                        score=0
                        score1=font1.render("Score:-"+str(score),True,(255,255,255))
                        screen.blit(score1,(50,100))
                        score=str(score)
                        scorelist.write("%s --> %s\n"%(name,score))
                    while 1:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                exit(0)
                            if event.type == KEYDOWN:
                                if event.key == K_r:
                                    playagain()
                        pygame.display.flip()
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
        playername=font.render("Your name--"+str(name),True,(255,255,255))
        screen.blit(playername,(0,200))
        screen.blit(Option3 , (180,0))
        screen.blit(Option5, (180,25))
        if startgame==1:
            screen.blit(Option1, (90, 95))
            screen.blit(Option2 , (90,135))
            screen.blit(Option4, (90, 175))
        pygame.display.update()
        pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        pygame.display.flip()
playagain()