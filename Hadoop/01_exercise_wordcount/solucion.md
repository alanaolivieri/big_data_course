# Práctico Hadoop — WordCount

## Objetivo

Aplicar el programa **WordCount de Hadoop** para comparar la frecuencia de palabras en distintos textos y reforzar la comprensión del funcionamiento básico de **MapReduce**.

---

## 1. Preparar el entorno de trabajo

En el ejemplo anterior ya creamos la carpeta:

```bash
ejemplo_mapreduce
```

Por tanto, no es necesario volver a crearla ni eliminar su contenido.

Accede directamente a ella:

```bash
cd ~/ejemplo_mapreduce
```

Comprueba el contenido de la carpeta:

```bash
ls -l
```

Deberías encontrar, entre otros archivos, el `.jar` utilizado anteriormente:

```text
hadoop-mapreduce-examples-3.3.6.jar
```

### Si la carpeta no existe

Solo en ese caso, créala:

```bash
mkdir ~/ejemplo_mapreduce
cd ~/ejemplo_mapreduce
```

---

## 2. Crear los archivos de texto

Crear tres nuevos archivos dentro de `ejemplo_mapreduce`:

```bash
touch cuento.txt noticia.txt song.txt
```

Editar cada archivo con `nano` y añadir un texto breve que contenga algunas palabras repetidas.

### Cuento

```bash
nano cuento.txt
```

Añadir el texto y guardar.

### Noticia

```bash
nano noticia.txt
```

Añadir el texto y guardar.

### Canción

```bash
nano song.txt
```

Añadir el texto y guardar.

En `nano`:

- `Ctrl + O` → guardar.
- `Enter` → confirmar.
- `Ctrl + X` → salir.

---

## 3. Ejecutar WordCount

Vamos a ejecutar WordCount de forma independiente para cada archivo.

Cada ejecución debe utilizar una **carpeta de salida diferente**.

### Analizar `cuento.txt`

```bash
hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount cuento.txt output_cuento
```

### Analizar `noticia.txt`

```bash
hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount noticia.txt output_noticia
```

### Analizar `song.txt`

```bash
hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount song.txt output_song
```

### Importante: Hadoop no sobrescribe las carpetas de salida

Si vuelves a ejecutar alguno de los comandos y aparece un error indicando que la carpeta de salida ya existe, elimina **únicamente esa salida**.

Por ejemplo:

```bash
rm -rf output_cuento
```

Y vuelve a ejecutar:

```bash
hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount cuento.txt output_cuento
```

Si quieres repetir los tres análisis desde cero:

```bash
rm -rf output_cuento output_noticia output_song
```

Después, ejecutar nuevamente los tres comandos WordCount.

> No es necesario eliminar la carpeta `ejemplo_mapreduce`.

---

## 4. Si falta el archivo JAR

Si aparece un error similar a:

```text
JAR does not exist or is not a normal file
```

comprueba primero el contenido de la carpeta:

```bash
ls -l
```

Si el archivo:

```text
hadoop-mapreduce-examples-3.3.6.jar
```

no aparece, descárgalo otra vez:

```bash
wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-mapreduce-examples/3.3.6/hadoop-mapreduce-examples-3.3.6.jar
```

Comprueba que se haya descargado correctamente:

```bash
ls -l hadoop-mapreduce-examples-3.3.6.jar
```

Después puedes volver a ejecutar WordCount.

---

## 5. Visualizar los resultados

Hadoop guarda los resultados de cada ejecución dentro de la carpeta de salida correspondiente.

### Resultado del cuento

```bash
cat output_cuento/part-r-00000
```

### Resultado de la noticia

```bash
cat output_noticia/part-r-00000
```

### Resultado de la canción

```bash
cat output_song/part-r-00000
```

Cada línea muestra:

```text
palabra    frecuencia
```

Por ejemplo:

```text
Hadoop    3
datos     5
```

---

## 6. Comparar los resultados

Analiza los tres resultados y responde:

- ¿Cuál es la palabra que aparece más veces en cada texto?
- ¿Qué palabras aparecen repetidas en más de un texto?
- ¿En cuál de los tres textos se observa una mayor repetición de palabras?

---

# Ampliación: analizar los tres textos juntos

Ahora vamos a comprobar qué sucede cuando los tres archivos se procesan como un único texto.

## 7. Combinar los archivos

Utilizar `cat` para unir el contenido de los tres archivos:

```bash
cat cuento.txt noticia.txt song.txt > combinado.txt
```

Comprobar el contenido:

```bash
cat combinado.txt
```

---

## 8. Ejecutar WordCount sobre el archivo combinado

```bash
hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount combinado.txt output_combinado
```

Si `output_combinado` ya existe porque ejecutaste anteriormente el ejercicio:

```bash
rm -rf output_combinado
```

Y vuelve a ejecutar WordCount.

---

## 9. Visualizar el resultado combinado

```bash
cat output_combinado/part-r-00000
```

Ahora el conteo incluye las palabras de los tres textos.

Compara este resultado con los obtenidos anteriormente.

- ¿Qué palabras aparecen ahora con mayor frecuencia?
- ¿Coinciden con las palabras más frecuentes de los textos individuales?
- ¿Qué cambia cuando aumenta la cantidad de datos de entrada?

---

# Para profundizar un poco más

## 10. Ordenar los resultados por frecuencia

El archivo generado por WordCount contiene dos columnas:

```text
palabra    frecuencia
```

Podemos ordenar los resultados utilizando `sort`.

### De menor a mayor frecuencia

```bash
sort -k2 -n output_combinado/part-r-00000
```

### De mayor a menor frecuencia

```bash
sort -k2 -nr output_combinado/part-r-00000
```

Las opciones utilizadas son:

- `-k2` → ordenar utilizando la segunda columna.
- `-n` → interpretar el valor como número.
- `-r` → invertir el orden.

---

## 11. Mostrar solamente las palabras más frecuentes

Podemos combinar `sort` con `head`.

Por ejemplo, para mostrar las dos palabras con mayor frecuencia:

```bash
sort -k2 -nr output_combinado/part-r-00000 | head -2
```

El símbolo:

```bash
|
```

se denomina **pipe** y permite utilizar la salida de un comando como entrada del siguiente.

En este caso:

```text
sort → ordena los resultados
      ↓
head → muestra únicamente los primeros
```

---

## 12. Guardar el resultado en un archivo

Podemos guardar las dos palabras más frecuentes en un nuevo archivo:

```bash
sort -k2 -nr output_combinado/part-r-00000 | head -2 > resultado_top.txt
```

El operador:

```bash
>
```

redirige la salida del comando hacia un archivo.

Visualizar el contenido:

```bash
cat resultado_top.txt
```

---

## 13. Cambiar el nombre del archivo

Podemos cambiar el nombre utilizando `mv`:

```bash
mv resultado_top.txt palabras_mas_frecuentes.txt
```

Comprobar el resultado:

```bash
ls -l
```

Y visualizarlo:

```bash
cat palabras_mas_frecuentes.txt
```

---

## Conclusión

En este ejercicio hemos aplicado el mismo programa **WordCount** sobre diferentes conjuntos de datos.

Hemos observado cómo MapReduce:

1. recibe los datos de entrada;
2. identifica las palabras;
3. genera pares clave–valor;
4. agrupa las palabras iguales;
5. calcula su frecuencia;
6. genera un resultado final.

También hemos comprobado que el mismo proceso puede ejecutarse sobre diferentes archivos sin modificar el programa.

Este principio es fundamental en Hadoop: **el procesamiento puede mantenerse mientras cambian o aumentan los datos de entrada**.