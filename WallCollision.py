import pygame

screenWidth = 800
screenHeight = 600

colourBlack = (0, 0, 0)
colourRed = (255, 0, 0)
colourWhite = (255, 255, 255)

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):

        # super() gets the attributes of the inherited property.
        # In this case, inherits from the Sprite object from pygame.

        super().__init__()

        self.image = pygame.Surface((30, 30))
        self.image.fill(colourWhite)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.xSpeed = 0
        self.ySpeed = 0
        self.wallCollisions = None

    def changeSpeed(self, x, y):
        self.xSpeed += x
        self.ySpeed += y

    def update(self):

        # Check for horizontal movement and collisions

        self.rect.x += self.xSpeed

        wallCollisionsList = pygame.sprite.spritecollide(self, self.wallCollisions, False)
        for wall in wallCollisionsList:
            if self.xSpeed > 0:
                # This means we are moving right
                # Therefore, we adjust as necessary
                self.rect.right = wall.rect.left

            else:
                # Otherwise, we are moving left
                # Therefore, we adjust as necessary
                self.rect.left = wall.rect.right

        # Check for vertical movement and collisions

        self.rect.y += self.ySpeed

        wallCollisionsList = pygame.sprite.spritecollide(self, self.wallCollisions, False)

        for wall in wallCollisionsList:
            if self.ySpeed > 0:
                # We are moving downwards
                # So we adjust as needed

                self.rect.bottom = wall.rect.top

            else:
                # We are moving upwards
                # So we adjust as needed

                self.rect.top  = wall.rect.bottom


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):

        super().__init__()

        # This makes it so the wall size depends on what we input
        self.image = pygame.Surface([width, height])
        self.image.fill(colourRed)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Wall Collision")

wall1 = Wall(20, 20, 50, 10)

player1 = Player(100, 100)

wallSprites = pygame.sprite.Group()
wallSprites.add(wall1)

allSprites = pygame.sprite.Group()
allSprites.add(player1)
allSprites.add(wall1)

listOfValues = [(50, 50, 10, 100), (250, 170, 30, 10), (100, 100, 70, 10)]
for i, j, k, l in listOfValues:
    wallSprites.add(Wall(i,j,k,l))
    allSprites.add(Wall(i,j,k,l))

player1.wallCollisions = wallSprites

running = True

while running:
    
    pygame.time.wait(40)

    player1.xSpeed = 0
    player1.ySpeed = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player1.changeSpeed(-3, 0)

    elif keys[pygame.K_RIGHT]:
        player1.changeSpeed(3, 0)

    elif keys[pygame.K_DOWN]:
        player1.changeSpeed(0, 3)

    elif keys[pygame.K_UP]:
        player1.changeSpeed(0, -3)

    allSprites.update()
    screen.fill(colourBlack)
    allSprites.draw(screen)
    pygame.display.flip()

pygame.quit()





