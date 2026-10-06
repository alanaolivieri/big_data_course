# Ejemplo 1 — WordCount con Hadoop

## Objetivo

Utilizar Hadoop para ejecutar un ejemplo sencillo de **MapReduce** mediante `WordCount`, un programa que cuenta cuántas veces aparece cada palabra dentro de un archivo de texto.

## 1. Crear la carpeta de trabajo

En la terminal, crear una carpeta para el ejercicio:

```bash
mkdir ejemplo_mapreduce
```

Entrar en la carpeta:

```bash
cd ejemplo_mapreduce
```

## 2. Crear el archivo de entrada

Crear un archivo de texto:

```bash
touch data.txt
```

Abrirlo con el editor `nano`:

```bash
nano data.txt
```

Escribir o pegar un texto que contenga algunas palabras repetidas.

Guardar el archivo:

- `Ctrl + O`
- `Enter`
- `Ctrl + X`

## 3. Descargar el ejemplo de MapReduce

Descargar el archivo `.jar` que contiene los ejemplos de MapReduce de Hadoop:

```bash
wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-mapreduce-examples/3.3.6/hadoop-mapreduce-examples-3.3.6.jar
```

Podemos comprobar los ejemplos disponibles ejecutando:

```bash
hadoop jar hadoop-mapreduce-examples-3.3.6.jar
```

## 4. Ejecutar WordCount

Ejecutar el programa `wordcount` sobre el archivo `data.txt`:

```bash
hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount data.txt output
```

Hadoop procesará el archivo y guardará el resultado dentro de la carpeta `output`.

## 5. Consultar los resultados

Mostrar el resultado en la terminal:

```bash
cat output/part-r-00000
```

El resultado mostrará cada palabra junto con el número de veces que aparece en el texto.

Ejemplo:

```text
Big     2
Data    3
Hadoop  2
```

También podemos ver esto en la interfaz gráfica utilizando.

```bash
nautilus .
```

## Volver a ejecutar el ejercicio

Hadoop no sobrescribe automáticamente la carpeta de salida.

Si queremos ejecutar nuevamente el programa, primero debemos eliminar la carpeta `output`:

```bash
rm -rf output
```

Después podemos volver a ejecutar:

```bash
hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount data.txt output
```

y consultar de nuevo los resultados:

```bash
cat output/part-r-00000
```

## Resultado esperado

Al finalizar el ejercicio se habrá:

- creado un archivo de entrada;
- ejecutado un proceso MapReduce con Hadoop;
- generado una salida;
- comprobado la frecuencia de aparición de las palabras.