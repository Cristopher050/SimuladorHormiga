
from concurrent.futures import ProcessPoolExecutor

from models import Ant, GameState
from simulation import update
from parallel import update_parallel, WORKERS


def main():
    hormigas = tuple(
        Ant(i, 500 + (i % 20), 350 + (i % 15))
        for i in range(1000)
    )

    estado = GameState(ants=hormigas)

    # Actualización secuencial
    resultado_secuencial = update(
        estado, (), 1 / 60
    )

    # Actualización con procesos reales
    with ProcessPoolExecutor(max_workers=WORKERS) as executor:
        resultado_paralelo = update_parallel(
            estado, (), 1 / 60, executor
        )

    print("Hormigas:", len(hormigas))
    print("Workers:", WORKERS)
    print(
        "¿Los resultados son iguales?:",
        resultado_secuencial == resultado_paralelo
    )
    print("Estado original:", estado.frame)
    print("Estado secuencial:", resultado_secuencial.frame)
    print("Estado paralelo:", resultado_paralelo.frame)


if __name__ == "__main__":
    main()
