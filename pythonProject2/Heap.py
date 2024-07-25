def heapify(arreglo, n, i, operaciones):
    mayor = i  # Inicializa el índice del mayor elemento como i
    izquierda = 2 * i + 1  # Calcula el índice del hijo izquierdo
    derecha = 2 * i + 2  # Calcula el índice del hijo derecho

    if izquierda < n:  # Verifica si el hijo izquierdo está dentro de los límites del arreglo
        operaciones += 1  # Incremento por la comparación de índices
        if arreglo[izquierda] > arreglo[mayor]:
            mayor = izquierda  # Actualiza el índice del mayor elemento si el hijo izquierdo es mayor

    if derecha < n:  # Verifica si el hijo derecho está dentro de los límites del arreglo
        operaciones += 1  # Incremento por la comparación de índices
        if arreglo[derecha] > arreglo[mayor]:
            mayor = derecha  # Actualiza el índice del mayor elemento si el hijo derecho es mayor

    if mayor != i:  # Si el índice del mayor elemento no es igual a i, hay un nuevo mayor
        arreglo[i], arreglo[mayor] = arreglo[mayor], arreglo[i]  # Intercambia los elementos
        operaciones += 1  # Incremento por las operaciones de intercambio
        operaciones = heapify(arreglo, n, mayor, operaciones)  # Llamada recursiva para mantener la propiedad de max-heap
    return operaciones  # Devuelve el número total de operaciones realizadas


def heap_sort(arreglo):
    n = len(arreglo)  # Obtiene la longitud del arreglo
    operaciones = 0  # Inicializa el contador de operaciones

    # Construir un max heap.
    for i in range(n // 2 - 1, -1, -1):  # Itera desde el último nodo no hoja hasta la raíz
        operaciones = heapify(arreglo, n, i, operaciones)

    # Extraer elementos uno por uno del montículo.
    for i in range(n - 1, 0, -1):  # Itera desde el último elemento hasta el segundo elemento
        arreglo[i], arreglo[0] = arreglo[0], arreglo[i]  # Intercambia el primer elemento (el mayor) con el último elemento del heap
        operaciones += 1  # Incremento por las operaciones de intercambio
        operaciones = heapify(arreglo, i, 0, operaciones)  # Restaura la propiedad de max-heap
    return arreglo, operaciones  # Devuelve el arreglo ordenado y el número total de operaciones realizadas
