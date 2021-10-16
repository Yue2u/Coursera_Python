#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, x_, y_):
        self.x = x_
        self.y = y_

    def __len__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __mul__(self, number):
        return Vec2d(self.x * number, self.y * number)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def int_pair(self):
        return self.x, self.y


class Polyline:
    def __init__(self, display):
        self.points = []
        self.speeds = []
        self.game_display = display

    def speed_up(self):
        for p in self.speeds:
            p.x *= 1.1
            p.y *= 1.1

    def speed_break(self):
        for p in self.speeds:
            p.x *= 0.9
            p.y *= 0.9

    def clear(self):
        self.points = []
        self.speeds = []

    def append(self, point):
        self.points.append(Vec2d(point[0], point[1]))
        self.speeds.append(Vec2d(random.random() * 2, random.random() * 2))

    def delete_last(self):
        del self.points[-1]
        del self.speeds[-1]

    def set_points(self):
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p] = Vec2d(- self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)

    def draw_points(self, style="points", width=3, color=(255, 255, 255), spec_points=None):
        """функция отрисовки точек на экране"""
        if spec_points is None:
            spec_points = self.points
        if style == "line":
            for p_n in range(-1, len(spec_points) - 1):
                pygame.draw.line(self.game_display, color,
                                 (int(spec_points[p_n].x), int(spec_points[p_n].y)),
                                 (int(spec_points[p_n + 1].x), int(spec_points[p_n + 1].y)), width)

        elif style == "points":
            for p in spec_points:
                pygame.draw.circle(self.game_display, color,
                                   (int(p.x), int(p.y)), width)


class Knot(Polyline):
    def __init__(self, spec_steps, display):
        super().__init__(display)
        self.steps = spec_steps
        self.knotted = []

    def delete_last(self):
        super().delete_last()
        self.knotted = self.get_knot()

    def clear(self):
        super().clear()
        self.knotted = []

    def decrease_steps(self):
        self.steps -= 1 if self.steps > 1 else 0

    def increase_steps(self):
        self.steps += 1 if self.steps > 0 else 0

    def get_point(self, spec_points, alpha, deg=None):
        if deg is None:
            deg = len(spec_points) - 1
        if deg == 0:
            return spec_points[0]
        return (spec_points[deg] * alpha) + (self.get_point(spec_points, alpha, deg - 1) * (1 - alpha))

    def get_points(self, base_points):
        alpha = 1 / self.steps
        res = []
        for i in range(self.steps):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = [(self.points[i] + self.points[i + 1]) * 0.5, self.points[i + 1],
                   (self.points[i + 1] + self.points[i + 2]) * 0.5]
            res.extend(self.get_points(ptn))
        return res

    def append(self, pos):
        super().append(pos)
        self.knotted = self.get_knot()

    def set_points(self):
        super().set_points()
        self.knotted = self.get_knot()

    def draw_points(self, style="points", width=3, color=(255, 255, 255), spec_points=None):
        super().draw_points(style, width, color, self.knotted)


class ScreenSaver:
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode(SCREEN_DIM)
        pygame.display.set_caption("MyScreenSaver")

        self.steps = 35
        self.working = True
        self.show_help = False
        self.pause = True
        self.hue = 0
        self.color = pygame.Color(0)
        self.polyline = Polyline(self.game_display)
        self.knot = Knot(self.steps, self.game_display)

    def draw_help(self):
        """функция отрисовки экрана справки программы"""
        self.game_display.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = [["F1", "Show Help"], ["R", "Restart"], ["P", "Pause/Play"], ["Num+", "More points"],
                ["Num-", "Less points"], ["U", "Increase speed"], ["D", "Decrease speed"],
                ["Del", "Delete last added point"], ["", ""], [str(self.steps), "Current points"]]
        pygame.draw.lines(self.game_display, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            self.game_display.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            self.game_display.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))

    def run_saver(self):
        while self.working:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.working = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.working = False
                    if event.key == pygame.K_r:
                        self.polyline.clear()
                        self.knot.clear()
                    if event.key == pygame.K_p:
                        self.pause = not self.pause
                    if event.key == pygame.K_KP_PLUS:
                        self.steps += 1
                        self.knot.increase_steps()
                    if event.key == pygame.K_F1:
                        self.show_help = not self.show_help
                    if event.key == pygame.K_KP_MINUS:
                        self.steps -= 1 if self.steps > 1 else 0
                        self.knot.decrease_steps()
                    if event.key == pygame.K_u:
                        self.polyline.speed_up()
                        self.knot.speed_up()
                    if event.key == pygame.K_d:
                        self.polyline.speed_break()
                        self.knot.speed_break()
                    if event.key == pygame.K_DELETE:
                        self.polyline.delete_last()
                        self.knot.delete_last()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.polyline.append(event.pos)
                    self.knot.append(event.pos)

            self.game_display.fill((0, 0, 0))
            self.hue = (self.hue + 1) % 360
            self.color.hsla = (self.hue, 100, 50, 100)
            self.polyline.draw_points()
            self.knot.draw_points("line", 3, self.color)
            if not self.pause:
                self.polyline.set_points()
                self.knot.set_points()
            if self.show_help:
                self.draw_help()

            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()
        exit(0)


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    s = ScreenSaver()
    s.run_saver()
