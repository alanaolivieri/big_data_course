# Prácticas de Hadoop

Esta carpeta contiene los materiales necesarios para preparar el entorno de trabajo y realizar tres prácticas introductorias con **Hadoop, HDFS y Hive**.

## Estructura

### Preparación del entorno

Antes de realizar los Ejemplos es necesario configurar las herramientas que se utilizarán durante las prácticas.

#### Hadoop

[00_environment_setup.md](00_environment_setup.md)

Preparación del entorno para trabajar con Hadoop de forma local.

Incluye:

- instalación de Java;
- descarga e instalación de Hadoop;
- configuración de variables de entorno;
- configuración de `JAVA_HOME`;
- comprobación de la instalación.

Esta preparación es necesaria para realizar el Ejemplo de **WordCount**.

#### Docker

[02_docker_environment_setup.md](02_docker_environment_setup.md)

Preparación del entorno Hadoop con Docker.

Incluye:

- instalación de Docker;
- instalación de Git;
- descarga del proyecto desde GitHub;
- creación y arranque de los contenedores;
- comprobación del estado del clúster;
- introducción a los principales componentes:
  - NameNode;
  - DataNode;
  - ResourceManager;
  - NodeManager.

Esta preparación se utiliza para el Ejemplo de **HDFS**.

#### Hive

[04_hive_environment_setup.md]()

Preparación del entorno para trabajar con Hive.

Incluye:

- preparación del directorio de trabajo;
- descarga del conjunto de datos;
- descarga de la imagen de Hive;
- creación y arranque del contenedor;
- comprobación del estado del contenedor;
- conexión a Hive mediante Beeline.

Esta preparación es necesaria para el ejemplo de **Hive**.

---

## Ejemplos

### Ejemplo 1 — WordCount con MapReduce

Introducción práctica a MapReduce mediante el programa `WordCount`.

El Ejemplo permite:

- crear un archivo de texto;
- ejecutar un proceso MapReduce;
- contar la frecuencia de las palabras;
- consultar los resultados generados por Hadoop.

Archivo:

[01_wordcount.md](01_wordcount.md)

---

### Ejemplo 2 — Trabajar con HDFS

Práctica introductoria sobre el sistema de archivos distribuido de Hadoop.

El Ejemplo permite:

- acceder al contenedor del NameNode;
- crear directorios en HDFS;
- cargar archivos;
- consultar los archivos almacenados;
- visualizar la información desde la interfaz web de Hadoop.

Archivo:

[03_hdfs.md](03_hdfs.md)

---

### Ejemplo 3 — Hive y Beeline

Práctica para trabajar con datos estructurados mediante Hive.

El Ejemplo permite:

- ejecutar Hive mediante Docker;
- conectarse con Beeline;
- crear una tabla;
- cargar datos desde un archivo CSV;
- realizar consultas básicas;
- aplicar filtros, agregaciones y agrupaciones.

Archivo:

[05_hive_beeline.md]()

---

## Orden recomendado

1. Preparar el entorno local de Hadoop.
2. Realizar el Ejemplo de WordCount.
3. Preparar el entorno Docker.
4. Realizar el Ejemplo de HDFS.
5. Preparar el entorno Hive.
6. Realizar el Ejemplo de Hive y Beeline.

## Objetivo

Estas prácticas permiten introducir de forma progresiva algunos de los componentes principales del ecosistema Hadoop:

- **MapReduce** para procesamiento de datos;
- **HDFS** para almacenamiento distribuido;
- **Docker** para simular un entorno Hadoop con diferentes servicios;
- **Hive** para consultar y analizar datos mediante una sintaxis similar a SQL.