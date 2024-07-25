def pigeonhole_sort(arreglo):
    minimo_valor = min(arreglo)  # Encuentra el valor mínimo en el arreglo
    maximo_valor = max(arreglo)  # Encuentra el valor máximo en el arreglo
    rango_valores = maximo_valor - minimo_valor + 1  # Calcula el rango de valores

    agujeros = [0] * rango_valores  # Crea una lista de agujeros de tamaño rango_valores, inicializada con ceros
    operaciones = 0  # Inicializa el contador de operaciones

    # Llenar los agujeros y realizar conteo de comparaciones
    for num in arreglo:  # Itera sobre cada elemento del arreglo
        agujeros[num - minimo_valor] += 1  # Incrementa el conteo del número actual en el agujero correspondiente
        operaciones += 1  # Incremento por las operaciones de comparación y de asignación

    # Reconstruir el arreglo en orden
    indice = 0  # Inicializa el índice para reconstruir el arreglo en orden
    for i in range(rango_valores):  # Itera sobre cada índice en la lista de agujeros
        while agujeros[i] > 0:  # Mientras haya elementos en este agujero
            arreglo[indice] = i + minimo_valor  # Asigna el valor al arreglo en la posición actual
            indice += 1  # Incrementa el índice para avanzar en el arreglo ordenado
            agujeros[i] -= 1  # Decrementa el conteo del valor actual en el agujero
            operaciones += 3  # Incremento por las operaciones de asignación, incremento de índice y decremento de agujeros[i]

    return arreglo, operaciones  # Devuelve el arreglo ordenado y el número total de operaciones realizadas
