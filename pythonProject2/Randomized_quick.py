import random  # Importa el módulo random para generar números aleatorios

def swap(arreglo, i, j):
    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]  # Intercambia los elementos en las posiciones i y j del arreglo

def randomized_quick_sort(arreglo, bajo, alto):
    operaciones = 0  # Inicializa el contador de operaciones

    def particion(arreglo, bajo, alto):
        nonlocal operaciones  # Permite modificar la variable operaciones definida en el ámbito exterior a esta función interna
        indice_pivote = random.randint(bajo, alto)  # Elige un índice aleatorio como pivote
        pivote = arreglo[indice_pivote]  # Obtiene el valor del pivote
        swap(arreglo, indice_pivote, alto)  # Coloca el pivote al final del arreglo
        i = bajo  # Inicializa un índice para recorrer el arreglo
        for j in range(bajo, alto):  # Itera sobre el rango desde bajo hasta alto - 1
            operaciones += 1  # Incremento por cada iteración del bucle for
            if arreglo[j] < pivote:  # Compara el elemento actual con el pivote
                swap(arreglo, i, j)  # Intercambia el elemento actual con el elemento en la posición i
                i += 1  # Incrementa el índice i
        swap(arreglo, i, alto)  # Coloca el pivote en la posición correcta
        operaciones += 1  # Incremento por la operación de intercambio del pivote final
        return i  # Retorna la posición del pivote después de la partición

    if bajo < alto:  # Verifica si hay más de un elemento en el arreglo
        pivote = particion(arreglo, bajo, alto)  # Obtiene la posición del pivote después de la partición
        randomized_quick_sort(arreglo, bajo, pivote - 1)  # Aplica el algoritmo de ordenación para la sublista izquierda
        randomized_quick_sort(arreglo, pivote + 1, alto)  # Aplica el algoritmo de ordenación para la sublista derecha

    return arreglo, operaciones  # Retorna el arreglo ordenado y el número total de operaciones realizadas
