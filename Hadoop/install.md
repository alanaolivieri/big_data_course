# Instalación

## Actualizamos 
sudo apt update
apt list --upgradable

## Instalamos Java
sudo apt install openjdk-11-jdk -y

## Descargamos Hadoop
wget https://downloads.apache.org/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz

wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz

## Descomprimimos archivo de descarga
tar xzf hadoop-3.3.6-aarch64.tar.gz

### Listado de archivos en una carpeta
ls

## Mover carpeta de hadoop
sudo mv hadoop-3.3.6 /opt/hadoop

## Variables hadoop al bash
nano .bashrc

Al final del archivo pegar

export HADOOP_HOME=/opt/hadoop

export HADOOP_INSTALL=$HADOOP_HOME

export HADOOP_MAPRED_HOME=$HADOOP_HOME

export HADOOP_COMMON_HOME=$HADOOP_HOME

export HADOOP_HDFS_HOME=$HADOOP_HOME

export YARN_HOME=$HADOOP_HOME

export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native

export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin


Después Ctrl+O para guardar
Enter para dejar el mismo nombre
Ctrl+X para cerrar

## Actualizamos
### Bash (configuración)
source .bashrc

### Java
sudo nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh

Buscamos export java
Ctrl+W escribimos "export java" y Enter

Borrar la #
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

Después Ctrl+O para guardar
Enter para dejar el mismo nombre
Ctrl+X para cerrar
