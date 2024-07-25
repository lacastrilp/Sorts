def merge_sort(arreglo):
    operaciones = 0  # Contador de operaciones

    def merge(izquierda, derecha):
        nonlocal operaciones  # Indica que operaciones se refiere a la variable de la función externa
        arreglo_fusionado = []  # Lista para almacenar el arreglo fusionado
        i = j = 0  # Inicialización de los índices para recorrer los arreglos izquierda y derecha

        # Itera mientras haya elementos tanto en el arreglo izquierda como en el arreglo derecha
        while i < len(izquierda) and j < len(derecha):
            operaciones += 1  # Incrementa el contador de operaciones
            # Compara los elementos en las posiciones i y j de izquierda y derecha respectivamente
            if izquierda[i] < derecha[j]:
                arreglo_fusionado.append(izquierda[i])  # Agrega el elemento de izquierda a arreglo_fusionado
                i += 1  # Incrementa el índice de izquierda
            else:
                arreglo_fusionado.append(derecha[j])  # Agrega el elemento de derecha a arreglo_fusionado
                j += 1  # Incrementa el índice de derecha

        # Agrega los elementos restantes de izquierda, si es que hay
        while i < len(izquierda):
            arreglo_fusionado.append(izquierda[i])
            i += 1
            operaciones += 1

        # Agrega los elementos restantes de derecha, si es que hay
        while j < len(derecha):
            arreglo_fusionado.append(derecha[j])
            j += 1
            operaciones += 1

        return arreglo_fusionado  # Devuelve el arreglo fusionado

    def mergeSort(arr):
        if len(arr) > 1:
            mitad = len(arr) // 2  # Calcula la mitad del arreglo
            mitad_izquierda = arr[:mitad]  # Sub-arreglo de la izquierda
            mitad_derecha = arr[mitad:]  # Sub-arreglo de la derecha

            mitad_izquierda = mergeSort(mitad_izquierda)  # Llama recursivamente mergeSort con la mitad izquierda
            mitad_derecha = mergeSort(mitad_derecha)  # Llama recursivamente mergeSort con la mitad derecha

            arr = merge(mitad_izquierda, mitad_derecha)  # Fusiona los sub-arreglos ordenados

        return arr  # Devuelve el arreglo ordenado

    return mergeSort(arreglo), operaciones  # Llama a mergeSort con el arreglo dado y devuelve el arreglo ordenado y el número de operaciones
