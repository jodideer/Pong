import pygame, sys
from pygame.locals import *



def main():
    pygame.init()

    #frames per second
    fps=250

    window_width=800
    window_height=550
    linethickness=15
    paddlesize=90
    paddledistance=20

    white=(255,255,255) #256th element of red, green and blue (red, green and blue combined makes white)
    black=(0,0,0)
    blue=(0,0,255)
    green=(0,255,0)
    red=(255,0,0)

    global displaysurf
    global basicfont,basicfontsize


    def drawArena():
        displaysurf.fill(black)
        pygame.draw.line(displaysurf,white,((window_width/2),0),((window_width/2),window_height),(linethickness/4))


    def drawPaddle(paddle):
        #stops paddle from moving too low
        if paddle.bottom > (window_height-linethickness):
            paddle.bottom = (window_height-linethickness)
            
        #stops paddles from moving too high
        elif paddle.top < linethickness:
            paddle.top = linethickness

        pygame.draw.rect(displaysurf,white,paddle)
        

    def aipaddle(ball, ballDirX, paddle2):
        if ballDirX == -1 or ballDirX == 1:
            if paddle2.centery < ball.centery:
                paddle2.y += 1
            else:
                paddle2.y -= 1
        return paddle2


    def drawBall(ball):
        pygame.draw.rect(displaysurf,white,ball)


    def moveBall(ball,ballDirX,ballDirY):
        ball.x += ballDirX 
        ball.y += ballDirY
        return ball
    

    def checkedgecoll(ball,ballDirX,ballDirY):

        if ball.left==(linethickness) or ball.right==(window_width-linethickness):
            ballDirX=ballDirX * -1
            
        if ball.top==(linethickness) or ball.bottom==(window_height-linethickness):
            ballDirY=ballDirY * -1
            
        return ballDirX,ballDirY


    def checkpaddlecoll(ball,paddle1,paddle2, ballDirX):
        if ballDirX == -1 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
            return -1
        
        elif ballDirX == 1 and paddle2.left == ball.right and paddle2.top < ball.top and paddle2.bottom > ball.bottom:
            return -1
        
        else:
            return 1


    def checkPoints(paddle1, ball, score, ballDirX):
        #reset points if left wall is hit
        if ball.left == linethickness:
            return 0
        
        #1 point for hitting the ball
        elif ballDirX == -1 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
            score += 1
            return score
        
        #5 points for beating the other paddle
        elif ball.right == window_width - linethickness:
            score += 5
            return score
        
        #if no points scored, return score unchanged
        else:
            return score


    def display(ball,score,paddle1):
        resultSurf = basicfont.render('SCORE = %s' %(score), True, blue)    
        resultRect = resultSurf.get_rect()
        resultRect.topleft = (window_width - 150, 25)
        displaysurf.blit(resultSurf, resultRect)

        if score==0:
            resultSurf = basicfont.render('YOU LOSE :(', True, red)
            resultRect = resultSurf.get_rect()
            resultRect.topleft = (window_width - 670, 25)
            displaysurf.blit(resultSurf, resultRect)

        if score>=5:
            resultSurf = basicfont.render('YOU WIN!!!', True, green)
            resultRect = resultSurf.get_rect()
            resultRect.topleft = (window_width - 670, 25)
            displaysurf.blit(resultSurf, resultRect)

     
    
    basicfontsize=20
    basicfont = pygame.font.Font('freesansbold.ttf', basicfontsize)


    fpsclock = pygame.time.Clock()
    displaysurf = pygame.display.set_mode((window_width,window_height)) 
    pygame.display.set_caption('Pong')


    #initiate variable and set starting positions in the centre
    ball_X = window_width/2 - linethickness/2
    ball_Y = window_height/2 - linethickness/2
    p_one_pos = (window_height - paddlesize)/2
    p_two_pos = (window_height - paddlesize)/2
    score=1


    ## -1 = left  and 1 = right
    ## -1 = up  and  1 = down
    ballDirX = -1  
    ballDirY = -1  


    #(x coordinate,y coordinate, width, length)
    paddle1 =  pygame.Rect(paddledistance,p_one_pos,linethickness,paddlesize)
    paddle2 = pygame.Rect(window_width - paddledistance - linethickness, p_two_pos,linethickness,paddlesize)
    ball = pygame.Rect(ball_X, ball_Y, linethickness, linethickness)



    #while main is true:
    while True: 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()  

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                        paddle1.y -= 30
                if event.key==pygame.K_DOWN:
                        paddle1.y += 30             


        drawArena()
        drawPaddle(paddle1)
        
        drawPaddle(paddle2)
        drawBall(ball)
        
        ball=moveBall(ball,ballDirX,ballDirY)
        ballDirX,ballDirY = checkedgecoll(ball,ballDirX,ballDirY)
        
        score = checkPoints(paddle1, ball, score, ballDirX)
        ballDirX = ballDirX * checkpaddlecoll(ball,paddle1,paddle2,ballDirX)
        
        paddle2 = aipaddle(ball,ballDirX,paddle2)
        display(ball,score,paddle1)

        pygame.display.update()
        fpsclock.tick(fps)


if __name__== '__main__':
    main()

