"""
This script is to practice this before the project
"""

import sys
from pathlib import Path

import pygame
from pygame.event import EventType

sys.path.append(str(Path(__file__).resolve().parent.parent))

from packages.colorizer import Colorizer
from packages.colorizer.Colorizer import color_class
from fixtures.f10_pizza_survivor.package import methods as m
from fixtures.f10_pizza_survivor.package.constants import game_config


def print_title(text):
    print()
    print(Colorizer.colorize(text + ':', color_class.GREEN))
    print()


print_title('Py game')

# Init pygame
pygame.mixer.pre_init(
    frequency=44100,
    size=-16,
    channels=2,
    buffer=128,
)
pygame.init()
game_config['init']()

# Fixtures
icon_path = m.complete_path('icon-pizza.png')
bg_path = m.complete_path('fondo.png')
icon = pygame.image.load(icon_path)
bg = pygame.image.load(bg_path)
bg = pygame.transform.scale(bg, game_config['scree_size'])

# Sound fixtures
pygame.mixer.music.load(m.complete_path('bg.mp3'))
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

# Show screen
pygame.display.set_caption('Pizza Survivor')
pygame.display.set_icon(icon)

# Objects
game_config['enemy_father'].new_enemy()

# Game loop
while game_config['is_running']:
    game_config['screen'].blit(bg, (0, 0))
    events: list[EventType] = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            game_config['is_running'] = False

    if game_config['game_over']:
        m.show_end()
    else:
        m.play(events)

    pygame.display.update()

pygame.quit()

print_title('Bye bye')
