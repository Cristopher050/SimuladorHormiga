# Simulador de Colonia de Hormigas

## Descripción

Este proyecto consiste en un simulador 2D de una colonia de hormigas desarrollado en Python utilizando Pygame.

El simulador representa hormigas que se desplazan entre un nido y una fuente de alimento, evitando obstáculos. También permite comparar la ejecución secuencial con la ejecución paralela mediante múltiples procesos.

## Objetivos

- Simular el movimiento de una colonia de hormigas.
- Aplicar principios de programación funcional.
- Utilizar estructuras de datos inmutables.
- Implementar procesamiento paralelo con múltiples procesos.
- Comparar el rendimiento secuencial y paralelo.

## Tecnologías utilizadas

- Python 3.13
- Pygame 2.6.1
- Dataclasses
- Concurrent Futures
- Multiprocessing

## Estructura del proyecto

text
SimuladorHormigas/
│
├── models.py
├── simulation.py
├── parallel.py
├── rendering.py
├── benchmark.py
├── main.py
├── verificar_paralelo.py
├── verificar_inmutabilidad.py
├── requirements.txt
└── README.md


## Instalación

1. Instalar Python.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Crear y activar un entorno virtual.
4. Instalar las dependencias:

bash
pip install -r requirements.txt


## Ejecución

Para iniciar el simulador:

bash
python main.py


## Controles

| Tecla | Función |
|---|---|
| 1 | Modo secuencial |
| 2 | Modo paralelo |
| F1 | 1000 hormigas |
| F2 | 3000 hormigas |
| F3 | 5000 hormigas |
| F4 | 8000 hormigas |
| R | Reiniciar puntuación |
| ESC | Salir |

## Programación funcional

El proyecto utiliza:

- @dataclass(frozen=True) para crear estructuras inmutables.
- Funciones que reciben un estado y retornan uno nuevo.
- Comprensiones de tuplas.
- Transformaciones declarativas.
- Separación entre lógica de simulación y efectos externos.

## Procesamiento paralelo

Se utiliza ProcessPoolExecutor para distribuir el procesamiento de las hormigas entre varios procesos.

La estrategia de distribución divide las entidades en grupos o bloques (chunks). Cada proceso calcula el movimiento de su grupo y posteriormente los resultados se consolidan en un nuevo estado.

## Pruebas

El proyecto incluye:

- Verificación de equivalencia entre actualización secuencial y paralela.
- Verificación de inmutabilidad.
- Benchmark para comparar tiempos de ejecución con 1000, 3000, 5000 y 8000 hormigas.
