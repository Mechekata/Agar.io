#!/usr/bin/env python3
import pygame
from pygame.math import Vector2
from cont import *
from random import randint

pygame.init()

blue = (125, 249, 255)
green = (62, 218, 148)
red = (255, 0, 0)
bleck = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 228, 107)

camera = Vector2(0, 0)

class Velocity(Vector2):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.last_tick = 0

def paint_card(self, shift_x, shift_y):
        self.paint()
        window.blit(self.image, (self.rect.x +shift_x, self.rect.y + shift_y))

class Circle:
    def __init__(self, display, color, radius, x, y):
        self.display = display
        self.color = color
        self.radius = radius
        self.position = Vector2(x, y)
        self.velocity = Velocity(0, 0);
        self.speed = 1.2
        self.currentTarget = None
        self.changeSpeed()

    def changeSpeed(self):
        self.speed = .2 * (10 / self.radius)

    def draw(self):
        pygame.draw.circle(self.display, self.color, (int(self.position[0] - camera.x), int(self.position[1] - camera.y)), self.radius)

    def move(self):
        if pygame.time.get_ticks() - self.velocity.last_tick > 1:
            self.velocity.last_tick = pygame.time.get_ticks()


            if self.currentTarget:
                self.turn_to(self.currentTarget)



            self.position += self.velocity

    def turn_to(self, vec):
        newVec = vec - self.position
        newVec.scale_to_length(self.speed)
        self.velocity.x = newVec.x
        self.velocity.y = newVec.y


class Player(Circle):
    def __init__(self, display, color, radius, x, y):
        super().__init__(display, color, radius, x, y)

    def move(self):
        super().move()
        x, y = pygame.mouse.get_pos()
        self.currentTarget = Vector2(camera.x + x, camera.y + y)


class Enemy(Circle):
    def __init__(self, display, radius, objects):
        self.objects = objects
        super().__init__(display, ENEMY_COLOR, radius, randint(0, SIZE[0]), randint(0, SIZE[1]))

    def move(self):
        # scanning
        for_scan = []
        for obj in self.objects:
            if obj != self:
                for_scan.append(obj)


        self.currentTarget = for_scan[0].position
        for obj in for_scan:
            if self.position.distance_to(obj.position) < self.position.distance_to(self.currentTarget):
                self.currentTarget = obj.position
        super().move()

class Game:
    def __init__(self, display):
        self.display = display
        self.player = Player(display, CIRCLE_COLOR, 10, 100,100)
        self.objects = [self.player]

        global camera
        camera = Vector2(self.player.position.x, self.player.position.y)

        for i in range(5):
            enemy = Enemy(self.display, 10, self.objects)
            self.objects.append(enemy)

        for i in range(10):
            food = Circle(display, FOOD_COLOR, 5, randint(0, SIZE[0]), randint(0, SIZE[1]))
            self.objects.append(food)
    def draw(self):
        for circle in self.objects:
            if (circle.position.x and circle.position.x <= camera.x + SIZE[0] and circle.position.y >= camera.y and circle.position.y <= camera.y + SIZE[1]):
                circle.draw()

    def update(self):
        for circle in self.objects:
            circle.move()
        camera.x = self.player.position.x - SIZE[0] // 2
        camera.y = self.player.position.y - SIZE[1] // 2

    def collisionDetection(self):
        to_remove = []
        for i, circle in enumerate(self.objects):
            for j, nextCircle in enumerate(self.objects[i + 1:]):
                if circle.position.distance_to(nextCircle.position) <= (circle.radius + nextCircle.radius):
                    if circle.radius > nextCircle.radius:
                        circle.radius += int(nextCircle.radius / 2)
                        circle.changeSpeed()
                        self.add_food()
                        to_remove.append(nextCircle)
                        break

                    elif nextCircle.radius > circle.radius:
                        nextCircle.radius += int(circle.radius / 2)
                        nextCircle.changeSpeed
                        to_remove.append(circle)
                        break

        for circle in to_remove:
            self.objects.remove(circle)


    def add_food(self):
        food = Circle(self.display, FOOD_COLOR, 5, randint(0, SIZE[0]), randint(0, SIZE[1]))
        self.objects.append(food)
