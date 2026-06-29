"""
This script is to practice this before the project
"""

import sys
from pathlib import Path
import pygame
from jinja2 import UndefinedError
from pygame.event import EventType
from pygame.key import ScancodeWrapper
from random import randint, choice

from pygame.surface import SurfaceType

sys.path.append(str(Path(__file__).resolve().parent.parent))

from packages.colorizer import Colorizer
from packages.colorizer.Colorizer import color_class


def play(events: list[EventType]):
    global is_running

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                deliver.shoot()

    if enemy_father.is_time_exceded():
        enemy_father.new_enemy()

    deliver.move(pygame.key.get_pressed())
    deliver.update()
    enemy_father.update()


def show_end():
    global game_over_title, end_time

    if end_time is None: end_time = pygame.time.get_ticks()

    living_time = format_time(end_time - start_time)

    game_over_title.show()
    stats_text = Text(f'Living time was: {living_time}', 35, (260, 20), (400, 350))
    stats_text.show()


def format_time(ms) -> str:
    total_seconds = ms // 1000
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    return f'{minutes:02}:{seconds:02}'


def complete_path(filename: str) -> Path:
    return Path(__file__).resolve().parent.parent / 'fixtures' / 'f10_pizza_survivor' / filename


def print_title(text):
    print()
    print(Colorizer.colorize(text+':', color_class.GREEN))
    print()


def locate(coordinates, object_size):
    return (
        coordinates[0] - (object_size[0] / 2),
        coordinates[1] - (object_size[1] / 2),
    )


class GameObject:
    def __init__(self, coordinates: tuple[int|float, int|float], image_path, size: tuple[int|float, int|float]):
        self.coordinates = coordinates
        image = pygame.image.load(image_path)
        self.image: SurfaceType = pygame.transform.scale(image, size)
        self.size = size
        self.limits_h: tuple[int|float, int|float] = (
            0 + (size[0] / 2),
            scree_size[0] - (size[0] / 2),
        )
        self.limits_v: tuple[int|float, int|float] = (
            0 + (size[1] / 2),
            scree_size[1] - (size[1] / 2),
        )


    def locate(self, coordinates):
        self.coordinates = coordinates
        self.limite()
        screen.blit(self.image, locate(self.coordinates, self.size))


    def update(self):
        self.locate(self.coordinates)


    def limite(self):
        if self.coordinates[0] < self.limits_h[0]:
            self.coordinates = (
                self.limits_h[0],
                self.coordinates[1],
            )

        if self.coordinates[0] > self.limits_h[1]:
            self.coordinates = (
                self.limits_h[1],
                self.coordinates[1],
            )

        if self.coordinates[1] < self.limits_v[0]:
            self.coordinates = (
                self.coordinates[0],
                self.limits_v[0],
            )

        if self.coordinates[1] > self.limits_v[1]:
            self.coordinates = (
                self.coordinates[0],
                self.limits_v[1],
            )


    def got_boundary(self):
        if self.coordinates[0] <= self.limits_h[0] or self.coordinates[0] >= self.limits_h[1]:
            return True

        if self.coordinates[1] <= self.limits_v[0] or self.coordinates[1] >= self.limits_v[1]:
            return True

        return False


    def calculate_distance(self, objective: GameObject) -> float:
        diff_x = objective.coordinates[0] - self.coordinates[0]
        diff_y = objective.coordinates[1] - self.coordinates[1]

        return (diff_x ** 2 + diff_y ** 2) ** 0.5


class MovableGameObject(GameObject):
    def __init__(self, coordinates: tuple[int|float, int|float], image_path, size: tuple[int|float, int|float], speed: int|float):
        super().__init__(coordinates, image_path, size)
        self.speed = speed


    def move(self, keys: ScancodeWrapper):
        movement_length = 1
        location = self.coordinates

        if keys[pygame.K_UP]:
            location = (
                location[0],
                location[1] - movement_length,
            )
        if keys[pygame.K_DOWN]:
            location = (
                location[0],
                location[1] + movement_length,
            )
        if keys[pygame.K_RIGHT]:
            location = (
                location[0] + movement_length,
                location[1],
            )
        if keys[pygame.K_LEFT]:
            location = (
                location[0] - movement_length,
                location[1],
            )

        self.coordinates = location
        self.limite()


class LivesOrchestrator:
    def __init__(self, count: int=3):
        self.lives: list[GameObject] = []

        self.image_path = complete_path('heart-icon.png')
        self.width = 30
        self.coordinates_margin = 10
        self.size = (self.width, self.width)

        i = 0
        while i < count:
            self.add()
            i += 1


    def _calculate_life_position(self, life_number: int) -> tuple[int|float, int|float]:
        left_margin = 0
        total_size_per_life = self.width + (self.coordinates_margin * 2)

        x = (total_size_per_life * life_number) + (total_size_per_life / 2) + left_margin
        y = total_size_per_life / 2

        return x, y


    def show(self):
        for life in self.lives:
            life.update()


    def count(self):
        return len(self.lives)


    def kill(self):
        if len(self.lives) == 0: return

        life_lost_sound.play()
        self.lives.remove(self.lives[-1])


    def add(self):
        global maximum_lives

        if self.count() >= maximum_lives: return

        self.lives.append(GameObject(self._calculate_life_position(self.count()), self.image_path, self.size))


    def __str__(self):
        return str(self.count())


class Player(MovableGameObject):
    pizzas: list[Pizza] = []


    def __init__(self, coordinates: tuple[int|float, int|float], image_path, size: tuple[int|float, int|float], speed: int|float, lives: int):
        super().__init__(coordinates, image_path, size, speed)
        self.is_vulnerable = True
        self.last_shot = 0
        self.lives: LivesOrchestrator = LivesOrchestrator(lives)
        self.score = Score(self)


    def choose_enemy(self) -> Enemy|None:
        global enemy_father

        chosen_enemy: Enemy|None = None
        chosen_distance: float|None = None

        for enemy in enemy_father.children:
            distance = self.calculate_distance(enemy)

            if chosen_distance is None or distance < chosen_distance:
                chosen_distance = distance
                chosen_enemy = enemy

        if chosen_enemy is None:
            return None

        return chosen_enemy


    def shoot(self):
        chosen_enemy = self.choose_enemy()

        if chosen_enemy is None: return


        pizza = Pizza(
            player=self,
            image_path=complete_path('icon-pizza.png'),
            size=(50, 50),
            speed=3,
        )


        self.pizzas.append(pizza)


        self.pizzas[-1].shoot(chosen_enemy)


    def update(self):
        now = pygame.time.get_ticks()


        if not self.is_vulnerable and now - self.last_shot > vulnerability_interval:
            self.is_vulnerable = True


        if self.is_vulnerable or ((now // 100) % 2 == 0):
            super().update()


        for pizza in self.pizzas:
            pizza.update()

            if pizza.got_boundary():
                self.pizzas.remove(pizza)


        self.lives.show()
        self.score.show()


    def is_shot(self):
        global game_over

        if not self.is_vulnerable: return

        self.lives.kill()
        self.last_shot = pygame.time.get_ticks()
        self.is_vulnerable = False

        if self.is_death():
            game_over = True
            print('GAME OVER!!!')


    def is_death(self):
        return self.lives.count() == 0


class Enemy(MovableGameObject):
    def run(self):
        distance = self.calculate_distance(deliver)

        if distance <= 0: return

        diff_x = deliver.coordinates[0] - self.coordinates[0]
        diff_y = deliver.coordinates[1] - self.coordinates[1]
        coordinates = (
            self.coordinates[0] + ( (diff_x / distance) * self.speed ),
            self.coordinates[1] + ( (diff_y / distance) * self.speed ),
        )

        self.locate(coordinates)

        if self.has_hit():
            deliver.is_shot()


    def has_hit(self) -> bool:
        enemy_rect = pygame.Rect(
            self.coordinates[0],
            self.coordinates[1],
            self.size[0],
            self.size[1],
        )
        deliver_rect = pygame.Rect(
            deliver.coordinates[0],
            deliver.coordinates[1],
            deliver.size[0],
            deliver.size[1],
        )

        return enemy_rect.colliderect(deliver_rect)


class Pizza(MovableGameObject):
    def __init__(self, player: Player, image_path, size: tuple[int|float, int|float], speed: int):
        super().__init__(player.coordinates, image_path, size, speed)
        self.player = player
        self.objetive: tuple[int|float, int|float] = (0, 0)
        self.enemy: Enemy|None = None


    def shoot(self, enemy: Enemy):
        self.enemy = enemy

        distance = self.calculate_distance(enemy)

        if distance <= 0: return

        diff_x = self.enemy.coordinates[0] - self.coordinates[0]
        diff_y = self.enemy.coordinates[1] - self.coordinates[1]
        self.objetive = (
            diff_x / distance,
            diff_y / distance,
        )

        shot_sound.play()


    def has_hit(self) -> bool:
        if self.enemy is None:
            return False


        pizza_rect = pygame.Rect(
            self.coordinates[0],
            self.coordinates[1],
            self.size[0],
            self.size[1],
        )
        enemy_rect = pygame.Rect(
            self.enemy.coordinates[0],
            self.enemy.coordinates[1],
            self.enemy.size[0],
            self.enemy.size[1],
        )


        return pizza_rect.colliderect(enemy_rect)


    def update(self):
        global enemy_father

        coordinates = (
            self.coordinates[0] + self.objetive[0] * self.speed,
            self.coordinates[1] + self.objetive[1] * self.speed,
        )

        if self.enemy is not None and self.has_hit():
            self.player.pizzas.remove(self)

            if self.enemy in enemy_father.children:
                hit_sound.play()
                enemy_father.children.remove(self.enemy)
                self.player.score.increase()


        self.locate(coordinates)


class EnemyFather:
    def __init__(self):
        self.children: list[Enemy] = []
        self.last_enemy_birth = pygame.time.get_ticks()


    def new_enemy(self):
        global scree_size

        rand_x = randint(0, scree_size[0] + 1)
        rand_y = randint(0, scree_size[1] + 1)

        positions = {
            'top': (rand_x, 0),
            'right': (scree_size[0], rand_y),
            'bottom': (rand_x, scree_size[1]),
            'left': (0, rand_y),
        }

        position = choice(list(positions.values()))

        new_enemy = Enemy(
            coordinates=position,
            image_path=complete_path('enemy.png'),
            size=(100, 100),
            speed=0.5,
        )

        self.children.append(new_enemy)
        self.last_enemy_birth = pygame.time.get_ticks()

        return self


    def is_time_exceded(self):
        return pygame.time.get_ticks() - self.last_enemy_birth >= enemies_interval


    def update(self):
        for enemy in self.children:
            enemy.run()
            enemy.update()


class Score:
    def __init__(self, player: Player):
        self.size = (100, 15)
        self.exchange_quantity = 3
        self.score = 0
        self.player = player
        self.margin = 25
        self.coordinates: tuple[int|float, int|float] = (
            scree_size[0] - (self.size[0] / 2) - self.margin,
            self.margin,
        )
        self.font = pygame.font.Font(None, 28)


    def show(self):
        rendered_object = self.font.render(f'SCORE: {str(self.score)}', True, text_color)
        screen.blit(rendered_object, locate(self.coordinates, self.size))


    def increase(self):
        self.score += 1

        if self.score >= self.exchange_quantity:
            self.exchange()

        self.show()


    def exchange(self):
        if self.score < self.exchange_quantity: return

        self.player.lives.add()
        self.score -= self.exchange_quantity


class Text:
    def __init__(
        self,
        text: str,
        font_size: int,
        size: tuple[int|float, int|float],
        coordinates: tuple[int|float, int|float]|None = None
    ):
        global scree_size

        self.text = text
        self.font_size = font_size
        self.size = size
        self.coordinates = coordinates if coordinates is not None else (
            scree_size[0] / 2,
            scree_size[1] / 2,
        )
        self.font = pygame.font.Font(None, self.font_size)


    def show(self):
        rendered_object = self.font.render(self.text, True, text_color)
        rect = rendered_object.get_rect(center=self.coordinates)
        screen.blit(rendered_object, rect)


print_title('Py game')


# Init pygame
pygame.mixer.pre_init(
    frequency=44100,
    size=-16,
    channels=2,
    buffer=128,
)
pygame.init()


# Fixtures
maximum_lives = 5
scree_size = (800, 600)
icon_path = complete_path('icon-pizza.png')
bg_path = complete_path('fondo.png')
icon = pygame.image.load(icon_path)
bg = pygame.image.load(bg_path)
bg = pygame.transform.scale(bg, scree_size)
enemies_interval = 5000
vulnerability_interval = 5000
game_over_title = Text('GAME OVER!!', 60, (275, 30))
text_color: tuple[int, int, int] = (255, 0, 0)


# Sound fixtures
pygame.mixer.music.load(complete_path('bg.mp3'))
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

hit_sound = pygame.mixer.Sound(complete_path('hit.wav'))
hit_sound.set_volume(0.8)
life_lost_sound = pygame.mixer.Sound(complete_path('life_lost.wav'))
life_lost_sound.set_volume(0.8)
shot_sound = pygame.mixer.Sound(complete_path('shot.wav'))
shot_sound.set_volume(0.8)


# Show screen
pygame.display.set_caption('Pizza Survivor')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(scree_size)


# Objects
deliver = Player(
    coordinates=(scree_size[0] / 2, scree_size[1] / 2),
    image_path=complete_path('pizza-deliver.png'),
    size=(100, 100),
    speed=1,
    lives=1
)


enemy_father: EnemyFather = EnemyFather()
enemy_father.new_enemy()


# Game loop
is_running = True
game_over = False
start_time = pygame.time.get_ticks()
end_time = None
while is_running:
    screen.blit(bg, (0, 0))
    events: list[EventType] = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            is_running = False

    if game_over:
        show_end()
    else:
        play(events)

    pygame.display.update()

pygame.quit()


print_title('Bye bye')






