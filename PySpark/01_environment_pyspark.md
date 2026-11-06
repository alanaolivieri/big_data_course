# Preparación del entorno de PySpark

Elige **una** de las tres opciones. En esta práctica usaremos **Java 17 y PySpark 3.5.x**. Si vas a trabajar en la máquina virtual, parte de la [guía del entorno de Python](00_environment_python.md).

## 1. Google Colab

### 1.1. Usar el entorno de Google


1. Abre un notebook temporal en Colab y ejecuta `!java -version` en una celda.
2. Si necesitas instalar Java 17, ejecuta `!apt-get update -qq` y después `!apt-get install -y openjdk-17-jre-headless`, en celdas separadas.
3. Si todavía no tienes PySpark 3.5.x, ejecuta la siguiente celda y reinicia la sesión de Python:

```python
%pip install "pyspark>=3.5,<3.6"
```

4. Si Colab está seleccionando otra versión de Java, ejecuta estas líneas antes de iniciar Spark. Ajusta la ruta si Java 17 está instalado en otra carpeta:

```python
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-17-openjdk-amd64"
```

Este ajuste vale para el kernel actual. Si lo necesitas en el cuaderno de práctica, repite esas líneas allí antes de iniciar Spark. Continúa con la [comprobación](#4-comprobar-que-spark-arranca).

### 1.2. Conectar Colab a un servidor local en la máquina virtual

Con esta opción abres Colab en el navegador de la **máquina virtual** y el código también se ejecuta en la VM. Usarás el Python, Java y los archivos accesibles desde el kernel de Jupyter de la VM.

1. En la VM, prepara [Jupyter Notebook](00_environment_python.md#2-jupyter-notebook) y comprueba [Java en la máquina virtual](#java-en-la-máquina-virtual).
2. En la terminal de la VM, desde la carpeta `PySpark`, inicia Jupyter con este comando y deja la terminal abierta:

```bash
python3 -m notebook \
  --ip=127.0.0.1 \
  --port=8888 \
  --NotebookApp.port_retries=0 \
  --NotebookApp.allow_origin='https://colab.research.google.com' \
  --NotebookApp.allow_credentials=True \
  --no-browser
```

3. Copia la URL completa que muestra la terminal, incluido el token. Tendrá una forma parecida a `http://127.0.0.1:8888/?token=TU_TOKEN`. Si el puerto 8888 ya está ocupado, usa otro en el comando y copia la nueva URL. Guarda el token para tu sesión.
4. Abre **Google Colab en el navegador de la VM**. En el menú **Conectar**, elige **Conectar a un entorno de ejecución local**, pega la URL y confirma. Usa el navegador de la VM porque `127.0.0.1` apunta a la máquina donde está abierto.
5. Si el kernel local todavía no tiene PySpark 3.5.x, ejecuta `%pip install "pyspark>=3.5,<3.6"` en una celda de Colab ya conectado al servidor local. Reinicia el kernel si hace falta y ejecuta la [comprobación de Spark](#4-comprobar-que-spark-arranca).

[Instrucciones oficiales de Colab para la conexión local](https://research.google.com/colaboratory/local-runtimes.html)


## 2. Jupyter Notebook

1. Comprueba [Java en la máquina virtual](#java-en-la-máquina-virtual).
2. Desde la carpeta `PySpark`, ejecuta `python3 -m notebook` en la terminal. Si el navegador no se abre automáticamente, usa la URL que muestra Jupyter.
3. Crea un notebook temporal y selecciona el mismo kernel de Python que usarás para la práctica. Si hace falta instalar PySpark, ejecuta la celda siguiente y reinicia el kernel:

```python
%pip install "pyspark>=3.5,<3.6"
```

4. Ejecuta la [comprobación](#4-comprobar-que-spark-arranca).

## 3. Visual Studio Code

1. Comprueba [Java en la máquina virtual](#java-en-la-máquina-virtual).
2. Abre la carpeta `PySpark` en VS Code y crea un notebook temporal. En **Seleccionar kernel**, elige el entorno de Python que usarás también para la práctica.
3. Si necesitas instalar PySpark, ejecuta la celda siguiente y reinicia el kernel:

```python
%pip install "pyspark>=3.5,<3.6"
```

4. Ejecuta la [comprobación](#4-comprobar-que-spark-arranca).

### Java en la máquina virtual

En la terminal de Debian o Ubuntu, ejecuta `java -version`. Si necesitas instalar Java 17, ejecuta:

```bash
sudo apt update
sudo apt install openjdk-17-jre-headless
```

Si hay varias versiones, indica la carpeta de Java 17 en la terminal desde la que iniciarás Jupyter o VS Code. Esta es la ruta habitual en Ubuntu x86-64:

```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
```

Abre Jupyter o VS Code desde esa misma terminal para que sus kernels reciban el ajuste. Si VS Code ya estaba abierto, ciérralo antes de volver a abrirlo.

## 4. Comprobar que Spark arranca

Ejecuta esta celda en el notebook temporal del entorno que elegiste:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[2]").appName("Comprobación PySpark").getOrCreate()
try:
    print("Versión de Spark:", spark.version)
    print("Resultado:", spark.range(3).count())
finally:
    spark.stop()
```

Si aparece `Resultado: 3`, el kernel puede iniciar Spark y ejecutar un cálculo. Si falla el arranque, comprueba que `JAVA_HOME` apunta a la carpeta de Java 17 y que dentro existe `bin/java`. Si aparece `ModuleNotFoundError`, comprueba que instalaste PySpark en el mismo kernel. Si ya hay un contexto de Spark activo y el notebook no responde como esperas, reinicia el kernel y vuelve a ejecutar la comprobación.

[Documentación de instalación de PySpark 3.5](https://spark.apache.org/docs/3.5.9/api/python/getting_started/install.html)

## Navegación

[Volver al README](README.md) · [Siguiente: Introducción a PySpark](notebooks/01_intro_pyspark.ipynb)

