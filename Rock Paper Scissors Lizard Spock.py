#Rock Paper Scissors Lizard Spock
import random
import pygame
pygame.init()

action = ["rock", "paper", "scissors", "lizard", "spock"]
pygame.display.set_caption("Rock Paper Scissors Lizard Spock")

#colors
whitecolor = (255, 255, 255)
graycolor = (100, 100, 100)
redcolor = (255, 0, 0)
greencolor = (0,200,0)
blackcolor = (0,0,0)
bluecolor = (100,100,200)

#window
width = 1000
height = 700
window = pygame.display.set_mode((width, height))
window.fill(whitecolor)
fps = 60
time = pygame.time.Clock()
font = pygame.font.Font(None, 50)
largeFont = pygame.font.Font(None, 150)

#Cover Screen
cover_screen = pygame.Rect(0,0,1000,700)

def intro():

    #title box
    title = "Rock Paper Scissors Lizard Spock"
    title_box = pygame.Rect(25,25,950,50)
    pygame.draw.rect(window, blackcolor, title_box)
    title_words = font.render(title, True, whitecolor)
    window.blit(title_words, (title_box.x + 200, title_box.y + 10))  #place title words

    #Welcome
    welcome = "Welcome"
    welcome_words = largeFont.render(welcome, True, bluecolor)
    window.blit(welcome_words, (280,300))
    

    #play button
    play_box = pygame.Rect(450,400,100,50)
    pygame.draw.rect(window, bluecolor, play_box)
    plays = "PLAY"
    plays_words = font.render(plays, True, whitecolor)
    window.blit(plays_words, (play_box.x + 6, play_box.y + 10))

    #exit button
    exit_box = pygame.Rect(450,455,100,50)
    pygame.draw.rect(window, bluecolor, exit_box)
    exits = "EXIT"
    exits_words = font.render(exits, True, whitecolor)
    window.blit(exits_words, (exit_box.x + 6, exit_box.y + 10))


    

    run = True
    while run:

        time.tick(fps)

        #Events that cause things to happen
        for event in pygame.event.get():

            #X button clicked
            if event.type == pygame.QUIT:
                run = False

            #Button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_box.collidepoint(event.pos):
                    pygame.draw.rect(window, whitecolor, cover_screen)
                    game()

                elif exit_box.collidepoint(event.pos):
                    run = False
                

    
        pygame.display.update()                                         #update the window

    pygame.quit()

#title box
title = "Rock Paper Scissors Lizard Spock"
title_box = pygame.Rect(25,25,950,50)
title_words = font.render(title, True, whitecolor)

#vertical box
vert_box = pygame.Rect(250,100,25,575)

#horizontal box
h_box = pygame.Rect(275,375,700,25)
#Player Cover Box
p_cover = pygame.Rect(450,425,60,60)
#Computer Cover Box
c_cover = pygame.Rect(500,125,60,60)

#computer name
computer_name = "Computer:"
computer_words = font.render(computer_name, True, blackcolor)

#plyer name
player_name = "Player:"
player_words = font.render(player_name, True, blackcolor)

#rock button
rock_button = pygame.Rect(25,100,200,75)
rock_name = "ROCK"
rock_words = font.render(rock_name, True, whitecolor)

#paper button
paper_button = pygame.Rect(25,225,200,75)
paper_name = "PAPER"
paper_words = font.render(paper_name, True, whitecolor)

#scissors button
sci_button = pygame.Rect(25,350,200,75)
sci_name = "SCISSORS"
sci_words = font.render(sci_name, True, whitecolor)

#lizard button
liz_button = pygame.Rect(25,475,200,75)
liz_name = "LIZARD"
liz_words = font.render(liz_name, True, whitecolor)

#Spock button
spock_button = pygame.Rect(25,600,200,75)
spock_name = "SPOCK"
spock_words = font.render(spock_name, True, whitecolor)

#Win Tie Cover top
c_win_tie_cover = pygame.Rect(675,125,100,60)
p_win_tie_cover = pygame.Rect(675,425,100,60)

#choice cover
p_choice_cover = pygame.Rect(375,500,600,100)
c_choice_cover = pygame.Rect(375,200,600,150)



def gametie():
    win = "WIN"
    tie = "TIE"
    tie_words = font.render(tie, True, redcolor)
    pygame.draw.rect(window, whitecolor, c_win_tie_cover)
    pygame.draw.rect(window, whitecolor, p_win_tie_cover)
    window.blit(tie_words, (675,425))
    window.blit(tie_words, (675,125))

    

def playerwin():
    win = "WIN"
    tie = "TIE"
    pwin_words = font.render(win, True, redcolor)
    pygame.draw.rect(window, whitecolor, p_win_tie_cover)
    pygame.draw.rect(window, whitecolor, c_win_tie_cover)
    window.blit(pwin_words, (675,425))


def compwin():
    win = "WIN"
    tie = "TIE"
    cwin_words = font.render(win, True, redcolor)
    pygame.draw.rect(window, whitecolor, c_win_tie_cover)
    pygame.draw.rect(window, whitecolor, p_win_tie_cover)
    window.blit(cwin_words, (675,125))

def playerchoice(choice):
    choice = choice.upper()
    pygame.draw.rect(window, whitecolor, p_choice_cover)
    player_choice_words = largeFont.render(choice, True, blackcolor)
    window.blit(player_choice_words, (375,500))

def changegreen(choice):
    if choice == "rock":
        pygame.draw.rect(window, blackcolor, spock_button)              #place spock button
        pygame.draw.rect(window, blackcolor, liz_button)                #place lizard button
        pygame.draw.rect(window, blackcolor, sci_button)                #place scissors button
        pygame.draw.rect(window, blackcolor, paper_button)              #place paper button
        pygame.draw.rect(window, greencolor, rock_button)               #place rock button
        window.blit(spock_words, (spock_button.x +35, spock_button.y +22)) #place spock name
        window.blit(liz_words, (liz_button.x +37, liz_button.y +22))    #place lizard name
        window.blit(sci_words, (sci_button.x +10, sci_button.y +22))    #place scissors name
        window.blit(paper_words,(paper_button.x +37,paper_button.y +22))#place paper name
        window.blit(rock_words, (72, 122))                              #place rock name
    elif choice == "paper":
        pygame.draw.rect(window, blackcolor, spock_button)              #place spock button
        pygame.draw.rect(window, blackcolor, liz_button)                #place lizard button
        pygame.draw.rect(window, blackcolor, sci_button)                #place scissors button
        pygame.draw.rect(window, greencolor, paper_button)              #place paper button
        pygame.draw.rect(window, blackcolor, rock_button)               #place rock button
        window.blit(spock_words, (spock_button.x +35, spock_button.y +22)) #place spock name
        window.blit(liz_words, (liz_button.x +37, liz_button.y +22))    #place lizard name
        window.blit(sci_words, (sci_button.x +10, sci_button.y +22))    #place scissors name
        window.blit(paper_words,(paper_button.x +37,paper_button.y +22))#place paper name
        window.blit(rock_words, (72, 122))                              #place rock name
    elif choice == "scissors":
        pygame.draw.rect(window, blackcolor, spock_button)              #place spock button
        pygame.draw.rect(window, blackcolor, liz_button)                #place lizard button
        pygame.draw.rect(window, greencolor, sci_button)                #place scissors button
        pygame.draw.rect(window, blackcolor, paper_button)              #place paper button
        pygame.draw.rect(window, blackcolor, rock_button)               #place rock button
        window.blit(spock_words, (spock_button.x +35, spock_button.y +22)) #place spock name
        window.blit(liz_words, (liz_button.x +37, liz_button.y +22))    #place lizard name
        window.blit(sci_words, (sci_button.x +10, sci_button.y +22))    #place scissors name
        window.blit(paper_words,(paper_button.x +37,paper_button.y +22))#place paper name
        window.blit(rock_words, (72, 122))                              #place rock name
    elif choice == "lizard":
        pygame.draw.rect(window, blackcolor, spock_button)              #place spock button
        pygame.draw.rect(window, greencolor, liz_button)                #place lizard button
        pygame.draw.rect(window, blackcolor, sci_button)                #place scissors button
        pygame.draw.rect(window, blackcolor, paper_button)              #place paper button
        pygame.draw.rect(window, blackcolor, rock_button)               #place rock button
        window.blit(spock_words, (spock_button.x +35, spock_button.y +22)) #place spock name
        window.blit(liz_words, (liz_button.x +37, liz_button.y +22))    #place lizard name
        window.blit(sci_words, (sci_button.x +10, sci_button.y +22))    #place scissors name
        window.blit(paper_words,(paper_button.x +37,paper_button.y +22))#place paper name
        window.blit(rock_words, (72, 122))                              #place rock name
    else:
        pygame.draw.rect(window, greencolor, spock_button)              #place spock button
        pygame.draw.rect(window, blackcolor, liz_button)                #place lizard button
        pygame.draw.rect(window, blackcolor, sci_button)                #place scissors button
        pygame.draw.rect(window, blackcolor, paper_button)              #place paper button
        pygame.draw.rect(window, blackcolor, rock_button)               #place rock button
        window.blit(spock_words, (spock_button.x +35, spock_button.y +22)) #place spock name
        window.blit(liz_words, (liz_button.x +37, liz_button.y +22))    #place lizard name
        window.blit(sci_words, (sci_button.x +10, sci_button.y +22))    #place scissors name
        window.blit(paper_words,(paper_button.x +37,paper_button.y +22))#place paper name
        window.blit(rock_words, (72, 122))                              #place rock name
    


    

def game():

    
    pygame.draw.rect(window, blackcolor, spock_button)              #place spock button
    window.blit(spock_words, (spock_button.x +35, spock_button.y +22)) #place spock name
    pygame.draw.rect(window, blackcolor, liz_button)                #place lizard button
    window.blit(liz_words, (liz_button.x +37, liz_button.y +22))    #place lizard name
    pygame.draw.rect(window, blackcolor, sci_button)                #place scissors button
    window.blit(sci_words, (sci_button.x +10, sci_button.y +22))    #place scissors name
    pygame.draw.rect(window, blackcolor, paper_button)              #place paper button
    window.blit(paper_words,(paper_button.x +37,paper_button.y +22))#place paper name
    pygame.draw.rect(window, blackcolor, rock_button)               #place rock button
    window.blit(rock_words, (72, 122))                              #place rock name
    pygame.draw.rect(window, blackcolor, h_box)                     #place horizontal box
    pygame.draw.rect(window, blackcolor, vert_box)                  #place vertical box
    pygame.draw.rect(window, blackcolor, title_box)                 #place title box
    window.blit(title_words, (title_box.x + 200, title_box.y + 10))  #place title words
    window.blit(computer_words, (300,125))                          #place computer name
    window.blit(player_words, (300,425))                            #place player name

    #exit number 2 button
    exit_box_2 = pygame.Rect(875,625,100,50)
    pygame.draw.rect(window, bluecolor, exit_box_2)
    exits = "EXIT"
    exits_words = font.render(exits, True, whitecolor)
    window.blit(exits_words, (exit_box_2.x + 6, exit_box_2.y + 10))
    
    pScore = 0
    cScore = 0
    
    player = ""
    run = True
    while run:

        time.tick(fps)

        #Events that cause things to happen
        for event in pygame.event.get():

            #X button clicked
            if event.type == pygame.QUIT:
                run = False

            #Button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                        
                    
                

                #Player = rock
                if rock_button.collidepoint(event.pos):
                    comp = random.choice(action)
                    player = "rock"
                    if comp == player:
                        gametie()
                    elif comp == "lizard" or comp == "scissors":
                        playerwin()
                        pScore += 1
                        pygame.draw.rect(window, whitecolor, p_cover)
                        pScore_words = font.render( str(pScore), True, blackcolor)
                        window.blit(pScore_words, (450,425))
                        
                    else:
                        compwin()
                        cScore += 1
                        pygame.draw.rect(window, whitecolor, c_cover)
                        cScore_words = font.render( str(cScore), True, blackcolor)
                        window.blit(cScore_words, (500,125))
                    playerchoice("rock")
                    changegreen("rock")
                    comp = comp.upper()
                    pygame.draw.rect(window, whitecolor, c_choice_cover)
                    comp_choice_words = largeFont.render(comp, True, blackcolor)
                    window.blit(comp_choice_words, (375,200))


                #Player = paper
                if paper_button.collidepoint(event.pos):
                    comp = random.choice(action)
                    player = "paper"
                    if comp == player:
                        gametie()
                    elif comp == "rock" or comp == "spock":
                        playerwin()
                        pScore += 1
                        pygame.draw.rect(window, whitecolor, p_cover)
                        pScore_words = font.render( str(pScore), True, blackcolor)
                        window.blit(pScore_words, (450,425))
                    else:
                        compwin()
                        cScore += 1
                        pygame.draw.rect(window, whitecolor, c_cover)
                        cScore_words = font.render( str(cScore), True, blackcolor)
                        window.blit(cScore_words, (500,125))
                    playerchoice("paper")
                    changegreen("paper")
                    comp = comp.upper()
                    pygame.draw.rect(window, whitecolor, c_choice_cover)
                    comp_choice_words = largeFont.render(comp, True, blackcolor)
                    window.blit(comp_choice_words, (375,200))

                #Player = scissors
                if sci_button.collidepoint(event.pos):
                    comp = random.choice(action)
                    player = "scissors"
                    if comp == player:
                        gametie()
                    elif comp == "paper" or comp == "lizard":
                        playerwin()
                        pScore += 1
                        pygame.draw.rect(window, whitecolor, p_cover)
                        pScore_words = font.render( str(pScore), True, blackcolor)
                        window.blit(pScore_words, (450,425))
                    else:
                        compwin()
                        cScore += 1
                        pygame.draw.rect(window, whitecolor, c_cover)
                        cScore_words = font.render( str(cScore), True, blackcolor)
                        window.blit(cScore_words, (500,125))
                    playerchoice("scissors")
                    changegreen("scissors")
                    comp = comp.upper()
                    pygame.draw.rect(window, whitecolor, c_choice_cover)
                    comp_choice_words = largeFont.render(comp, True, blackcolor)
                    window.blit(comp_choice_words, (375,200))
                    

                #Player = lizard
                if liz_button.collidepoint(event.pos):
                    comp = random.choice(action)
                    player = "lizard"
                    if comp == player:
                        gametie()
                    elif comp == "paper" or comp == "spock":
                        playerwin()
                        pScore += 1
                        pygame.draw.rect(window, whitecolor, p_cover)
                        pScore_words = font.render( str(pScore), True, blackcolor)
                        window.blit(pScore_words, (450,425))
                        
                    else:
                        compwin()
                        cScore += 1
                        pygame.draw.rect(window, whitecolor, c_cover)
                        cScore_words = font.render( str(cScore), True, blackcolor)
                        window.blit(cScore_words, (500,125))
                    playerchoice("lizard")
                    changegreen("lizard")
                    comp = comp.upper()
                    pygame.draw.rect(window, whitecolor, c_choice_cover)
                    comp_choice_words = largeFont.render(comp, True, blackcolor)
                    window.blit(comp_choice_words, (375,200))


                #Player = spock
                if spock_button.collidepoint(event.pos):
                    comp = random.choice(action)
                    player = "spock"
                    if comp == player:
                        gametie()
                    elif comp == "rock" or comp == "scissors":
                        playerwin()
                        pScore += 1
                        pygame.draw.rect(window, whitecolor, p_cover)
                        pScore_words = font.render( str(pScore), True, blackcolor)
                        window.blit(pScore_words, (450,425))
                    else:
                        compwin()
                        cScore += 1
                        pygame.draw.rect(window, whitecolor, c_cover)
                        cScore_words = font.render( str(cScore), True, blackcolor)
                        window.blit(cScore_words, (500,125))
                    playerchoice("spock")
                    changegreen("spock")
                    comp = comp.upper()
                    pygame.draw.rect(window, whitecolor, c_choice_cover)
                    comp_choice_words = largeFont.render(comp, True, blackcolor)
                    window.blit(comp_choice_words, (375,200))

                #Exit number 2
                if exit_box_2.collidepoint(event.pos):
                    
                    #White Screen
                    pygame.draw.rect(window, whitecolor, cover_screen)
                    #title box
                    pygame.draw.rect(window, blackcolor, title_box)
                    window.blit(title_words, (title_box.x + 200, title_box.y + 10))  #place title words
                    #You scored
                    you = "You scored:"+ " " + str(pScore)
                    you_words = font.render(you, True, bluecolor)
                    window.blit(you_words, (325,300))
                    #Comp socred
                    comps = "Computer scored:"+ " " + str(cScore)
                    comps_words = font.render(comps, True, bluecolor)
                    window.blit(comps_words, (325,350))
                    #Who win
                    if pScore > cScore:
                        youwin = "YOU WIN"
                        youwin_words = largeFont.render(youwin, True, bluecolor)
                        window.blit(youwin_words, (275,400))
                    elif pScore < cScore:
                        youlost = "YOU LOSE"
                        youlost_words = largeFont.render(youlost, True, bluecolor)
                        window.blit(youlost_words, (250,400))
                    else:
                        youtie = "YOU TIE"
                        youtie_words = largeFont.render(youtie, True, bluecolor)
                        window.blit(youtie_words, (300,400))
                    


        

        pygame.display.update()                                         #update the window

    pygame.quit()


intro()
