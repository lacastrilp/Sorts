def counting_sort(arreglo):
    maximo_valor = max(arreglo)  # Encuentra el valor máximo en el arreglo
    cuenta = [0] * (maximo_valor + 1)  # Crea una lista de conteo de tamaño maximo_valor + 1, inicializada con ceros
    operaciones = 0  # Contador de operaciones

    for num in arreglo:  # Itera sobre cada elemento del arreglo
        cuenta[num] += 1  # Incrementa el conteo del número actual
        operaciones += 1  # Incrementa el contador de operaciones por la operación de incrementar cuenta[num]

    indice = 0  # Inicializa el índice para recorrer el arreglo ordenado
    for i in range(len(cuenta)):  # Itera sobre cada índice en la lista de conteo
        while cuenta[i] > 0:  # Mientras haya elementos con este valor en el arreglo
            arreglo[indice] = i  # Asigna el valor al arreglo en la posición actual
            indice += 1  # Incrementa el índice para avanzar en el arreglo ordenado
            cuenta[i] -= 1  # Decrementa el conteo del valor actual
            operaciones += 3  # Incrementa el contador de operaciones por las operaciones de asignación, incremento de índice y decremento de cuenta[i]

    return arreglo, operaciones  # Devuelve el arreglo ordenado y el número total de operaciones realizadas
