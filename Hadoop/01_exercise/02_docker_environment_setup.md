# Preparación del entorno Hadoop con Docker

Esta sección prepara el entorno necesario para trabajar con un clúster Hadoop utilizando **Docker**.

## 1. Instalar Docker y Git

Abrir una nueva terminal y ejecutar:

```bash
sudo snap install docker
sudo apt install git -y
```

La contraseña de administrador de la máquina virtual es:

```text
eurecat
```

## 2. Descargar la configuración del clúster

Clonar el repositorio que contiene la configuración necesaria para levantar el entorno Hadoop:

```bash
git clone https://github.com/alanaolivieri/docker_hadoop
```

Entrar en la carpeta descargada:

```bash
cd docker_hadoop
```

## 3. Iniciar el clúster Hadoop

Levantar los contenedores definidos en el proyecto:

```bash
sudo docker-compose up -d
```

El parámetro `-d` permite ejecutar los contenedores en segundo plano.

## 4. Comprobar los contenedores

Verificar que los servicios se han iniciado correctamente:

```bash
sudo docker ps
```

Deberían aparecer los principales componentes del clúster Hadoop.

### NameNode

Administra los metadatos de HDFS y sabe dónde están almacenados los bloques de datos.

### DataNode

Almacena físicamente los bloques de datos.

### ResourceManager

Gestiona los recursos disponibles del clúster, como CPU y memoria.

### NodeManager

Ejecuta las tareas asignadas por el ResourceManager.

## 5. Comprobar el estado

En la columna `STATUS` de Docker pueden aparecer estados como:

```text
Up (healthy)
```

Esto indica que el contenedor está en ejecución y que el servicio funciona correctamente.

Otros estados como:

```text
Exited
Restarting
Unhealthy
```

pueden indicar que existe algún problema con el servicio.

## 6. Acceder a la interfaz web de Hadoop

Abrir un navegador dentro de la máquina virtual y acceder a:

```text
http://localhost:9870
```

Desde esta interfaz se puede consultar información del **NameNode** y explorar posteriormente los archivos almacenados en HDFS.

También puede utilizarse el puerto:

```text
8088
```

para acceder a la interfaz de YARN.

## Entorno preparado

Una vez que los contenedores estén funcionando correctamente, el entorno estará listo para comenzar el ejemplo práctico de **HDFS**.