def shell_sort(arreglo):
    n = len(arreglo)  # Obtiene la longitud del arreglo
    brecha = n // 2  # Inicializa la brecha como la mitad de la longitud del arreglo
    operaciones = 0  # Contador de operaciones

    while brecha > 0:  # Mientras la brecha sea mayor que cero
        for i in range(brecha, n):  # Itera sobre el arreglo con la brecha actual
            temp = arreglo[i]  # Guarda el valor actual en una variable temporal
            j = i  # Inicializa un índice para recorrer el arreglo desde la posición actual
            while j >= brecha and arreglo[j - brecha] > temp:  # Mientras haya elementos anteriores y el elemento actual sea menor que el anterior
                arreglo[j] = arreglo[j - brecha]  # Desplaza el elemento anterior hacia adelante
                j -= brecha  # Decrementa el índice con la brecha
                operaciones += 2  # Incremento por cada iteración del bucle while y el decremento de j
            arreglo[j] = temp  # Coloca el valor guardado en la posición correcta
            operaciones += 1  # Incremento por la asignación de temp a arreglo[j]
        brecha //= 2  # Reduce la brecha a la mitad en cada iteración
        operaciones += 1  # Incremento por la división de brecha

    return arreglo, operaciones  # Retorna el arreglo ordenado y el número total de operaciones realizadas
