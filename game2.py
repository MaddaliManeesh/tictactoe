import time
import datetime
import random
import pygame
import copy
from pygame.locals import *

pygame.mixer.init()


class Game:
    def __init__(self):
        pass

    def screen_print(self, tic, screen, x, o):
        """

        :param tic: a list which have 3 lists in it which updates your move.
        :param screen: pygame screen where game is executed.
        :param x: x is the image of "x"
        :param o: o is the image of "o"
        :return:
        """
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
            screen.blit(o, (182, 182))  #

    # it prints "x" and "o" on the screen when you click on a box.

    def rect(self, board):
        box1 = pygame.draw.rect(board, (255, 255, 255), (0, 0, 86, 86))  # row=1 , coloumn=1
        box2 = pygame.draw.rect(board, (255, 255, 255), (92, 0, 86, 86))  # row=1 , coloumn=2
        box3 = pygame.draw.rect(board, (255, 255, 255), (182, 0, 86, 86))  # row=1 , coloumn = 3
        box4 = pygame.draw.rect(board, (255, 255, 255), (0, 92, 86, 86))  # row=2 , coloumn = 1
        box5 = pygame.draw.rect(board, (255, 255, 255), (92, 92, 86, 86))  # row=2 , coloumn = 2
        box6 = pygame.draw.rect(board, (255, 255, 255), (182, 92, 86, 86))  # row=2 , coloumn = 3
        box7 = pygame.draw.rect(board, (255, 255, 255), (0, 182, 86, 86))  # row = 3 , coloumn = 1
        box8 = pygame.draw.rect(board, (255, 255, 255), (92, 182, 86, 86))  # row = 3 , coloumn = 2
        box9 = pygame.draw.rect(board, (255, 255, 255), (182, 182, 86, 86))  # row = 3 , coloumn = 3
        return box1, box2, box3, box4, box5, box6, box7, box8, box9

    # it helps to detct the position of the click.

    def replay(self, board, store, screen, x, o, i):
        print store
        if store[i][0][0] == 'x':
            screen.blit(x, (0, 0))
        if store[i][0][0] == 'o':
            screen.blit(o, (0, 0))
        if store[i][0][1] == 'x':
            screen.blit(x, (92, 0))
        if store[i][0][1] == 'o':
            screen.blit(o, (92, 0))
        if store[i][0][2] == 'x':
            screen.blit(x, (182, 0))
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

    # it replays your game played by you.

    def click(self, pos, box1, box2, box3, box4, box5, box6, box7, box8, box9, row, coloumn):
        if box1.collidepoint(pos):  # detects the position of your click
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
        return row, row1, coloumn, coloumn1

    # this funtion helps you to detect the row and coloumn where you placed "x" or "o".

    def start(self):
        tic = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        check = ""
        count = 0
        count1 = 0
        store = []
        width, height = 270, 270
        screen = pygame.display.set_mode((width, height))
        board = pygame.image.load("tick.png")  # image of the board
        x = pygame.image.load("x.jpg")  # image of "x"
        o = pygame.image.load("o.jpg")  # image of "o"
        row = row2 = 0  # row2 is the row which computer plays
        coloumn = coloumn2 = 0  # coloumn is the coloumn in which computer plays
        return tic, check, count, count1, screen, board, x, o, row, row2, coloumn, coloumn2, store
        # these contains the basic requirements to run the code


class play(Game):
    def computer_play(self, tic, check, count, store):
        n = 1
        while n > 0:
            row2 = (random.randint(1, 3))
            coloumn2 = (random.randint(1, 3))
            if tic[row2 - 1][coloumn2 - 1] != "x" and tic[row2 - 1][coloumn2 - 1] != "o":
                tic[row2 - 1][coloumn2 - 1] = "o"
                store.append(copy.deepcopy(tic))
                break
            n = n + 1
        for element in tic:
            print element
        print "------------------------"
        for number in range(3):
            check = ""
            for element in tic:
                check = check + str(element[number])
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
        for element in tic:
            check = ""
            for number in range(3):
                check = check + str(element[number])
            if check == "xxx" or check == "ooo":
                count = count + 2
                print count, "-"
        check = ""
        if count > 0:
            print "PLAYER2 WON"
        count1 = 0
        for element in tic:
            for j in element:
                if j == "x" or j == 'o':
                    count1 = count1 + 1
        if count1 == 9:
            print "Draw"
        for element in tic:
            print element
        return row2, coloumn2, count, count1, store

    # it controls and detects the moves played by the computer.

    def play(self, tic, row1, coloumn1, count, count1, check, store):
        """

        :param tic:a list which have 3 lists in it which updates your move.
        :param row1:it is the row which you choosen
        :param coloumn1:it is the coloumn which you choosen
        :param count:it increses when any row or coloumn are filled with "x" or "o"
        :param count1:it increses when the no. move are equal to 9
        :param check:it is a string which checks whether row or coloumn are equal
        :param store:a list which stores your every move
        :return:
        """
        print "--------------------------"
        if tic[row1 - 1][coloumn1 - 1] != "x" and tic[row1 - 1][coloumn1 - 1] != "o":
            tic[row1 - 1][coloumn1 - 1] = "x"  # updates tic
        else:
            print "Error"
        for number in range(3):
            check = ""
            for element in tic:
                check = check + str(element[number])
                if check == "xxx" or check == "ooo":  # checks coloumn
                    count = count + 1
                    break
        check = ""
        if count > 0:
            print "PLAYER1 WON"
        for element in tic:
            check = ""
            for number in range(3):
                check = check + str(element[number])
                if check == "xxx" or check == "ooo":  # checks row
                    count = count + 1
                    break
        check = ""
        if count > 0:
            print "PLAYER1 WON"
        n = 0
        while n < 3:
            check = check + str(tic[n][n])
            n = n + 1
        if check == "xxx" or check == "ooo":  # checks left to right cross
            count = count + 1
        check = ""
        if count > 0:
            print "PLAYER1 WON"
        n = 2
        f = 0
        while n >= 0 and f < 3:
            check = check + str(tic[f][n])  # checks right to left cross
            n = n - 1
            f = f + 1
        if check == "xxx" or check == "ooo":
            count = count + 1
        check = ""
        if count > 0:
            print "PLAYER1 WON"
        count1 = 0
        for element in tic:
            for j in element:
                if j == "x" or j == 'o':  # checks draw
                    count1 = count1 + 1
        if count1 == 9:
            print "Draw"
        return row1, coloumn1, count, count1, store
        # it controls and detects all the moves played by a player.


class player_options(play, Game):
    def settings(self, namelist, name, select, screen, font):
        settings_file = open("volume.txt", "a+")
        pygame.init()
        volume = ""
        scroll_x = 0
        intermediate = pygame.surface.Surface((600, 270))  # creates a surface
        choose_singleplayer = font.render("Single player", True, (255, 255, 255))
        choose_multiplayer = font.render("Multi player", True, (255, 255, 255))
        rect10 = pygame.draw.rect(intermediate, ((0)), (10, 40, 70, 20))
        rect1010 = pygame.draw.rect(intermediate, ((0)), (100, 40, 70, 20))
        running = 1
        for j in settings_file:
            if name == j[:len(j) - 4]:
                volume == j[len(j) - 4:]
                running = 0
                self.playagain()
                break
        while running:
            screen.fill((0))
            if rect10.collidepoint(pygame.mouse.get_pos()):
                choose_singleplayer = font.render("Single player", False, (255, 0, 0))
            if rect1010.collidepoint(pygame.mouse.get_pos()):
                choose_multiplayer = font.render("Multi player", False, (255, 0, 0))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.unicode.isdigit():
                        volume += event.unicode
                    elif event.key == K_BACKSPACE:
                        volume = volume[:-1]
                    if event.key == K_RETURN:
                        volume = int(volume)
                        running = 0
                    if event.key == K_ESCAPE:
                        self.playagain()
                        running = 0
                    if event.key == K_LEFT:
                        scroll_x = min(0, scroll_x + 15)
                    if event.key == K_RIGHT:
                        scroll_x = min(0, scroll_x - 15)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            veiw_volume = font.render("Volume-" + str(volume), True, (255, 255, 255))
            intermediate.blit(veiw_volume, (0, 0))
            choose_player = font.render("Choose default player", True, (255, 255, 255))
            intermediate.blit(choose_player, (0, 20))
            intermediate.blit(choose_singleplayer, (10, 40))
            intermediate.blit(choose_multiplayer, (100, 40))
            screen.blit(intermediate, (scroll_x, 0))
            pygame.display.flip()
        settings_file.write(str(name) + " " + str(volume) + "\n")

    def leader_board(self, scorelist, screen, font):
        """

        :param scorelist: name of the file which stores your name entered,date,score of that person.
        :param screen: already explained
        :param font: stores type of font,size of font
        :return:
        """
        pygame.init()
        leaderboard = []
        d = []
        c = []
        for line in scorelist:
            c.append(line[-3:])  # stores scores
            d.append(line)  # stores date,name,score
        c.sort()  # sorts scores
        n = 0
        while n < len(c):
            for line in d:
                if c[n] == line[-3:]:
                    leaderboard.append(line)  # stores your name , date by the arranged score
            n = n + 1
            intermediate = pygame.surface.Surface((300, 600))  # creates a surface
            y = 20
            f = pygame.font.Font(None, 17)
            for each_leaderboard in leaderboard:
                intermediate.blit(f.render(each_leaderboard, True, (255, 255, 255)), (10, y))  # writes on the surface
                y += 20
        clock = pygame.time.Clock()
        scroll_y = 0
        running = 1
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = 0  # restarts the game
                        self.playagain()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4: scroll_y = min(scroll_y + 15, 0)  # scrolls up
                    if event.button == 5: scroll_y = max(scroll_y - 15, -300)  # scrolls down
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            screen.blit(intermediate, (0, scroll_y))  # displays your surface
            back = font.render("press ESC to move back", True, (255, 255, 255))
            screen.blit(back, (100, 250))
            pygame.display.flip()
            clock.tick(60)

    # it shows your position according to your score.

    def Daily_Stats(self, scorelist, font, b):
        pygame.init()
        screen = pygame.display.set_mode((270, 270))
        date = ""
        running = 1
        scroll_y = 0
        intermediate = pygame.surface.Surface((300, 600))  # creates a surface

        while running:
            screen.fill((0))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.unicode.isdigit():  # only allows numbers
                        date += event.unicode
                    if event.key == K_MINUS:  # when - is clicked
                        date += "-"
                    elif event.key == K_BACKSPACE:
                        date = date[:-1]
                    if event.key == K_RETURN:
                        for line in scorelist:
                            if line[:8] == date:
                                b.append(line)
                                y = 20
                                f = pygame.font.Font(None, 17)
                                for each_b in b:
                                    intermediate.blit(f.render(each_b, True, (255, 255, 255)),
                                                      (10, y))  # writes on the surface
                                    y += 20
                    if event.key == K_ESCAPE:
                        self.playagain()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4: scroll_y = min(scroll_y + 15, 0)  # scrolls up
                    if event.button == 5: scroll_y = max(scroll_y - 15, -300)  # scrolls down
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            seendate = font.render("Enter date(DD-MM-YY)" + str(date), True, (255, 255, 255))
            screen.blit(intermediate, (0, scroll_y))
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
            # it records the daily game status.


class player_types(play, Game, player_options):
    def test_play(self, score, youwon, youlose, draw, restart, font1):
        pygame.init()
        tic, check, count, count1, screen, board, x, o, row, row2, coloumn, coloumn2, store = self.start()
        ant = bat = cat = dog = eat = fish = goat = hat = ink = jug = knife = lamp = man = nill = oil = pant = quit = rat = a1 = a2 = b1 = b2 = c1 = c2 = d1 = d2 = e1 = e2 = f1 = f2 = g1 = g2 = h1 = h2 = i1 = i2 = (
            271, 271)
        store.append(copy.deepcopy(tic))
        tic = store[len(store) - 1]
        running = 1
        while running:
            tic = store[len(store) - 1]
            pygame.display.set_caption("Tic Tac Toe")
            screen.fill(0)
            box1, box2, box3, box4, box5, box6, box7, box8, box9 = self.rect(board)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_BACKSPACE:  # undo option
                        del store[len(store) - 1]
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
                    for number in range(3):
                        check = ""
                        for element in tic:
                            check = check + str(element[number])
                            if check == "xxx" or check == "ooo":
                                count = count + 1
                                break
                    check = ""
                    if count > 0:
                        print "PLAYER1 WON"
                        break
                    for element in tic:
                        check = ""
                        for number in range(3):
                            check = check + str(element[number])
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
                    for element in tic:
                        for j in element:
                            if j == "x" or j == 'o':
                                count1 = count1 + 1
                    if count1 == 9:
                        print "Draw"
                        break
                    row2, coloumn2, count, count1, store = self.computer_play(tic, check, count, store)
                    print store
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        self.playagain()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            screen.blit(board, (0, 0))
            self.screen_print(tic, screen, x, o)
            pygame.display.flip()
            score = score + 1
            if count > 0 or count1 == 9:
                break
        if count == 1:
            screen.fill((0, 0, 0))
            screen.blit(youwon, (50, 25))  # displays you won
            screen.blit(restart, (30, 235))  # displays text how to restart
            score = 100 - (score / 100)
            score1 = font1.render("Score:-" + str(score), True, (255, 255, 255))
            screen.blit(score1, (50, 100))  # displays score
        if count == 2:
            screen.fill((0, 0, 0))
            screen.blit(youlose, (50, 25))  # displays you lose
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
            screen.blit(draw, (0, 0))  # displays draw
            screen.blit(restart, (30, 235))
            score = 0
            score1 = font1.render("Score:-" + str(score), True, (255, 255, 255))
            screen.blit(score1, (50, 100))
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # event to end the game
                    pygame.quit()
                    exit(0)
                if event.type == KEYDOWN:
                    if event.key == K_r:  # if we click r we game restarts
                        self.playagain()
            pygame.display.flip()

    # it shows the game played by 2 computer players.

    def Single_Player(self, score, youwon, youlose, restart, scorelist, name, font1, draw):
        pygame.init()
        tic, check, count, count1, screen, board, x, o, row, row2, coloumn, coloumn2, store = self.start()
        clicksound = pygame.mixer.Sound("click sound.wav")
        close = pygame.mixer.Sound("close.wav")
        store.append(copy.deepcopy(tic))
        tic = store[len(store) - 1]
        running = 1
        while running:
            tic = store[len(store) - 1]
            pygame.display.set_caption("Tic Tac Toe")
            screen.fill(0)
            box1, box2, box3, box4, box5, box6, box7, box8, box9 = self.rect(board)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_BACKSPACE:
                        del store[len(store) - 1]
                        close.play()
                        print store
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicksound.play()
                    pos = pygame.mouse.get_pos()
                    row, row1, coloumn, coloumn1 = self.click(pos, box1, box2, box3, box4, box5, box6, box7, box8, box9,
                                                              row,
                                                              coloumn)
                    row1, coloumn1, count, count1, store = self.play(tic, row1, coloumn1, count, count1, check, store)
                    if count == 1 or count1 == 9:
                        break
                    row2, coloumn2, count, count1, store = self.computer_play(tic, check, count, store)
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        clicksound.play()
                        self.playagain()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            screen.blit(board, (0, 0))
            self.screen_print(tic, screen, x, o)
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
        i = 0
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    close.play()
                    pygame.quit()
                    exit(0)
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        self.playagain()
                    if event.key == K_l:
                        while i < len(store) - 1:
                            screen.blit(board, (0, 0))
                            self.replay(board, store, screen, x, o, i)
                            time.sleep(2)
                            i = i + 1
            pygame.display.flip()
        return store, close,check

    # game played between you and a computer player.

    def playagain(self):
        scorelist = open("filetest.txt", "a+")
        pygame.init()
        screen = pygame.display.set_mode((270, 270))
        font = pygame.font.Font(None, 20)
        font1 = pygame.font.Font(None, 30)
        font2 = pygame.font.SysFont("comicsansms", 40)
        tictactoe = pygame.image.load("TicTacToe.png")
        select = pygame.mixer.Sound("Ding.wav")
        volume = 0.05
        score = 0
        a = 0
        name = ""
        namelist = []
        startgame = 0
        b = []
        while True:
            pygame.display.set_caption("Tic Tac Toe")
            pos = pygame.mouse.get_pos()
            pygame.event.pump()
            screen.fill((0, 0, 0))
            rect1 = pygame.draw.rect(screen, (0, 0, 0), (90, 105, 100, 20))
            rect2 = pygame.draw.rect(screen, (0, 0, 0), (90, 140, 100, 20))
            rect3 = pygame.draw.rect(screen, (0, 0, 0), (180, 0, 100, 20))
            rect4 = pygame.draw.rect(screen, (0, 0, 0), (90, 180, 100, 20))
            rect5 = pygame.draw.rect(screen, (0, 0, 0), (180, 25, 100, 20))
            rect6 = pygame.draw.rect(screen, (0, 0, 0), (10, 5, 70, 20))
            Option1 = font.render("Single Player", True, (255, 255, 255))
            Option2 = font.render("Multi Player", True, (255, 255, 255))
            Option3 = font.render("Daily stats", False, (255, 255, 255))
            Option4 = font.render("Test Play", False, (255, 255, 255))
            Option5 = font.render("Leader Board", False, (255, 255, 255))
            Option6 = font.render("Settings", False, (255, 255, 255))
            restart = font1.render("Press r to PLAYAGAIN", True, (176, 48, 96))
            youwon = font2.render("YOU WON", True, (127, 255, 0))
            youlose = font2.render("YOU LOSE", True, (127, 255, 0))
            draw = font2.render("DRAW", True, (127, 255, 0))
            player1 = font2.render("PLAYER1 WON", True, (127, 255, 0))
            player2 = font2.render("PLAYER2 WON", True, (127, 255, 0))
            screen.blit(tictactoe, (0, 0))
            if rect1.collidepoint(pygame.mouse.get_pos()):
                Option1 = font.render("Single Player", False, (255, 0, 0))
            if rect2.collidepoint(pygame.mouse.get_pos()):
                Option2 = font.render("Multi Player", False, (255, 0, 0))
            if rect3.collidepoint(pygame.mouse.get_pos()):
                Option3 = font.render("Daily stats", False, (255, 0, 0))
            if rect4.collidepoint(pygame.mouse.get_pos()):
                Option4 = font.render("Test Play", False, (255, 0, 0))
            if rect5.collidepoint(pygame.mouse.get_pos()):
                Option5 = font.render("Leader board", False, (255, 0, 0))
            if rect6.collidepoint(pygame.mouse.get_pos()):
                Option6 = font.render("Settings", False, (255, 0, 0))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.unicode.isalpha():
                        name += event.unicode
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    if event.key == K_RETURN:
                        startgame = 1
                    namelist.append(name)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    select.play()
                    if rect4.collidepoint(pygame.mouse.get_pos()):
                        self.test_play(score, youwon, youlose, draw, restart, font1)
                    if rect5.collidepoint(pygame.mouse.get_pos()):
                        self.leader_board(scorelist, screen, font)
                    if rect3.collidepoint(pygame.mouse.get_pos()):
                        self.Daily_Stats(scorelist, font, b)
                    if rect1.collidepoint(pygame.mouse.get_pos()):
                        store, close = self.Single_Player(score, youwon, youlose, restart, scorelist, name, font1, draw)
                    if rect6.collidepoint(pygame.mouse.get_pos()):
                        self.settings(namelist, name, select, screen, font)
                    if rect2.collidepoint(pygame.mouse.get_pos()):
                        tic, check, count, count1, screen, board, x, o, row, row2, coloumn, coloumn2, store = self.start()
                        running = 1
                        score = 0
                        while running:
                            pygame.display.set_caption("Tic Tac Toe")
                            screen.fill(0)
                            screen.blit(board, (0, 0))
                            box1, box2, box3, box4, box5, box6, box7, box8, box9 = self.rect(board)
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if event.button == 3:
                                        pos = pygame.mouse.get_pos()
                                        row, row1, coloumn, coloumn1 = self.click(pos, box1, box2, box3, box4, box5,
                                                                                  box6, box7,
                                                                                  box8, box9, row, coloumn)
                                        row1, coloumn1, count, count1, store = self.play(tic, row1, coloumn1, count,
                                                                                         count1,
                                                                                         check, store)

                                    if event.button == 1:
                                        pos = pygame.mouse.get_pos()
                                        if box1.collidepoint(pos):
                                            row2 = 1
                                            row3 = row2
                                            coloumn2 = 1
                                            coloumn3 = coloumn2
                                        if box2.collidepoint(pos):
                                            row2 = 1
                                            row3 = row2
                                            coloumn2 = 2
                                            coloumn3 = coloumn2
                                        if box3.collidepoint(pos):
                                            row2 = 1
                                            row3 = row2
                                            coloumn2 = 3
                                            coloumn3 = coloumn2
                                        if box4.collidepoint(pos):
                                            row2 = 2
                                            row3 = row2
                                            coloumn2 = 1
                                            coloumn3 = coloumn2
                                        if box5.collidepoint(pos):
                                            row2 = 2
                                            row3 = row2
                                            coloumn2 = 2
                                            coloumn3 = coloumn2
                                        if box6.collidepoint(pos):
                                            row2 = 2
                                            row3 = row2
                                            coloumn2 = 3
                                            coloumn3 = coloumn2
                                        if box7.collidepoint(pos):
                                            row2 = 3
                                            row3 = row2
                                            coloumn2 = 1
                                            coloumn3 = coloumn2
                                        if box8.collidepoint(pos):
                                            row2 = 3
                                            row3 = row2
                                            coloumn2 = 2
                                            coloumn3 = coloumn2
                                        if box9.collidepoint(pos):
                                            row2 = 3
                                            row3 = row2
                                            coloumn2 = 3
                                            coloumn3 = coloumn2
                                        if tic[row3 - 1][coloumn3 - 1] != "x" and tic[row3 - 1][coloumn3 - 1] != "o":
                                            tic[row3 - 1][coloumn3 - 1] = "o"
                                        for element in tic:
                                            print element
                                        print "------------------------"
                                        for number in range(3):
                                            check = ""
                                            for element in tic:
                                                check = check + str(element[number])
                                            if check == "xxx" or check == "ooo":
                                                count = count + 2
                                                break
                                        check = ""
                                        if count > 0:
                                            print "PLAYER2 WON"
                                            break
                                        n = 0
                                        while n < 3:
                                            check = check + str(tic[n][n])
                                            n = n + 1
                                        if check == "xxx" or check == "ooo":
                                            count = count + 2
                                        check = ""
                                        if count > 0:
                                            print "PLAYER2 WON"
                                            break
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
                                            break
                                        for element in tic:
                                            check = ""
                                            for number in range(3):
                                                check = check + str(element[number])
                                            if check == "xxx" or check == "ooo":
                                                count = count + 2
                                                print count, "-"
                                        check = ""
                                        if count > 0:
                                            print "PLAYER2 WON"
                                            break
                                        count1 = 0
                                        for element in tic:
                                            for j in element:
                                                if j == "x" or j == 'o':
                                                    count1 = count1 + 1
                                        if count1 == 9:
                                            print "Draw"
                                            break
                                        for i in tic:
                                            print i

                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    exit(0)
                            self.screen_print(tic, screen, x, o)
                            pygame.display.flip()
                            score = score + 1
                            if count > 0:
                                running = 0
                            if count1 == 9:
                                running = 0
                        if count == 1:
                            screen.fill((0, 0, 0))
                            screen.blit(player1, (0, 0))
                            screen.blit(restart, (30, 235))
                            score = 100 - (score / 100)
                            score1 = font1.render("Score:-" + str(score), True, (255, 255, 255))
                            screen.blit(score1, (50, 100))
                            score = str(score)
                            scorelist.write("%s --> %s\n" % (name, score))
                        if count == 2:
                            screen.fill((0, 0, 0))
                            screen.blit(player2, (0, 0))
                            screen.blit(restart, (30, 235))
                            score = 70 - (score / 100) - 5
                            score1 = font1.render("Score:-" + str(score), True, (255, 255, 255))
                            screen.blit(score1, (50, 100))
                            score = str(score)
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
                            scorelist.write("%s --> %s\n" % (name, score))
                        while 1:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    exit(0)
                                if event.type == KEYDOWN:
                                    if event.key == K_r:
                                        self.playagain()
                            pygame.display.flip()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            playername = font.render("Your name--" + str(name), True, (255, 255, 255))
            screen.blit(playername, (0, 200))
            screen.blit(Option3, (180, 0))
            screen.blit(Option5, (180, 25))
            screen.blit(Option6, (10, 5))
            if startgame == 1:
                screen.blit(Option1, (90, 95))
                screen.blit(Option2, (90, 135))
                screen.blit(Option4, (90, 175))
            pygame.display.update()
            pygame.display.flip()
        select.set_volume(volume)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.flip()


game = player_types()
game.playagain()
# this funtion executes the code and has multiplayer option in it.
