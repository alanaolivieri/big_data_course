# Preparación del entorno de Python

Python puede escribirse y ejecutarse desde diferentes entornos.

En esta guía veremos tres opciones para trabajar con Python y notebooks:

1. **Google Colab**
2. **Jupyter Notebook**
3. **Visual Studio Code**

Los tres entornos nos permiten trabajar con Python. La diferencia principal está
en dónde se ejecuta el código y en la preparación necesaria para empezar a trabajar.

## Teclado en español en toda la máquina virtual

Configura la distribución antes de abrir un editor o notebook. En una máquina
virtual basada en Debian o Ubuntu, abre una terminal **dentro de la máquina
virtual** y ejecuta:

```bash
sudo dpkg-reconfigure keyboard-configuration
```

Conserva el modelo de teclado sugerido si coincide con tu teclado y selecciona
**Español (España)** como distribución. Reinicia la máquina virtual para aplicar
la configuración del sistema. Si el escritorio sigue usando otra distribución,
abre sus **Ajustes → Teclado → Fuentes de entrada** (el nombre del menú depende
del escritorio), añade **Español (España)** y selecciónalo como distribución activa.

La distribución del escritorio se aplica donde escribes dentro de la máquina
virtual, incluida la terminal integrada de Visual Studio Code y Colab si lo
abres en el navegador de la máquina virtual. Si abres Colab en el navegador de
Windows, Colab usará la distribución activa de Windows. Comprueba que puedes
escribir `ñ`, `.`, `(` y `)` en el entorno que vas a usar.

En una sesión gráfica X11, `setxkbmap es` puede servir como cambio temporal
para la sesión. Para que el ajuste persista, usa la configuración anterior.

[Configuración del teclado en Debian](https://dyn.manpages.debian.org/bullseye/keyboard-configuration/keyboard.5.en.html)

---

# 1. Google Colab

Google Colab permite trabajar con notebooks directamente desde el navegador.

Es la opción más sencilla para empezar porque **no necesitamos instalar Python
ni preparar un entorno local**.

Para trabajar con Google Colab:

1. Abrimos [Google Colab](https://colab.research.google.com/) en el navegador.
2. Creamos un nuevo notebook o abrimos un archivo `.ipynb`.
3. Ejecutamos las celdas de código directamente desde el navegador.

> Si utilizamos Google Colab podemos omitir la instalación de Python descrita
> en las siguientes secciones.

---

# 2. Jupyter Notebook

Jupyter Notebook permite trabajar con archivos `.ipynb` desde nuestra propia
máquina.

A diferencia de Google Colab, para utilizar Jupyter Notebook localmente debemos
preparar primero nuestra máquina.

## 2.1. Abrir una terminal

Abrimos una terminal en la máquina virtual:
- Clicamos en el menú.
- En el buscador escribimos `terminal`.
- Lo seleccionamos.

Los siguientes comandos deben ejecutarse **uno por uno**.
Esperamos a que termine cada comando antes de ejecutar el siguiente.

---

## 2.2. Actualizar la lista de paquetes

Ejecutamos:

```bash
sudo apt update
```

Este comando actualiza la información de los paquetes disponibles en el sistema.

Si solicita la contraseña:

```text
eurecat
```

---

## 2.3. Instalar Python y pip

Ejecutamos:

```bash
sudo apt install -y python3 python3-pip
```

Con este comando instalamos:

- `python3`: el intérprete de Python.
- `python3-pip`: el gestor de paquetes de Python.

`pip` nos permitirá instalar otras herramientas y librerías de Python.

---

## 2.4. Actualizar pip

Ejecutamos:

```bash
python3 -m pip install --user --upgrade pip
```

Esto actualiza `pip` para el usuario actual.

---

## 2.5. Instalar Jupyter Notebook

Ejecutamos:

```bash
python3 -m pip install --user notebook
```

---

## 2.6. Iniciar Jupyter Notebook

Ejecutamos este comando desde la carpeta `PySpark` del curso en la máquina virtual:

```bash
python3 -m notebook
```

Mantén la terminal abierta mientras trabajas. Si el navegador no se abre
automáticamente, copia la URL completa que muestra Jupyter y pégala en el
navegador de la máquina virtual. Por ejemplo,
`http://localhost:8888/tree?token=TU_TOKEN`. Usa el puerto y el token que
aparezcan en tu terminal. Desde el explorador de Jupyter, entra en `notebooks`
y abre `00_intro_python.ipynb`.

Si abres el navegador en Windows, `localhost` apunta a Windows. Para seguir
estos pasos tal como están, abre el navegador dentro de la máquina virtual.

Podrás usar el mismo Jupyter para PySpark cuando el kernel tenga disponible
PySpark y el entorno de la máquina virtual esté preparado para ejecutar Spark.
La URL anterior abre Jupyter. La sesión de Spark se inicia desde el código
del notebook de PySpark.

[Guía de inicio de Jupyter](https://docs.jupyter.org/en/latest/running.html)

---

## 2.7. Comprobar que Python funciona

Creamos o abrimos un notebook y ejecutamos:

```python
print("Hola mundo")
```

El resultado debería ser:

```text
Hola mundo
```

Si aparece este resultado, podemos ejecutar correctamente Python desde
Jupyter Notebook.

---

# 3. Visual Studio Code

Visual Studio Code permite trabajar con archivos, carpetas, extensiones,
proyectos y notebooks `.ipynb` desde un mismo entorno.

En nuestra máquina virtual podemos preparar Visual Studio Code para ejecutar
directamente notebooks de Python.

## 3.1. Abrir una nueva terminal en Visual Studio Code

En el menú superior seleccionamos:

**Terminal → New Terminal**

La terminal nos permite ejecutar comandos directamente en la máquina virtual.

> Los siguientes comandos deben ejecutarse **uno por uno**. Esperamos a que
> termine cada comando antes de ejecutar el siguiente.

---

## 3.2. Actualizar la lista de paquetes

Ejecutamos:

```bash
sudo apt update
```

Este comando actualiza la información de los programas y paquetes disponibles
en el sistema.

Si solicita la contraseña:

```text
eurecat
```

---

## 3.3. Instalar Python y pip

Ejecutamos:

```bash
sudo apt install -y python3 python3-pip
```

Con este comando instalamos:

- `python3`: el intérprete que ejecutará nuestro código Python.
- `python3-pip`: el gestor de paquetes de Python.

`pip` funciona como un gestor desde el que podemos instalar las herramientas y
librerías adicionales que necesitaremos posteriormente.

---

## 3.4. Verificar que pip está instalado

Ejecutamos:

```bash
pip3 --version
```

Este comando nos permite comprobar que `pip` está disponible.

Debería aparecer una salida similar a:

```text
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.x)
```

> La versión concreta puede ser diferente.

---

## 3.5. Actualizar pip

Ejecutamos:

```bash
python3 -m pip install --user --upgrade pip
```

Con este comando actualizamos `pip` para el usuario actual.

---

## 3.6. Instalar ipykernel

Para ejecutar Python desde un notebook necesitamos disponer de un kernel.

Ejecutamos:

```bash
python3 -m pip install ipykernel --user --force-reinstall
```

`ipykernel` permite que Visual Studio Code utilice Python para ejecutar las
celdas de código de nuestros notebooks `.ipynb`.

La opción `--force-reinstall` vuelve a instalar `ipykernel` aunque ya exista una
instalación previa.

---

## 3.7. Abrir un notebook

Abrimos un archivo con extensión:

```text
.ipynb
```

O vamos a **File → New File... → Jupyter Notebook**

Si Visual Studio Code solicita seleccionar un intérprete o un kernel de Python,
seleccionamos el entorno de Python que acabamos de preparar, aparecerá como **Recommended**.

Pedirá instalar las extensiones así que solo aceptamos la instalación.

---

## 3.8. Comprobar que Python funciona

En el notebook que abrimos ejecutamos en una celda de código:

```python
print("Hola mundo")
```

El resultado debería ser:

```text
Hola mundo
```

Si obtenemos este resultado, nuestro notebook está ejecutando correctamente
código Python desde Visual Studio Code.

---

# Resumen

Tenemos tres alternativas para trabajar con Python:

| Entorno | ¿Dónde trabajamos? | ¿Necesita preparación local? |
|---|---|---|
| **Google Colab** | Navegador | No |
| **Jupyter Notebook** | Máquina virtual + navegador | Sí |
| **Visual Studio Code** | Máquina virtual + editor | Sí |

Independientemente del entorno elegido, el lenguaje que utilizamos es
**Python**.

La diferencia está en el entorno desde el que escribimos y ejecutamos nuestro
código.

Una vez tengamos Python funcionando, podremos continuar nuestro recorrido:

```text
Python
  ↓
PySpark
  ↓
Apache Spark
```

Python será el lenguaje con el que escribiremos nuestras instrucciones,
PySpark nos permitirá comunicarlas a Spark y Apache Spark realizará el
procesamiento.

## Navegación

[Volver al README](README.md) · [Siguiente: Primeros pasos con Python](notebooks/00_intro_python.ipynb)
