# Troubleshooting Hive

Utilizar esta guía únicamente si Hive no arranca correctamente o si no es posible conectarse con Beeline.

---

## 1. Comprobar el estado del contenedor

Mostrar todos los contenedores, incluidos los detenidos:

```bash
sudo docker ps -a
```

Buscar el contenedor:

```text
myhiveserver
```

### Si aparece como `Up`

El contenedor está funcionando.

Intentar conectarse con Beeline:

```bash
sudo docker exec -it myhiveserver beeline -u 'jdbc:hive2://localhost:10000/'
```

Si Hive acaba de arrancar, puede tardar unos segundos en aceptar conexiones. Volver a ejecutar el comando si fuera necesario.

---

## 2. El contenedor aparece como `Exited`

Si `myhiveserver` aparece con estado `Exited`, eliminarlo y crear un contenedor nuevo.

Eliminar el contenedor:

```bash
sudo docker rm myhiveserver
```

Si Docker indica que el contenedor todavía está en ejecución:

```bash
sudo docker stop myhiveserver
sudo docker rm myhiveserver
```

También puede hacerse directamente con:

```bash
sudo docker rm -f myhiveserver
```

> `-f` fuerza la eliminación del contenedor.

Esto elimina el **contenedor**, pero no la imagen de Apache Hive.

---

## 3. Crear nuevamente el contenedor de Hive

```bash
sudo docker run -d \
  -p 10000:10000 \
  -p 10002:10002 \
  --env SERVICE_NAME=hiveserver2 \
  -v /home/project/data:/hive_custom_data \
  --name myhiveserver \
  apache/hive:4.0.0-alpha-1
```

Comprobar que está funcionando:

```bash
sudo docker ps
```

---

## 4. Error: `The container name "/myhiveserver" is already in use`

Este error significa que Docker ya tiene un contenedor llamado `myhiveserver`.

Comprobarlo:

```bash
sudo docker ps -a
```

Si ya no se necesita el contenedor anterior:

```bash
sudo docker rm -f myhiveserver
```

Después crear nuevamente el contenedor.

También es posible conservarlo cambiándole el nombre:

```bash
sudo docker rename myhiveserver myhiveserver_old
```

---

## 5. Error: `port is already allocated`

Si aparece un mensaje similar a:

```text
Bind for 0.0.0.0:10000 failed: port is already allocated
```

significa que el puerto `10000` ya está siendo utilizado.

Comprobar qué contenedores están activos:

```bash
sudo docker ps
```

También puede comprobarse el puerto con:

```bash
sudo lsof -i :10000
```

Si otro contenedor está utilizando ese puerto, detenerlo antes de crear `myhiveserver`.

Por ejemplo:

```bash
sudo docker stop $(sudo docker ps -q --filter "publish=10000")
```

Después volver a crear el contenedor de Hive.

---

## 6. Conectarse nuevamente con Beeline

Una vez que `myhiveserver` aparece como `Up`:

```bash
sudo docker exec -it myhiveserver beeline -u 'jdbc:hive2://localhost:10000/'
```

La conexión correcta debería mostrar un prompt similar a:

```text
0: jdbc:hive2://localhost:10000>
```
