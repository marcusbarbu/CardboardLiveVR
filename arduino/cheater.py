import pygame
import requests



def up():
    r = requests.post("http://192.168.2.24:5000/up")
    print "whatever"
def down():
    r = requests.post("http://192.168.2.24:5000/down")
def left():
    r = requests.post("http://192.168.2.24:5000/left")
def right():
    r = requests.post("http://192.168.2.24:5000/right")
    
pygame.init()
pygame.display.set_mode()
while True:
    for event in pygame.event.get():
        print event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left()
            elif event.key == pygame.K_RIGHT:
                right()
            elif event.key == pygame.K_UP:
                r = requests.post("http://192.168.2.24:5000/up")
            elif event.key == pygame.K_DOWN:
                down()