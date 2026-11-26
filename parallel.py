
import os
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat

from models import GameState
from simulation import move_ant

# Núcleos detectados en el equipo
CPU_CORES = os.cpu_count() or 1

# Máximo de procesos que utilizaremos
WORKERS = min(CPU_CORES, 8)


def split_entities(ants, workers):
    """Divide las hormigas en grupos para los procesos."""

    total = len(ants)

    if total == 0:
        return ()

    workers = max(1, min(workers, total))
    chunk_size = (total + workers - 1) // workers

    return tuple(
        ants[i:i + chunk_size]
        for i in range(0, total, chunk_size)
    )


def process_chunk(chunk, dt):
    """Actualiza un grupo de hormigas en un proceso."""

    results = tuple(
        move_ant(ant, dt)
        for ant in chunk
    )

    new_ants = tuple(
        result[0]
        for result in results
    )

    delivered = sum(
        result[1]
        for result in results
    )

    return new_ants, delivered


def update_parallel(state, events, dt, executor):
    """Distribuye el cálculo y consolida el nuevo estado."""

    chunks = split_entities(state.ants, WORKERS)

    results = tuple(
        executor.map(
            process_chunk,
            chunks,
            repeat(dt)
        )
    )

    new_ants = tuple(
        ant
        for group, delivered in results
        for ant in group
    )

    new_delivered = sum(
        delivered
        for group, delivered in results
    )

    score = state.delivered + new_delivered

    if "reset_score" in events:
        score = 0

    return GameState(
        ants=new_ants,
        delivered=score,
        frame=state.frame + 1
    )
