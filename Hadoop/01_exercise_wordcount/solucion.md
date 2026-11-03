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

### 7.1. Ejecutar WordCount sobre el archivo combinado

```bash
hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount combinado.txt output_combinado
```

Si `output_combinado` ya existe porque ejecutaste anteriormente el ejercicio:

```bash
rm -rf output_combinado
```

Y vuelve a ejecutar WordCount.

---

### 7.2. Visualizar el resultado combinado

```bash
cat output_combinado/part-r-00000
```

Ahora el conteo incluye las palabras de los tres textos.

Compara este resultado con los obtenidos anteriormente.

- ¿Qué palabras aparecen ahora con mayor frecuencia?
- ¿Coinciden con las palabras más frecuentes de los textos individuales?
- ¿Qué cambia cuando aumenta la cantidad de datos de entrada?

---

## 8. Usar una sola línea

Podemos ejecutar WordCount sobre varios archivos en una sola línea utilizando el operador lógico ``&&``.

Este operador indica que el siguiente comando se ejecutará solo si el comando anterior termina correctamente.

```bash
hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount cuento.txt output_cuento && hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount song.txt output_song && hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount noticia.txt output_noticia
```

De esta forma:

- se procesa cuento.txt;
- si termina correctamente, se procesa song.txt;
- si también termina correctamente, se procesa noticia.txt.

Para visualizar el contenido deberemos hacerlo como en el [paso 5](#5-visualizar-los-resultados) , ya que cada ejecución genera una carpeta de salida diferente:

```text
output_cuento
output_song
output_noticia
```
---

# Para profundizar un poco más

## 9. Ordenar los resultados por frecuencia

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

## 10. Mostrar solamente las palabras más frecuentes

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

## 11. Guardar el resultado en un archivo

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

## 12. Cambiar el nombre del archivo

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

---

# Comparación Python vs Hadoop

En este apartado vamos a ejecutar el mismo proceso de **WordCount** utilizando dos enfoques diferentes:

- **Python**
- **Hadoop MapReduce**

Ambos ejecutados dentro de la máquina virtual.

Para la comparación utilizaremos tres archivos de distinto tamaño:

- `texto_100MB.txt`
- `texto_1GB.txt`
- `texto_5GB.txt`

La carpeta completa `txt_grandes` estará disponible para descargar desde el [Drive](https://drive.google.com/file/d/1Xt_HrKSq73HJPGq8UqeTdgZ8Ewcvks9m/view?usp=sharing).

Como la descarga la hace, por defecto, a la carpeta de descargas en un archivo comprimido .zip, necesitaremos moverlo a la carpeta del ejemplo y descomprimirlo. Podemos hacerlo de dos formas:

1. Por terminal:

Lo movemos a la carpeta del ejemplo que estamos utilizando
```bash
mv ~/Descargas/txt_grandes.zip ~/ejemplo_mapreduce/
```

Descomprimimos:
```bash
unzip txt_grandes.zip
```

Si te dice que unzip no está instalado:
```bash
sudo apt update
sudo apt install unzip -y
```

Repetimos el paso de descomprimir.

2. Por la parte gráfica

También podemos mover el archivo utilizando el explorador de archivos de Ubuntu.

1. Abrimos **Archivos**.
2. Entramos en la carpeta **Descargas**.
3. Seleccionamos el archivo descargado.
4. Hacemos clic derecho y seleccionamos **Cortar**, o utilizamos `Ctrl + X`.
5. En el panel izquierdo haz clic en **Carpeta personal** o **Home** y entramos a `ejemplo_mapreduce`.
6. Hacemos clic derecho dentro de la carpeta y seleccionamos **Pegar**, o utilizamos `Ctrl + V`.
7. Hacemos clic derecho sobre la carpeta comprimida y seleccionamos **Extraer aquí**

De esta forma, el archivo quedará dentro de la carpeta donde estamos realizando el ejemplo.


---

## 1. Hipótesis antes de ejecutar

Antes de comenzar, planteamos una pregunta:

> **¿A medida que aumenta el tamaño del archivo, creen que Hadoop será más rápido que Python?**

Podemos pensar inicialmente que Hadoop debería ganar porque está diseñado para trabajar con grandes volúmenes de datos.

Sin embargo, hay un detalle importante:

**en esta práctica Python y Hadoop están ejecutándose sobre los mismos recursos físicos.**

Nuestro entorno es aproximadamente:

```text
Máquina virtual
├── Python
└── Hadoop
```

Aunque Hadoop pueda dividir el trabajo en varias tareas, todas ellas siguen utilizando la CPU, la memoria y el disco disponibles en esa misma máquina virtual.

---

## 2. Medir el tiempo con Hadoop

Para medir cuánto tarda Hadoop podemos utilizar el comando `time`.

Con el archivo de 100 MB:

```bash
time hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount txt_grandes/texto_100MB.txt output_100MB
```

Para 1 GB:

```bash
time hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount txt_grandes/texto_1GB.txt output_1GB
```

Para 5 GB:

```bash
time hadoop jar hadoop-mapreduce-examples-3.3.6.jar wordcount txt_grandes/texto_5GB.txt output_5GB
```

> **Importante:** las carpetas de salida no pueden existir previamente.  
> Si ya existen, Hadoop devolverá un error.

Podemos eliminarlas antes de repetir la prueba:

```bash
rm -rf output_100MB output_1GB output_5GB
```

---

## 3. Medir el tiempo con Python

Ejecutaremos un programa Python que realice el mismo WordCount el cual descargamos de [aquí](https://drive.google.com/file/d/1Snx-Vph8z3YwZf-DQMrdrLP4wwbkDeTq/view?usp=sharing) que es el mismo [archivo](wordcount.py) que se encuentra en este repositorio.

Lo movemos a la carpeta del ejemplo que estamos utilizando
```bash
mv ~/Descargas/wordcount.py ~/ejemplo_mapreduce/
```

Por ejemplo:

```bash
time python3 wordcount.py txt_grandes/texto_100MB.txt output_py_100MB
```

```bash
time python3 wordcount.py txt_grandes/texto_1GB.txt output_py_1GB
```

```bash
time python3 wordcount.py txt_grandes/texto_5GB.txt output_py_5GB
```

El objetivo es comparar el tiempo total de ejecución utilizando exactamente los mismos archivos.

> **Importante:** fíjense si al ejecutar el archivo aparece el mensaje `Terminado (killed)`.
>
> Esto significa que el sistema operativo detuvo el proceso porque estaba consumiendo demasiados recursos, normalmente memoria RAM.
>
> No significa que Python haya terminado correctamente. En este caso, el procesamiento no se completó.


---

## 4. Registrar los resultados

Completa la siguiente tabla con los tiempos obtenidos:

| Tamaño | Python | Hadoop |
|---|---:|---:|
| 100 MB |  |  |
| 1 GB |  |  |
| 5 GB |  |  |

Después observa:

- ¿qué herramienta ha sido más rápida?
- ¿la diferencia aumenta o disminuye al crecer el archivo?
- ¿el comportamiento es el mismo para los tres tamaños?

---

## 5. ¿Por qué Hadoop puede ser más lento?

Hadoop tiene un coste adicional de preparación y coordinación.

Antes de producir el resultado debe realizar diferentes tareas:

```text
Preparar el job
      ↓
Dividir la entrada
      ↓
Ejecutar Map
      ↓
Shuffle y Sort
      ↓
Ejecutar Reduce
      ↓
Escribir la salida
```

Todo este proceso introduce un coste adicional llamado **overhead**.

Python, en cambio, puede leer directamente el archivo y realizar el conteo utilizando los recursos de una sola máquina.

Por eso, con archivos pequeños o medianos y una sola máquina, es perfectamente posible que **Python sea más rápido que Hadoop**

Esto no significa que Hadoop funcione mal. Significa que estamos utilizando Hadoop en un escenario donde todavía no puede aprovechar su principal ventaja.

---

## 6. ¿Dónde aparece realmente la ventaja de Hadoop?

La ventaja de Hadoop aparece cuando los datos y el procesamiento se distribuyen entre varios nodos.

En un clúster real podríamos tener:

```text
                    archivo muy grande
                           ↓
                    Hadoop / HDFS
                           ↓
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
       Nodo 1           Nodo 2           Nodo 3
       parte A          parte B          parte C
          ↓                ↓                ↓
       procesa          procesa          procesa
          └────────────────┼────────────────┘
                           ↓
                       resultado
```

El trabajo puede dividirse y ejecutarse en paralelo utilizando los recursos de varias máquinas.

En cambio, un programa Python local tendría un esquema como:

```text
archivo muy grande
       ↓
una máquina
       ↓
CPU + memoria
       ↓
resultado
```

La capacidad de procesamiento queda limitada por los recursos de ese único equipo.

---

## 7. La conclusión importante

Esta práctica no pretende demostrar que:

> **Hadoop siempre es más rápido que Python.**

De hecho, en nuestra máquina virtual es posible que Python sea más rápido incluso con archivos relativamente grandes.

La idea importante es otra:

> **Hadoop está diseñado para escalar horizontalmente.**

Es decir, cuando aumentan mucho los datos, podemos añadir más nodos y repartir tanto el almacenamiento como el procesamiento.

Por eso la pregunta correcta no es:

> “¿Hadoop es más rápido que Python?”

Sino:

> **“¿Qué ocurre cuando los datos dejan de caber o de procesarse cómodamente en una sola máquina?”**

Ahí es donde el procesamiento distribuido empieza a aportar una ventaja real.

---

## Reflexión final

Si Python tarda menos en esta práctica, el resultado no contradice lo aprendido.

Al contrario, demuestra una idea fundamental:

> **No debemos utilizar una tecnología Big Data simplemente porque los datos sean grandes.**

La tecnología adecuada depende de:

- volumen de datos;
- recursos disponibles;
- tiempo de procesamiento requerido;
- posibilidad de distribuir el trabajo;
- complejidad que estamos dispuestos a asumir.

Hadoop empieza a tener sentido cuando el volumen y la infraestructura permiten aprovechar realmente el **procesamiento distribuido**.
