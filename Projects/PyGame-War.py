import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN|pygame.SCALED)
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

exit_menu = False
while not done:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    while exit_menu is False:
        color = (0, 255, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        if pressed[pygame.K_q]:
            done = True
        if pressed[pygame.K_q]:
            exit_menu = True
    if pressed[pygame.K_UP]: y -= 9
    if pressed[pygame.K_DOWN]: y += 9
    if pressed[pygame.K_LEFT]: x -= 9
    if pressed[pygame.K_RIGHT]: x += 9
    if pressed[pygame.K_q]: done = True
    screen.fill((0, 0, 0))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    pygame.display.flip()
    clock.tick(60)
