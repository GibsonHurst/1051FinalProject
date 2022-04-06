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
blackcolor = (0,0,0)

#window
width = 1000
height = 700
window = pygame.display.set_mode((width, height))
window.fill(whitecolor)
fps = 60
time = pygame.time.Clock()
font = pygame.font.Font(None, 50)

#title box
title = "Rock Paper Scissors Lizard Spock"
title_box = pygame.Rect(25,25,750,50)
title_words = font.render(title, True, whitecolor)

#vertical box
vert_box = pygame.Rect(250,100,25,575)

#horizontal box
h_box = pygame.Rect(275,375,700,25)

#computer name
computer_name = "Computer:"
computer_words = font.render(computer_name, True, blackcolor)

#player name
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

def gametie():
    tie = "TIE"
    tie_words = font.render(tie, True, redcolor)
    window.blit(tie_words, (300,500))
    


def game():

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
        

        pygame.draw.rect(window, blackcolor, spock_button)              #place spock button
        window.blit(spock_words, (spock_button.x +35, spock_button.y +22))  #place spock name
        pygame.draw.rect(window, blackcolor, liz_button)                #place lizard button
        window.blit(liz_words, (liz_button.x +37, liz_button.y +22))    #place lizard name
        pygame.draw.rect(window, blackcolor, sci_button)                #place scissors button
        window.blit(sci_words, (sci_button.x +10, sci_button.y +22))    #place scissors name
        pygame.draw.rect(window, blackcolor, paper_button)              #place paper button
        window.blit(paper_words,(paper_button.x +37,paper_button.y +22))#place paper name
        pygame.draw.rect(window, blackcolor, rock_button)               #place rock button
        pygame.draw.rect(window, blackcolor, h_box)                     #place horizontal box
        pygame.draw.rect(window, blackcolor, vert_box)                  #place vertical box
        pygame.draw.rect(window, blackcolor, title_box)                 #place title box
        window.blit(title_words, (title_box.x + 80, title_box.y + 10))  #place title words
        window.blit(computer_words, (300,125))                          #place computer name
        window.blit(player_words, (300,425))                            #place player name
        window.blit(rock_words, (72, 122))                              #place rock name

        pygame.display.update()                                         #update the window

    pygame.quit()


game()
