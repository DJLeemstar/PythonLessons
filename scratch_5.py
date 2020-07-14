import pygame

class Player (pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        width = 50
        height = 50

        self.image = pygame.Surface((width, height))
        self.image.fill((150, 0, 0))
        self.rect = self.image.get_rect()

    def update(self):

        pos = pygame.mouse.get_pos()

        x = pos[0]
        y = pos[1]

        self.rect.x = x
        self.rect.y = y


pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Mouse Movement Test")
running = True
ourPlayer = Player()

sprites = pygame.sprite.Group()
sprites.add(ourPlayer)

# pygame.mouse.set_visible(False)

while running:

    # pygame.time.wait(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sprites.update()
    screen.fill((0, 0, 0))
    sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
