1. **Descargar el código:** Copia el código proporcionado
2. **Instalar librerias:** Deberás instalar las librerias necesarias si no se tienen previamente instaladas, las puedes instalar desde powerShell así:
```
# pip install psutil
```

3. **Ejecutar el código:** Puedes ejecutar el código desde la línea de comandos o esde tu entorno de desarrollo favorito. Para ejecutarlo desde la línea de comandos, navega hasta la ubicación del archivo en tu terminal y ejecuta:
```
# python sorting_benchmark.py
```


2. **Espera a que finalice la ejecución:** El código ejecutará pruebas de rendimiento para varios algoritmos de ordenación en diferentes tamaños de arreglos. Esto puede llevar un tiempo dependiendo del tamaño de los arreglos y de la potencia de tu computadora.

3. **Revisa los resultados:** Una vez que el código haya terminado de ejecutarse, revisa la salida en la terminal. Verás información sobre el tiempo de ejecución, la memoria utilizada y el número de operaciones para cada algoritmo de ordenación en diferentes tamaños de arreglos.

4. **Archivos de resultados:** El código también exportará los resultados a un archivo Excel llamado sorting_results.xlsx, donde podrás encontrar datos detallados sobre el tiempo de ejecución, la memoria utilizada y el número de operaciones para cada algoritmo de ordenación en diferentes tamaños de arreglos.


**Funcionamiento:**

1. **Medición del rendimiento:** El código utiliza diferentes algoritmos de ordenación implementados en archivos separados. Mide el tiempo de ejecución, la memoria utilizada y el número de operaciones para cada algoritmo en tamaños de arreglos crecientes.
2. **Gráficos de resultados:** Después de ejecutar las pruebas de rendimiento, el código genera gráficos que muestran cómo varía el tiempo de ejecución, la memoria utilizada y el número de operaciones en función del tamaño del arreglo para cada algoritmo de ordenación.
3. **Exportación de resultados:** Además de los gráficos, el código exporta los resultados a un archivo Excel para un análisis más detallado o para su posterior procesamiento.