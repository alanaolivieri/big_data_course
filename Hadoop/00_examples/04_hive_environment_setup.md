# Preparación del entorno de Hive y Beeline

## Objetivo

Preparar el entorno necesario para trabajar con **Apache Hive** y conectarse mediante **Beeline**.

Al finalizar esta guía tendremos:

- el archivo de datos disponible;
- la imagen de Apache Hive descargada;
- un contenedor con HiveServer2 en ejecución;
- conexión a Hive mediante Beeline.

---

## 1. Crear el directorio de datos

Crear la carpeta donde almacenaremos los archivos que utilizaremos con Hive:

```bash
sudo mkdir -p /home/project/data
```

Acceder al directorio:

```bash
cd /home/project/data
```

Esta carpeta se utilizará posteriormente para compartir archivos entre la máquina virtual y el contenedor de Hive.

---

## 2. Descargar el archivo de datos

Descargar el archivo CSV que utilizaremos durante la práctica:

```bash
wget -O BigData_Custom_Sample.csv https://raw.githubusercontent.com/alanaolivieri/big_data_course/main/Hadoop/00_examples/data/BigData_Custom_Sample.csv
```

Comprobar que el archivo se ha descargado:

```bash
ls -l
```

Debería aparecer:

```text
BigData_Custom_Sample.csv
```

Opcionalmente, se puede abrir el directorio con Visual Studio Code:

```bash
code .
```

---

## 3. Descargar la imagen de Apache Hive

Descargar la imagen que utilizaremos para crear el contenedor:

```bash
sudo docker pull apache/hive:4.0.0-alpha-1
```

Comprobar que la imagen está disponible:

```bash
sudo docker images
```

Debería aparecer una imagen similar a:

```text
apache/hive    4.0.0-alpha-1
```

---

## 4. Crear el contenedor de HiveServer2

Ejecutar:

```bash
sudo docker run -d \
  -p 10000:10000 \
  -p 10002:10002 \
  --env SERVICE_NAME=hiveserver2 \
  -v /home/project/data:/hive_custom_data \
  --name myhiveserver \
  apache/hive:4.0.0-alpha-1
```

### ¿Qué significa cada opción?

- `-d`  
  Ejecuta el contenedor en segundo plano.

- `-p 10000:10000`  
  Expone el puerto `10000`, utilizado para las conexiones con HiveServer2.

- `-p 10002:10002`  
  Expone el puerto `10002`, utilizado por la interfaz web de HiveServer2.

- `--env SERVICE_NAME=hiveserver2`  
  Indica que el servicio que debe iniciarse es HiveServer2.

- `-v /home/project/data:/hive_custom_data`  
  Comparte la carpeta de datos de la máquina virtual con el contenedor.

  Esto significa que:

```text
/home/project/data
```

en la máquina virtual estará disponible como:

```text
/hive_custom_data
```

dentro del contenedor.

- `--name myhiveserver`  
  Asigna el nombre `myhiveserver` al contenedor.

---

## 5. Comprobar que Hive está funcionando

Ejecutar:

```bash
sudo docker ps
```

Buscar el contenedor:

```text
myhiveserver
```

y comprobar que aparece con estado:

```text
Up
```

---

## 6. Acceder a la interfaz web de HiveServer2

Abrir un navegador y acceder a:

```text
http://localhost:10002
```

Desde esta interfaz se puede consultar información sobre HiveServer2, como:

- sesiones activas;
- consultas en ejecución;
- consultas finalizadas;
- información del servidor.

Esta interfaz sirve principalmente para comprobar que HiveServer2 está funcionando y para observar la actividad de las consultas.

---

## 7. Conectarse con Beeline

Ejecutar:

```bash
sudo docker exec -it myhiveserver beeline -u 'jdbc:hive2://localhost:10000/'
```

Si la conexión se realiza correctamente, aparecerá un prompt similar a:

```text
0: jdbc:hive2://localhost:10000>
```

A partir de este momento se pueden ejecutar consultas HiveQL.

Por ejemplo:

```sql
SHOW TABLES;
```

---

## 8. Volver a utilizar el entorno

Si el contenedor ya fue creado anteriormente pero está detenido, no es necesario volver a crearlo.

Iniciarlo con:

```bash
sudo docker start myhiveserver
```

Después conectarse nuevamente con Beeline:

```bash
sudo docker exec -it myhiveserver beeline -u 'jdbc:hive2://localhost:10000/'
```

---

## Entorno preparado

Si:

- `myhiveserver` aparece como `Up`;
- la interfaz `http://localhost:10002` responde;
- y Beeline muestra el prompt de conexión;

el entorno está listo para comenzar a trabajar con Hive.

Los problemas relacionados con contenedores detenidos, nombres duplicados o puertos ocupados se encuentran en:

```text
troubleshooting_hive.md
```