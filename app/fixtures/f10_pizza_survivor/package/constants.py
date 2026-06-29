from pathlib import Path

import pygame


class ObjectCreator:
    @staticmethod
    def create_enemy_father():
        from .Objects import EnemyFather
        return EnemyFather()

    @staticmethod
    def create_deliver():
        from .Objects import Player
        return Player(
            coordinates=(game_config['scree_size'][0] / 2, game_config['scree_size'][1] / 2),
            image_path=complete_path('pizza-deliver.png'),
            size=(100, 100),
            speed=1,
            lives=1
        )

    @staticmethod
    def create_game_over_title():
        from .Objects import Text
        return Text('GAME OVER!!', 60, (275, 30))

    @staticmethod
    def create_end_text(living_time: str):
        from .Objects import Text
        return Text(f'Living time was: {living_time}', 35, (260, 20), (400, 350))


def complete_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / filename


def init():
    game_config['game_over_title'] = ObjectCreator.create_game_over_title()
    game_config['deliver'] = ObjectCreator.create_deliver()
    game_config['enemy_father'] = ObjectCreator.create_enemy_father()

    hit_sound = pygame.mixer.Sound(complete_path('hit.wav'))
    hit_sound.set_volume(0.8)
    life_lost_sound = pygame.mixer.Sound(complete_path('life_lost.wav'))
    life_lost_sound.set_volume(0.8)
    shot_sound = pygame.mixer.Sound(complete_path('shot.wav'))
    shot_sound.set_volume(0.8)

    game_config['hit_sound'] = hit_sound
    game_config['life_lost_sound'] = life_lost_sound
    game_config['shot_sound'] = shot_sound

    return game_config


scree_size = (800, 600)

game_config = {
    'scree_size': scree_size,
    'screen': pygame.display.set_mode(scree_size),
    'text_color': (255, 0, 0),
    'maximum_lives': 5,
    'vulnerability_interval': 5000,
    'enemies_interval': 5000,
    'is_running': True,
    'game_over': False,
    'start_time': pygame.time.get_ticks(),
    'end_time': None,
    'game_over_title': None,
    'deliver': None,
    'enemy_father': None,
    'hit_sound': None,
    'life_lost_sound': None,
    'shot_sound': None,
    'new_end_text': ObjectCreator.create_end_text,
    'init': init,
}
