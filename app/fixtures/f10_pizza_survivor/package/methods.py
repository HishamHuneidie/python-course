from pathlib import Path

import pygame
from pygame.event import EventType

from .constants import game_config


def play(events: list[EventType]):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_config['deliver'].shoot()

    if game_config['enemy_father'].is_time_exceded():
        game_config['enemy_father'].new_enemy()

    game_config['deliver'].move(pygame.key.get_pressed())
    game_config['deliver'].update()
    game_config['enemy_father'].update()


def show_end():
    if game_config['end_time'] is None: game_config['end_time'] = pygame.time.get_ticks()

    living_time = format_time(game_config['end_time'] - game_config['start_time'])

    game_config['game_over_title'].show()
    stats_text = game_config['new_end_text'](living_time)
    stats_text.show()


def format_time(ms) -> str:
    total_seconds = ms // 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return f'{minutes:02}:{seconds:02}'


def complete_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / filename


def locate(coordinates, object_size):
    return (
        coordinates[0] - (object_size[0] / 2),
        coordinates[1] - (object_size[1] / 2),
    )
