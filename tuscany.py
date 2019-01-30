#!/usr/bin/env python
from textadventure import *
import sys
# suppress pygame import messages
with open(os.devnull, 'w') as devnull:
    stdout = sys.stdout
    sys.stdout = devnull
    import pygame
    sys.stdout = stdout
from pygame.mixer import music

colors(
    Count = FG.CYAN,
    Dream_Theater = FG.BLUE,
    Count_of_Tuscany = FG.CYAN,
    Car = FG.RED,
    Run = FG.GREEN,
    Item = FG.MAGENTA,
    Quit = BG.RED + FG.BLACK,
)

def quit(**kwargs):
    return None

def use(**kwargs):
    # TODO: get item to use
    clear()
    item = input('Which item? ')
    # input()
    return (back(kwargs), {'use': item})

def hospital(**kwargs):
    out("Next thing you know, you wake up in a hospital. You see a man without a face.")
    out("He said, \"Son do you remember, do you even know your name?\"")
    
    out("He shined a light into your eyes and said \"Take this for the pain.\n")

    out("Hopelessly drifting, bathing in beautiful agony.\n")

    pause("The End. Try Again.")
    return None

def angry(**kwargs):
    out("The count crashes the car!\n")
    pause()
    return hospital

def estate(**kwargs):
    pause()
    return None

def hills(**kwargs):
    out("Winding through the hills, the city far behind.")
    out("Down narrow streets and dusty roads.")
    out("At last we came upon...\n")
    return choice([
        ('c','a castle',None),
        ('m','muh bruthuh',None),
        ('r','ravesnkill',None),
        ('e','an estate',estate),
    ])

def dark(**kwargs):
    out("You burned with the thirst to seek things not yet seen?\n")
    out("Perhaps you were drawn to the beckoning light of the")
    out("Dark Enternal Night\n")
    pause("The End. Try Again.")
    return None

def car(**kwargs):
    out("\"Maybe you'll recall the character inspired by muh bruthuh's life?\"\n")
    return choice([
        ('b','Bearded gentlemen',angry),
        ('h','Historian',angry),
        ('s','Saint behind the altar',angry),
        ('c','Cannibal curator',hills),
        ('d','Dark eternal knight',dark),
    ])

def run(**kwargs):
    out("I touched the one that made me Run,")
    out("Away from my own soul.")
    out("In this game of many decisions,")
    out("We are moving like mice through a maze.")
    out('')
    pause('The End. Try Again.')
    return None

def vocals(**kwargs):
    if MUSIC: music.play(0, (60 * 4 + 39))
    
    out("Several years ago, in a foreign town, far away from home, you met the Count_of_Tuscany.")
    out("A young eccentric man bred from royal blood.\n")
    out("The Count says, \"Get into my car, let's go for a drive. Along the way I'll be your guide, just step inside!\"\n")
    out("Would you like to go for a ride across the open country side?\n")
    
    return choice([
        ('c', 'Get into his Car', car),
        ('r', 'Run', run),
    ])

def welcome(**kwargs):
    if MUSIC: music.play(0,0)
    out("Welcome to Tuscany.exe")
    out("")
    out('This game will play and sync to the '+FG.BLUE+'8-bit version'+FG.RESET+
        ' of Count_of_Tuscany by Dream_Theater, which you can get from YouTube.')
    out('')
    out('Name this file ' +FG.YELLOW + 'tuscany.mp3' + FG.RESET + '.')
    out('\n')
    pause()
    return vocals
    
choices([
    ('u', 'Use Item', use),
    ('q', 'Quit', quit)
])

if __name__=='__main__':
    pygame.mixer.init()
    
    try:
        music.load('tuscany.mp3')
        MUSIC = True
    except pygame.error:
        MUSIC = False
    
    start(welcome)

