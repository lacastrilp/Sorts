def counting_sort(arreglo, exp, contar_operaciones):
    n = len(arreglo)  # Obtiene la longitud del arreglo
    salida = [0] * n  # Inicializa un arreglo de salida del mismo tamaño que el arreglo original
    cuenta = [0] * 10  # Inicializa un arreglo de conteo para los dígitos del 0 al 9

    # Contar la frecuencia de cada dígito
    for i in range(n):  # Itera sobre cada elemento del arreglo
        indice = (arreglo[i] // exp) % 10  # Calcula el índice del dígito actual
        cuenta[indice] += 1  # Incrementa el conteo del dígito
        contar_operaciones[0] += 1  # Contador de operaciones

    # Actualizar cuenta para indicar la posición de cada dígito en la salida
    for i in range(1, 10):  # Itera desde el segundo dígito hasta el último
        cuenta[i] += cuenta[i - 1]  # Suma el conteo actual con el anterior
        contar_operaciones[0] += 1  # Contador de operaciones

    # Construir el arreglo de salida
    i = n - 1  # Inicializa el índice para recorrer el arreglo desde el final
    while i >= 0:  # Mientras haya elementos en el arreglo
        indice = (arreglo[i] // exp) % 10  # Calcula el índice del dígito actual
        salida[cuenta[indice] - 1] = arreglo[i]  # Coloca el elemento en la posición correcta de la salida
        cuenta[indice] -= 1  # Decrementa el conteo del dígito
        i -= 1  # Decrementa el índice para avanzar en el arreglo
        contar_operaciones[0] += 3  # Contador de operaciones (3 operaciones en el bucle)

    # Copiar el arreglo de salida al arreglo original
    for i in range(n):  # Itera sobre cada elemento del arreglo de salida
        arreglo[i] = salida[i]  # Copia el elemento de salida al arreglo original
        contar_operaciones[0] += 1  # Contador de operaciones

def radix_sort(arreglo):
    maximo_num = max(arreglo)  # Encuentra el número máximo en el arreglo
    contar_operaciones = [0]  # Inicializa el contador de operaciones

    # Aplica counting sort para cada dígito, comenzando desde el dígito menos significativo
    exp = 1  # Inicializa el exponente para el primer dígito
    while maximo_num // exp > 0:  # Mientras haya dígitos en el número más grande
        counting_sort(arreglo, exp, contar_operaciones)  # Aplica counting sort para el dígito actual
        exp *= 10  # Incrementa el exponente para pasar al siguiente dígito

    return arreglo, contar_operaciones[0]  # Retorna el arreglo ordenado y el número total de operaciones realizadas
