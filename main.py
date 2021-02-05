import pygame
import sys
import random

pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((1280, 768))  # Sets resolution.

screenWidth = 1280
screenHeight = 768

clock = pygame.time.Clock()  # Built-in function that enables frame-rate control.
cloud = pygame.image.load("cloud.png")  # Loading an image from a file. Put the file inside the project folder.
human = pygame.image.load("human_umbrella.png")

humanXPos = 0
humanYPos = 570


class Raindrop:

    def __init__(self, x, y, colour):  # On initiation, give the raindrops these values. These are randomised ONE TIME per instance of raindrop.
        self.xPosition = x
        self.yPosition = y
        self.size = random.randint(1, 5)
        self.speed = random.randint(5, 20)
        self.colour = colour

    def draw(self):  # Called every frame, takes the values from initialisation. Different for each instance of raindrop.
        pygame.draw.circle(screen, self.colour, (self.xPosition, self.yPosition), self.size)

    def move(self):  # Called every frame, takes the values from initialisation. Different for each instance of raindrop.
        self.yPosition += self.speed


class Cloud:

    def __init__(self):
        self.xCloudPos = random.randint(-500, 600)  # Create cloud position here, use directly in raindrop creation to avoid global variables.
        self.yCloudPos = -200  # Create cloud position here, use directly in raindrop creation to avoid global variables.
        self.size = random.randint(1, 2)

    def draw(self):  # Called every frame, takes the values from initialisation. Different for each instance of raindrop.
        screen.blit(cloud, (self.xCloudPos, self.yCloudPos))  # Put the cloud on the screen.

    def move(self):  # Called every frame, takes the values from initialisation. Different for each instance of raindrop.
        self.xCloudPos += 2

    def spawn_rain(self):
        raindropsList.append(Raindrop((random.randint(self.xCloudPos + 150, self.xCloudPos + 900)), self.yCloudPos + 400, (255, 255, 255)))  # Add the raindrop instance to a list.



raindropsList = []  # MUST be defined outside the while loop, otherwise list is erased every frame (duh).

cloudInstance = Cloud()

while True:

    clock.tick(60)  # Setting the frame-rate.
    for event in pygame.event.get():  # See the pygame user guide for various events (e.g. get button down).
        if event.type == pygame.QUIT:
            sys.exit()

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        humanXPos -= 10

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        humanXPos += 10

    # Rendering section (order matters).
    screen.fill((150, 150, 150))  # Filling the screen with a colour.

    raindrop = Raindrop(random.randint(0, screenWidth), 0, (100, 100, 100))
    raindropsList.append(raindrop)

    for droplet in raindropsList:  # Iterate through the list.
        if droplet.yPosition >= screenHeight:  # Check the position of each droplet.
            raindropsList.remove(droplet)  # Delete the droplets if they cross the bottom border.
        else:
            droplet.draw()  # If the droplet isn't below the bottom border, draw it on screen.
            droplet.move()  # Also move its position.

        if cloudInstance.xCloudPos >= screenWidth:  # Check the position of each droplet.
            cloudInstance.xCloudPos = -1000  # Delete the droplets if they cross the bottom border.
    cloudInstance.draw()
    cloudInstance.move()
    cloudInstance.spawn_rain()


    screen.blit(human, (humanXPos, humanYPos))

    pygame.display.flip()  # 2 buffers: stuff that's going to draw, stuff that's already drawn. Flip turns the two.
