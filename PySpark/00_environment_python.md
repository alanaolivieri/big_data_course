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
setxkbmap -layout es -model pc105 -variant ""
```

En una sesión gráfica, `setxkbmap es` puede servir como cambio temporal
para la sesión.

[Configuración del teclado en Debian](https://dyn.manpages.debian.org/bullseye/keyboard-configuration/keyboard.5.en.html)

---

# 1. Google Colab

Google Colab permite trabajar con notebooks directamente desde el navegador.

Es la opción más sencilla para empezar porque **no necesitamos instalar Python
ni preparar un entorno local**.

Para trabajar con Google Colab:

1. Abrimos [Google Colab](https://colab.research.google.com/) en el navegador.
2. Creamos un nuevo notebook o abrimos un archivo `.ipynb`.
3. En `conectar`, clicamos en `Conectar a un entorno de ejecución alojado`.
4. Ejecutamos las celdas de código directamente desde el navegador.

> Si utilizamos Google Colab podemos omitir la instalación de Python descrita
> en las siguientes secciones.
> WARNING: Aquí dependeríamos directamente de los recursos gratuitos de Google Colab tenga a disposición, por ende no están garantizados y su disponibilidad puede variar. [Advertencia](research.google.com)

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

Si hay un warning del PATH:
```text
WARNING: The scripts pip, pip3 and pip3.8 are installed in
'/home/eurecat/.local/bin' which is not on PATH.
```

Esto significa que los ejecutables de pip se instalaron en una carpeta que Ubuntu no tiene incluida en la variable PATH. Por lo tanto, agregamos la carpeta al PATH
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Comprobamos:
```bash
python3 -m pip --version
```

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
navegador de la máquina virtual `http://localhost:8888/tree`. En el explorador de Jupyter, estaremos justo en la misma `Carpeta personal`, ya aquí puedes iniciar un nuevo notebook o utilizar uno antiguo.

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

Esto actualiza `pip` para el usuario actual.

Si hay un warning del PATH:
```text
WARNING: The scripts pip, pip3 and pip3.8 are installed in
'/home/eurecat/.local/bin' which is not on PATH.
```

Esto significa que los ejecutables de pip se instalaron en una carpeta que Ubuntu no tiene incluida en la variable PATH. Por lo tanto, agregamos la carpeta al PATH
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Comprobamos:
```bash
python3 -m pip --version
```

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
