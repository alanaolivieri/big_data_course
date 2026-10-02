# Recursos de Hadoop — Curso de Big Data

Esta carpeta contiene los materiales prácticos relacionados con **Hadoop, HDFS, MapReduce, Docker y Hive** utilizados en el curso de Big Data de **Eurecat IT Academy**.

## Contenido

### `01_exercise`
Práctica guiada principal de Hadoop.

Incluye:
- Instalación y configuración de Hadoop.
- Ejecución de un ejemplo de **MapReduce / WordCount**.
- Creación de un clúster Hadoop con **Docker**.
- Trabajo con archivos en **HDFS**.
- Configuración básica de **Hive** y carga de datos desde CSV.
- Ejemplos y capturas de apoyo.

### `02_exercise_wordcount`
Ejercicio práctico de **MapReduce**.

El objetivo es utilizar `WordCount` para analizar diferentes archivos de texto y comparar la frecuencia de aparición de las palabras.

Incluye el enunciado y su solución.

### `03_Hive_and_Bee`
Ejercicio práctico de **Hive**.

Permite trabajar con consultas SQL sobre una tabla de opiniones cargada desde un archivo CSV.

Incluye:
- Preparación del entorno con Docker y Hive.
- Conexión mediante Beeline.
- Consultas, filtros y agregaciones.
- Creación de nuevas tablas.
- Solución de errores habituales.
- Enunciado y solución de los ejercicios.

### `install`
Archivos necesarios para desplegar un entorno Hadoop con **Docker**.

Contiene la configuración del clúster y de sus servicios, como NameNode, DataNode, ResourceManager y NodeManager.

### `troubleshooting_hive.md`
Archivo auxiliar con comandos para resolver problemas relacionados con el contenedor de **Hive**, especialmente cuando `myhiveserver` se encuentra detenido o debe crearse nuevamente.

## Objetivo

Estos recursos permiten practicar los principales conceptos trabajados en Hadoop:

- almacenamiento distribuido con **HDFS**;
- procesamiento de datos con **MapReduce**;
- ejecución de servicios mediante **Docker**;
- consulta y análisis de datos con **Hive**.
