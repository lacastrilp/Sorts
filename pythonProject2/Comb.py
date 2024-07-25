def obtenerSiguienteBrecha(brecha):
    # Reducir la brecha por el factor de reducción
    brecha = (brecha * 10) // 13
    # Si la brecha es menor que 1, establecerla en 1
    if brecha < 1:
        return 1
    # Devolver la brecha calculada
    return brecha

# Función para ordenar arr[] usando el Ordenamiento por Peine
def comb_sort(arr):
    n = len(arr)
    # Inicializar la brecha
    brecha = n
    # Inicializar swapped como verdadero para asegurarse de que
    # el bucle se ejecute al menos una vez
    intercambio = True
    # Contador de operaciones
    operaciones = 0
    # Seguir ejecutando mientras la brecha sea mayor que 1 y la última
    # iteración haya causado un intercambio
    while brecha != 1 or intercambio:
        # Encontrar la próxima brecha
        brecha = obtenerSiguienteBrecha(brecha)
        # Inicializar intercambio como falso para que podamos
        # verificar si ocurrió un intercambio o no en la iteración actual
        intercambio = False
        # Comparar todos los elementos con la brecha actual
        for i in range(0, n - brecha):
            # Incrementar el contador de operaciones
            operaciones += 1
            # Si el elemento actual es mayor que el elemento en la brecha,
            # intercambiar los elementos
            if arr[i] > arr[i + brecha]:
                arr[i], arr[i + brecha] = arr[i + brecha], arr[i]
                # Establecer intercambio como verdadero, ya que se realizó un intercambio
                intercambio = True
    # Devolver la lista ordenada y el número total de operaciones realizadas
    return arr, operaciones
