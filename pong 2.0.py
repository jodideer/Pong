import pygame, sys
pygame.init()
from pygame.locals import *

#frames per second
fps=200

window_width=800
window_height=550
linethickness=10
paddlesize=90
paddledistance=20

white=(255,255,255) #256th element of red, green and blue (red, green and blue combined makes white)
black=(0,0,0)



def drawArena():
    displaysurf.fill((0,0,0))
##    pygame.draw.rect(displaysurf,white,((0,0),(wwidth,wheight)),linethickness*2)

    #draw the line in the centre
    pygame.draw.line(displaysurf,white,((window_width/2),0),\
                     ((window_width/2),window_height),(linethickness/4))


def drawPaddle(paddle):
    #stops paddle from moving too low
    if paddle.bottom > (window_height-linethickness):
        paddle.bottom = (window_height-linethickness)
        
    #stops paddles from moving too high
    elif paddle.top < linethickness:
        paddle.top = linethickness

    pygame.draw.rect(displaysurf,white,paddle)


def drawBall(ball):
    pygame.draw.rect(displaysurf,white,ball)


def moveBall(ball,ballDirX,ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
    return ball


def main():
    pygame.init()
    global displaysurf
    fpsclock=pygame.time.Clock()
    displaysurf=pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption('PONG')


    #initiate variable and set starting positions
    #any future changes made within rectangles
    #these put them in the centre
    ball_X = window_width/2 - linethickness/2
    ball_Y = window_height/2 - linethickness/2
    p_one_pos = (window_height - paddlesize)/2
    p_two_pos = (window_height - paddlesize)/2

    ballDirX = -1 ## -1 = left  and 1 = right
    ballDirY = -1 ## -1 = up  and  1 = down


    #(x coordinate,y coordinate, width, length)
    paddle1 =  pygame.Rect(paddledistance,p_one_pos,linethickness,paddlesize)
    paddle2 = pygame.Rect(window_width - paddledistance - linethickness, p_two_pos,\
                          linethickness,paddlesize)
    ball = pygame.Rect(ball_X, ball_Y, linethickness, linethickness)

    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)

    #while main is true:
    while True: 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        drawArena()
        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)

        ball=moveBall(ball,ballDirX,ballDirY)
        
        pygame.display.update()
        fpsclock.tick(fps)


if __name__== '__main__':
    main()


















