
# Ejercicio práctico — Análisis de palabras con Hadoop

## Objetivo

Utilizar el programa **WordCount de Hadoop** para analizar y comparar la frecuencia de palabras en distintos textos.

## Instrucciones

1. Crear tres archivos de texto dentro de la carpeta `ejemplo_mapreduce`:

   - `cuento.txt`
   - `noticia.txt`
   - `song.txt`

2. Añadir contenido diferente en cada archivo.

3. Ejecutar **WordCount** para cada archivo:

```bash
hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount <archivo>.txt <carpeta_salida>
```

Por ejemplo:

```bash
hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount cuento.txt output_cuento
```

4. Consultar los resultados:

```bash
cat <carpeta_salida>/part-r-00000
```

5. Comparar los resultados obtenidos y responder:

- ¿Cuál es la palabra que más veces aparece en cada texto?
- ¿Qué palabras se repiten en más de un texto?
- ¿En cuál de los textos se observa una mayor repetición de palabras?
