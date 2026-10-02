# Preparación del entorno Hadoop

Antes de realizar los ejercicios prácticos, debemos preparar la máquina virtual instalando **Java** y **Hadoop**.

## 1. Instalar Java

Hadoop necesita Java para funcionar.

Abrir una terminal y ejecutar:

```bash
sudo apt update
sudo apt install openjdk-11-jdk -y
```

La contraseña de administrador de la máquina virtual es:

```text
eurecat
```

## 2. Descargar e instalar Hadoop

Descargar Hadoop 3.3.6:

```bash
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
```

Descomprimir el archivo:

```bash
tar xzf hadoop-3.3.6.tar.gz
```

> **Nota**
>
> El comando `tar` puede tardar unos segundos y no muestra información mientras está trabajando.
>
> Para comprobar que la extracción ha finalizado correctamente:
>
> ```bash
> ls
> ```
>
> Debe aparecer la carpeta:
>
> ```text
> hadoop-3.3.6
> ```

Mover Hadoop al directorio `/opt/hadoop`:

```bash
sudo mv hadoop-3.3.6 /opt/hadoop
```

## 3. Configurar las variables de entorno

Abrir el archivo `.bashrc`:

```bash
nano ~/.bashrc
```

Añadir al final:

```bash
# Hadoop
export HADOOP_HOME=/opt/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
```

Guardar los cambios:

- `Ctrl + O` → guardar.
- `Enter` → confirmar.
- `Ctrl + X` → salir.

Aplicar la nueva configuración:

```bash
source ~/.bashrc
```

## 4. Configurar Java para Hadoop

Abrir el archivo de configuración:

```bash
sudo nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh
```

Buscar:

```bash
# export JAVA_HOME=
```

y sustituirlo por:

```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

Guardar con:

- `Ctrl + O`
- `Enter`
- `Ctrl + X`

## 5. Verificar la instalación

Ejecutar:

```bash
hadoop
```

Si la instalación y la configuración son correctas, se mostrará la ayuda de Hadoop con los comandos disponibles.

Con esto, el entorno ya está preparado para comenzar los ejercicios.
