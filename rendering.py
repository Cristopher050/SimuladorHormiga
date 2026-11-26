
import pygame

from simulation import (
    WIDTH, HEIGHT, NEST, FOOD, OBSTACLES,
    OBSTACLE_RADIUS
)

BACKGROUND = (35, 45, 38)
WHITE = (245, 245, 245)
BLACK = (20, 20, 20)
GREEN = (40, 180, 80)
RED = (220, 65, 55)
BROWN = (130, 85, 45)
YELLOW = (255, 210, 50)


def draw_world(screen, state, mode, workers, fps):
    screen.fill(BACKGROUND)

    # Dibujar obstáculos
    for x, y in OBSTACLES:
        pygame.draw.circle(
            screen, BROWN,
            (int(x), int(y)),
            OBSTACLE_RADIUS
        )

    # Dibujar hormiguero
    pygame.draw.circle(
        screen, RED,
        (int(NEST[0]), int(NEST[1])), 32
    )

    # Dibujar comida
    pygame.draw.circle(
        screen, GREEN,
        (int(FOOD[0]), int(FOOD[1])), 22
    )

    # Dibujar hormigas
    for ant in state.ants:
        color = YELLOW if ant.carrying else WHITE

        pygame.draw.circle(
            screen,
            color,
            (int(ant.x), int(ant.y)),
            4
        )

    # Información en pantalla
    font = pygame.font.SysFont("Arial", 19)

    information = (
        f"Hormigas: {len(state.ants)}",
        f"Comida entregada: {state.delivered}",
        f"Modo: {mode}",
        f"Workers: {workers}",
        f"FPS: {fps:.1f}",
        "1: Secuencial | 2: Paralelo",
        "F1: 1000 | F2: 3000 | F3: 5000",
        "R: Reiniciar | ESC: Salir"
    )

    for index, line in enumerate(information):
        text = font.render(line, True, WHITE)
        screen.blit(text, (15, 12 + index * 24))

    pygame.display.flip()
