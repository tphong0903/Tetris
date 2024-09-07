import pygame,sys
from game import Game
pygame.init()

titleFont = pygame.font.Font(None,40)
score_surface = titleFont.render("Score", True, (255,255,255))
next_surface = titleFont.render("Next", True, (255,255,255))
game_over_surface = titleFont.render("GAME OVER", True, (255,255,255))

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500,620))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

gameUpdate = pygame.USEREVENT
normalDropTime = 400
fastDropTime = 30
dropTime = normalDropTime
pygame.time.set_timer(gameUpdate, dropTime)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.gameOver == True:
                game.gameOver = False
                game.reset()
            if event.key == pygame.K_LEFT and game.gameOver == False:
                game.moveLeft()
            if event.key == pygame.K_RIGHT and game.gameOver == False:
                game.moveRight()
            if event.key == pygame.K_DOWN and game.gameOver == False:
                dropTime = fastDropTime
                pygame.time.set_timer(gameUpdate, dropTime)
                game.moveDown(gameUpdate)
                game.updateScore(0)
            if event.key == pygame.K_SPACE and game.gameOver == False:
                dropTime = 5
                pygame.time.set_timer(gameUpdate,dropTime)
                game.moveDown(gameUpdate)
            if event.key == pygame.K_UP and game.gameOver == False:
                game.rotate()
        if event.type == pygame.KEYUP and game.gameOver == False:
            if  event.key == pygame.K_DOWN:
                dropTime = normalDropTime
                pygame.time.set_timer(gameUpdate, dropTime)
        if event.type == gameUpdate and game.gameOver == False:
            game.moveDown(gameUpdate)
   
    # Draw
    # 10 Columnm, 20 Row
    score_value_surface = titleFont.render(str(game.score), True, (255,255,255))

    screenColor = (44,44,127)
    screen.fill(screenColor)
    screen.blit(score_surface,(365,20,50,50))
    screen.blit(next_surface, (375, 180, 50, 50))
    if (game.gameOver == True):
        screen.blit(game_over_surface, (320, 450, 50, 50))
          
    pygame.draw.rect(screen,(59, 85, 162), score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, (59, 85, 162), next_rect, 0, 10)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
