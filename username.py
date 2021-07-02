import pygame, sys
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
font = pygame.font.SysFont('cambria', 28)
font2 = pygame.font.SysFont('cambira', 40)
username1=""
text2=font.render("Enter your username: ", True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                username1 = username1[:-1]
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.quit()
            elif event.key == pygame.K_SPACE:
                print(username1)
                running=False
            else:
                username1+=event.unicode
    screen.fill((0,0,0))
    text_surface=font.render(username1, True, (255, 255, 255))
    screen.blit(text_surface, (0,40))
    screen.blit(text2, (0,0))
    pygame.display.flip()
    clock.tick(60)


