import pygame
import time
import threading
import os

# //Init
pygame.init()

WIDTH, HEIGHT = 800, 800; # constant variables
WIN = pygame.display.set_mode((WIDTH, HEIGHT)); # Window init and dimensions set
pygame.display.set_caption("Crow"); # Caption == Name of window

# //Background image
BG = pygame.transform.scale(pygame.image.load("resources/background_image/dog.jpg"), (WIDTH, HEIGHT)); # Loading an image and referencing the playerob with the constant BG

# // Player playerob properties
PLAYER_WIDTH = 50;
PLAYER_HEIGHT = 50;
PLAYER_VELOCITY = 5;

def draw(playerob):
    WIN.blit(BG, (0,0)); # blit is a method to draw images or surfaces on the window
    #player = pygame.draw.circle(WIN, (255, 0, 0), (400, HEIGHT - PLAYER_HEIGHT), PLAYER_WIDTH, 0); # drawing a solid circle
    pygame.draw.rect(WIN, (150, 0, 0), playerob)
    pygame.display.update(); # Updates the display so any drawings made prior can apply

# //Main entry and foundation of the program
def main():
    gameloop = True;
    # Debugging mode
    debugm = True;
    runonce = True;

    playerob = pygame.Rect(400, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT);

    while (gameloop):
        # Passing functionality to the X Button
        for Event in (pygame.event.get()):
            if (Event.type == pygame.QUIT):
                gameloop = False;
                break;
        
        draw(playerob);

        keycodes = pygame.key.get_pressed();
        # Movement keys and player boundaries
        if (keycodes[pygame.K_d] and playerob.x + PLAYER_VELOCITY + playerob.width <= WIDTH):
            playerob.x = playerob.x + PLAYER_VELOCITY;
        if (keycodes[pygame.K_a] and playerob.x - PLAYER_VELOCITY >= 0):
            playerob.x = playerob.x - PLAYER_VELOCITY;
        if (keycodes[pygame.K_SPACE] and playerob.y - PLAYER_VELOCITY >= 0):
            playerob.y = playerob.y - PLAYER_VELOCITY;
        if (keycodes[pygame.K_s] and playerob.y + PLAYER_VELOCITY + playerob.width <= HEIGHT):
            playerob.y = playerob.y + PLAYER_VELOCITY;

        if debugm:
            if (runonce):
                print("Player Coordinates: (x: {0}p, y: {1}p)".format(playerob.x, playerob.y));
                poc = (playerob.y, playerob.x);

            runonce = False;
            if (playerob.x != poc[1]):
                os.system("clear");
                print("Player Coordinates: (x: {0}p, y: {1}p)".format(playerob.x, playerob.y));
                poc = (playerob.y, playerob.x);

        time.sleep(0.01);

    pygame.quit();


# //Standard boilerplate
if (__name__ == "__main__"):
    print("module was ran directly");
    thread = threading.Thread(target=main);
    thread.start();
