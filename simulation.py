
from math import hypot
from models import Ant, GameState

WIDTH = 1000
HEIGHT = 700

NEST = (500.0, 350.0)
FOOD = (850.0, 100.0)

SPEED = 90.0
ANT_RADIUS = 5.0
OBSTACLE_RADIUS = 20.0

OBSTACLES = (
    (200.0, 180.0),
    (350.0, 250.0),
    (650.0, 200.0),
    (750.0, 450.0),
    (300.0, 500.0),
    (600.0, 550.0),
    (150.0, 400.0),
    (850.0, 300.0),
)


def move_ant(ant, dt):
    target = NEST if ant.carrying else FOOD

    dx = target[0] - ant.x
    dy = target[1] - ant.y
    distance = hypot(dx, dy)

    if distance > 0:
        vx = dx / distance
        vy = dy / distance
    else:
        vx = 0.0
        vy = 0.0

    forces = tuple(
        (
            (ant.x - ox) / max(hypot(ant.x - ox, ant.y - oy), 1.0),
            (ant.y - oy) / max(hypot(ant.x - ox, ant.y - oy), 1.0)
        )
        for ox, oy in OBSTACLES
        if hypot(ant.x - ox, ant.y - oy) < 55
    )

    avoid_x = sum(force[0] for force in forces) * 35
    avoid_y = sum(force[1] for force in forces) * 35

    new_x = ant.x + (vx * SPEED + avoid_x) * dt
    new_y = ant.y + (vy * SPEED + avoid_y) * dt

    new_x = max(5, min(WIDTH - 5, new_x))
    new_y = max(5, min(HEIGHT - 5, new_y))

    carrying = ant.carrying
    delivered = 0

    if not carrying and hypot(
        new_x - FOOD[0], new_y - FOOD[1]
    ) < ANT_RADIUS + 22:
        carrying = True

    elif carrying and hypot(
        new_x - NEST[0], new_y - NEST[1]
    ) < ANT_RADIUS + 32:
        carrying = False
        delivered = 1

    new_ant = Ant(
        id=ant.id,
        x=new_x,
        y=new_y,
        carrying=carrying
    )

    return new_ant, delivered


def update(state, events, dt):
    results = tuple(
        move_ant(ant, dt)
        for ant in state.ants
    )

    new_ants = tuple(
        result[0]
        for result in results
    )

    new_delivered = sum(
        result[1]
        for result in results
    )

    score = state.delivered + new_delivered

    if "reset_score" in events:
        score = 0

    return GameState(
        ants=new_ants,
        delivered=score,
        frame=state.frame + 1
    )
