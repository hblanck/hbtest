import pygame
import os
import random
import threading
from time import sleep

WHITE = (255,255,255)

#Arrows
UPARROW = chr(int("0x2191",16))
DOUBLE_UPARROW = chr(int("0x21D1",16))
DOWNARROW = chr(int("0x2193",16))
DOUBLE_DOWNARROW = chr(int("0x21D3",16))
STRAIGHTARROW = chr(int("0x2192",16))
DIAGONAL_UP = chr(int("0x2197",16))
DIAGONAL_DOWN = chr(int("0x2198",16))
arrows = [UPARROW,DOUBLE_UPARROW,DOWNARROW,DOUBLE_DOWNARROW,STRAIGHTARROW,DIAGONAL_UP,DIAGONAL_DOWN]


os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
lcd=pygame.display.set_mode((480, 320))
lcd.fill((0,0,255))
font_big = pygame.font.Font(None, 250)

def theThread():
        global lcd, pygame
        font_smaller = pygame.font.Font(None, 75)
        while True:
            small_text = str(random.randint(2, 15)) + " Minutes Ago"
            small_text_surface = font_smaller.render(small_text, True, (255,255,255))
            rect2 = small_text_surface.get_rect(center=(200,30))
            lcd.blit(small_text_surface, rect2)
            pygame.display.update()
            sleep(5)
            clear_text_surface = font_smaller.render(small_text, True, (0,0,255))
            rect3 = clear_text_surface.get_rect(center=(200,30))
            lcd.blit(clear_text_surface, rect3)
            pygame.display.update()

MinutesAgoThread=threading.Thread(target=theThread)
MinutesAgoThread.setName('MinutesAgo')
MinutesAgoThread.start()

while True:
	text_surface = font_big.render(str(random.randint(45, 350))+arrows[random.randint(0,6)], True, WHITE)
	rect = text_surface.get_rect(center=(225,160))
	lcd.blit(text_surface, rect)
	pygame.display.update()
	pygame.mouse.set_visible(False)
	sleep(25)
	lcd.fill((0,0,255))
	pygame.display.update()

