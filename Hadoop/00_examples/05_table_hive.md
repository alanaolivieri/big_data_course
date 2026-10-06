# Ejemplo — Crear y consultar una tabla con Hive

## Objetivo

Crear una tabla en Hive a partir de un archivo CSV, cargar los datos y ejecutar consultas básicas para comprobar que todo funciona correctamente.

Antes de comenzar, asegúrate de:

- tener `myhiveserver` en ejecución;
- estar conectado a Hive mediante Beeline;
- tener disponible el archivo `BigData_Custom_Sample.csv`.

---

## 1. Comprobar las tablas disponibles

Desde Beeline, ejecutar:

```sql
SHOW TABLES;
```

Este comando muestra todas las tablas disponibles en la base de datos actual.

Si todavía no hemos creado ninguna tabla, el resultado estará vacío.

---

## 2. Crear la tabla `opiniones`

Ejecutar:

```sql
CREATE TABLE opiniones (
    id INT,
    edad INT,
    sexo STRING,
    pais_donde_vive STRING,
    opinion_big_data STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
TBLPROPERTIES ("skip.header.line.count"="1");
```

### ¿Qué estamos indicando?

Con esta sentencia estamos definiendo la estructura de la tabla:

- `id` → número entero;
- `edad` → número entero;
- `sexo` → texto;
- `pais_donde_vive` → texto;
- `opinion_big_data` → texto.

La instrucción:

```sql
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
```

indica que los campos del archivo están separados por comas.

La propiedad:

```sql
TBLPROPERTIES ("skip.header.line.count"="1")
```

indica a Hive que ignore la primera fila del CSV, ya que contiene los nombres de las columnas.

---

## 3. Comprobar que la tabla se ha creado

Ejecutar:

```sql
SHOW TABLES;
```

Debería aparecer:

```text
opiniones
```

Esto confirma que Hive ha registrado la tabla correctamente.

---

## 4. Cargar el archivo CSV

Ejecutar:

```sql
LOAD DATA INPATH '/hive_custom_data/BigData_Custom_Sample.csv'
INTO TABLE opiniones;
```

Con este comando cargamos el archivo CSV en la tabla `opiniones`.

La ruta:

```text
/hive_custom_data/BigData_Custom_Sample.csv
```

corresponde a la carpeta compartida anteriormente entre la máquina virtual y el contenedor de Hive.

---

## 5. Verificar los datos

Consultar los primeros registros:

```sql
SELECT *
FROM opiniones
LIMIT 10;
```

Este comando permite comprobar rápidamente:

- que la tabla contiene datos;
- que las columnas se están interpretando correctamente;
- que la primera fila del CSV no se está utilizando como registro.

---

## 6. Primera consulta: promedio de edad

Calcular la edad promedio:

```sql
SELECT AVG(edad) AS edad_promedio
FROM opiniones;
```

Aquí:

- `AVG(edad)` calcula el promedio;
- `AS edad_promedio` asigna un nombre al resultado.

---

## 7. Segunda consulta: filtrar datos

Mostrar únicamente las personas mayores de 30 años:

```sql
SELECT id, edad, sexo, pais_donde_vive
FROM opiniones
WHERE edad > 30;
```

La cláusula:

```sql
WHERE edad > 30
```

filtra los registros y conserva únicamente los que cumplen la condición.

---

## 8. Tercera consulta: agrupar y contar

Contar cuántas personas hay por país:

```sql
SELECT pais_donde_vive, COUNT(*) AS cantidad
FROM opiniones
GROUP BY pais_donde_vive
ORDER BY cantidad DESC;
```

Aquí:

- `GROUP BY` agrupa los registros por país;
- `COUNT(*)` cuenta cuántos registros hay en cada grupo;
- `ORDER BY cantidad DESC` ordena los resultados de mayor a menor.

---

## 9. Consultar la actividad en HiveServer2

Abrir en el navegador:

```text
http://localhost:10002
```

Desde la interfaz de HiveServer2 se puede observar:

- las sesiones activas;
- las consultas en ejecución;
- las consultas que ya finalizaron;
- el estado de las consultas;
- el tiempo de ejecución.

Después de ejecutar los comandos anteriores, debería ser posible identificar operaciones como:

```text
CREATE TABLE
SHOW TABLES
LOAD DATA
SELECT
```

Esto permite comprobar visualmente que las consultas enviadas desde Beeline están siendo procesadas por HiveServer2.

---

## 10. Salir de Beeline

Para cerrar la sesión:

```text
Ctrl + D
```

Esto devuelve el control a la terminal de la máquina virtual.

---

## Resultado

Al finalizar este ejemplo se habrá:

- creado una tabla en Hive;
- definido su estructura;
- cargado datos desde un archivo CSV;
- comprobado el contenido;
- ejecutado consultas con `SELECT`, `WHERE`, `AVG`, `GROUP BY` y `ORDER BY`;
- observado la actividad desde HiveServer2.

Con esto el entorno queda preparado para realizar ejercicios de análisis de forma autónoma.