# Estas líneas importan varios módulos necesarios para el funcionamiento del script,
# como generación de números aleatorios (random), medición del tiempo (time),
# monitoreo del uso de recursos del sistema (psutil), manipulación de datos (pandas),
# manipulación de gráficos (matplotlib.pyplot) y funciones de decoradores (wraps).
# Además, se importan los algoritmos de ordenación definidos en archivos separados.

import random
import time
import psutil
import pandas as pd
from functools import wraps
import matplotlib.pyplot as plt

import Comb
import Couting
import Heap
import Merge1
import Pigeonhole
import Radix
import Randomized_quick
import Shell

# Esta función plot_results se utiliza para trazar gráficos a partir de un DataFrame (df).
# Toma como entrada la columna para el eje x (x_column), las columnas para el eje y (y_columns),
# las etiquetas para las líneas (y_labels) y un título para el gráfico. Luego, traza un gráfico utilizando matplotlib.
def plot_results(df, x_column, y_columns, y_labels, title):
    for y_column, y_label in zip(y_columns, y_labels):
        plt.plot(df[x_column], df[y_column], marker='o', label=y_label)
    plt.title(title)
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Valor")
    plt.xscale("log")
    plt.grid(True)
    plt.legend()
    plt.show()

# Este decorador measure_sorting_no_range se utiliza para medir el tiempo de ejecución,
# la memoria utilizada y el número de operaciones de un algoritmo de ordenación que no requiere un rango especificado.
# Toma una función de ordenación como argumento (func) y devuelve otra función (wrapper) que realiza la medición.
def measure_sorting_no_range(func):
    @wraps(func)
    def wrapper(arr):
        print(f"\n\n***{func.__name__.replace('_', ' ').title()}*** {len(arr):,} elementos")
        start_time = time.time()
        before_memory = psutil.Process().memory_info().rss
        sorted_arr, operations = func(arr)
        after_memory = psutil.Process().memory_info().rss
        end_time = time.time()
        print("Memoria utilizada:", abs(after_memory - before_memory) / 1024, "KB")
        print("Tiempo de ejecucion:", abs(end_time - start_time))
        print("Numero de operaciones:", operations)
        return abs(end_time - start_time), abs(after_memory - before_memory), operations

    return wrapper

# Este decorador measure_sorting_with_range es similar al anterior,
# pero se utiliza para medir el tiempo de ejecución, la memoria utilizada y
# el número de operaciones de un algoritmo de ordenación que requiere entradas diferentes.
def measure_sorting_with_range(func):
    @wraps(func)
    def wrapper(arr, bajo, alto):
        print(f"\n\n***{func.__name__.replace('_', ' ').title()}*** {len(arr):,} elementos")
        start_time = time.time()
        before_memory = psutil.Process().memory_info().rss
        sorted_arr, operations = func(arr, bajo, alto)
        after_memory = psutil.Process().memory_info().rss
        end_time = time.time()
        print("Memoria utilizada:", abs(after_memory - before_memory) / 1024, "KB")
        print("Tiempo de ejecucion:", abs(end_time - start_time))
        print("Numero de operaciones:", operations)
        return abs(end_time - start_time), abs(after_memory - before_memory), operations

    return wrapper

# Esta clase SortingBenchmark contiene una lista de tuplas llamada sorting_methods,
# donde cada tupla contiene el nombre de un algoritmo de ordenación y
# la función correspondiente que implementa dicho algoritmo.
class SortingBenchmark:
    sorting_methods = [
        ("counting_sort", Couting.counting_sort),
        ("pigeonhole_sort", Pigeonhole.pigeonhole_sort),
        ("merge_sort", Merge1.merge_sort),
        ("radix_sort", Radix.radix_sort),
        ("randomized_quick_sort", Randomized_quick.randomized_quick_sort),
        ("heap_sort", Heap.heap_sort),
        ("comb_sort", Comb.comb_sort),
        ("shell_sort", Shell.shell_sort)
    ]

    # Estos son métodos estáticos dentro de la clase SortingBenchmark que se utilizan para crear arreglos ordenados,
    # arreglos invertidos y arreglos aleatorios de diferentes tamaños.
    @staticmethod
    def create_sorted_array(size):
        return list(range(size))

    @staticmethod
    def create_reverse_array(length):
        return list(range(length, 0, -1))

    @staticmethod
    def create_random_array(length):
        return [random.randint(0, 100000000) for _ in range(length)]

# Este método run_benchmarks de la clase SortingBenchmark ejecuta las pruebas de rendimiento
# para todos los algoritmos de ordenación en los tamaños de arreglos dados.
# Para cada algoritmo, mide el tiempo de ejecución, la memoria utilizada y }
# el número de operaciones en diferentes tamaños de arreglos.
# Luego, devuelve un DataFrame de pandas con los resultados.
    @staticmethod
    def run_benchmarks(sizes):
        results = {"Tamano del arreglo": sizes}

        for method_name, method in SortingBenchmark.sorting_methods:
            method_times = []
            method_memories = []
            method_operations = []

            for size in sizes:
                arr = SortingBenchmark.create_sorted_array(size)
                bajo, alto = 0, len(arr) - 1  # Establece bajo y alto para los métodos que los requieran
                if method_name in ["counting_sort", "pigeonhole_sort", "merge_sort", "radix_sort", "shell_sort",
                                   "comb_sort", "heap_sort"]:
                    execution_time, memory_use, operations = measure_sorting_no_range(method)(arr)
                else:
                    execution_time, memory_use, operations = measure_sorting_with_range(method)(arr, bajo, alto)
                method_times.append(execution_time)
                method_memories.append(memory_use)
                method_operations.append(operations)

            results[method_name + "_time"] = method_times
            results[method_name + "_memory"] = method_memories
            results[method_name + "_operations"] = method_operations

        return pd.DataFrame(results)

# La función main es el punto de entrada del script.
# Define los tamaños de los arreglos a probar, ejecuta las pruebas de
# rendimiento para todos los algoritmos de ordenación en esos tamaños de arreglos y
# luego traza y exporta los resultados a un archivo Excel. Se trazan tres tipos de gráficos:
# tiempo de ejecución, memoria utilizada y número de operaciones en función del tamaño del arreglo.
def main():
    sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]

    df_results = SortingBenchmark.run_benchmarks(sizes)

    # Plot time, memory, and operations for all sorting algorithms
    plot_results(df_results, "Tamano del arreglo",
                 [method_name + "_time" for method_name, _ in SortingBenchmark.sorting_methods],
                 [method_name.replace("_", " ").title() for method_name, _ in SortingBenchmark.sorting_methods],
                 "Tiempo de ejecución en función del tamaño del arreglo")

    plot_results(df_results, "Tamano del arreglo",
                 [method_name + "_memory" for method_name, _ in SortingBenchmark.sorting_methods],
                 [method_name.replace("_", " ").title() for method_name, _ in SortingBenchmark.sorting_methods],
                 "Memoria utilizada en función del tamaño del arreglo")

    plot_results(df_results, "Tamano del arreglo",
                 [method_name + "_operations" for method_name, _ in SortingBenchmark.sorting_methods],
                 [method_name.replace("_", " ").title() for method_name, _ in SortingBenchmark.sorting_methods],
                 "Operaciones en función del tamaño del arreglo")

    # Separar los datos en diferentes DataFrames para tiempo, memoria y operaciones
    df_time = df_results[[method_name + "_time" for method_name, _ in SortingBenchmark.sorting_methods] + ["Tamano del arreglo"]]
    df_memory = df_results[[method_name + "_memory" for method_name, _ in SortingBenchmark.sorting_methods] + ["Tamano del arreglo"]]
    df_operations = df_results[[method_name + "_operations" for method_name, _ in SortingBenchmark.sorting_methods] + ["Tamano del arreglo"]]

    # Plotear y exportar cada DataFrame a una hoja diferente en el archivo Excel
    with pd.ExcelWriter("sorting_results.xlsx") as writer:
        df_time.to_excel(writer, sheet_name="Tiempo", index=False)
        df_memory.to_excel(writer, sheet_name="Memoria", index=False)
        df_operations.to_excel(writer, sheet_name="Operaciones", index=False)


if __name__ == "__main__":
    main()
