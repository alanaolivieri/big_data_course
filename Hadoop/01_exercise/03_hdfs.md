# Ejemplo 2 — Trabajo con HDFS

En este ejemplo vamos a trabajar con **HDFS (Hadoop Distributed File System)** utilizando el clúster Hadoop que hemos levantado previamente con Docker.

## Objetivo

El objetivo es:

- acceder al contenedor del NameNode;
- crear directorios dentro de HDFS;
- cargar archivos;
- comprobar que los datos están almacenados;
- visualizar los archivos desde la interfaz web de Hadoop.

## 1. Acceder al contenedor del NameNode

Abrir una terminal y ejecutar:

```bash
sudo docker exec -it namenode bash
```

Este comando permite abrir una terminal dentro del contenedor donde se está ejecutando el **NameNode**.

## 2. Crear un directorio en HDFS

Crear el directorio:

```bash
hdfs dfs -mkdir -p /user/root/input
```

La opción `-p` permite crear toda la estructura de directorios necesaria si todavía no existe.

## 3. Copiar archivos de configuración a HDFS

Copiar los archivos `.xml` de configuración de Hadoop al directorio creado:

```bash
hdfs dfs -put $HADOOP_HOME/etc/hadoop/*.xml /user/root/input
```

Con este comando los archivos pasan del sistema de archivos del contenedor a **HDFS**.

## 4. Descargar un archivo de ejemplo

Descargar un archivo de texto:

```bash
curl https://raw.githubusercontent.com/ibm-developer-skills-network/ooxwv-docker_hadoop/master/SampleMapReduce.txt --output data.txt
```

El archivo se guardará con el nombre:

```text
data.txt
```

## 5. Cargar el archivo en HDFS

Copiar el archivo `data.txt` a HDFS:

```bash
hdfs dfs -put data.txt /user/root/
```

## 6. Visualizar los archivos desde la interfaz web

Abrir el navegador y acceder a:

```text
http://localhost:9870
```

En la interfaz del NameNode:

1. Ir a **Utilities**.
2. Seleccionar **Browse the file system**.
3. Navegar hasta:

```text
/user/root
```

Aquí debería aparecer el archivo `data.txt`.

También puede consultarse el directorio:

```text
/user/root/input
```

donde se encuentran los archivos `.xml` cargados anteriormente.

## 7. Consultar la información de los archivos

Desde la interfaz web es posible seleccionar un archivo y consultar información como:

- tamaño;
- número de bytes;
- identificador del bloque;
- ubicación del bloque.

HDFS utiliza por defecto bloques de **128 MB**, aunque el archivo almacenado sea mucho más pequeño.

## 8. Salir del contenedor

Para volver a la terminal de la máquina virtual:

```bash
exit
```

## Resultado

Al finalizar este ejemplo se habrá:

- accedido a un nodo del clúster Hadoop;
- creado un directorio en HDFS;
- cargado archivos en el sistema distribuido;
- comprobado su almacenamiento mediante la interfaz web del NameNode.