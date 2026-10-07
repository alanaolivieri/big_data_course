# Ejercicio práctico Hive — Análisis de Opiniones

## Objetivo

Aplicar los conceptos aprendidos sobre **HiveQL** para explorar y analizar los datos almacenados en la tabla `opiniones`.

En este ejercicio no se proporciona el código de las consultas. El objetivo es identificar qué operaciones SQL/HiveQL son necesarias para responder cada pregunta.

---

## Contexto

Ya tenemos cargado el archivo `BigData_Custom_Sample.csv` en la tabla:

```text
opiniones
```

La tabla contiene las siguientes columnas:

| Columna | Tipo | Descripción |
|---|---|---|
| `id` | INT | Identificador único de cada registro |
| `edad` | INT | Edad de la persona |
| `sexo` | STRING | Sexo reportado |
| `pais_donde_vive` | STRING | País de residencia |
| `opinion_big_data` | STRING | Opinión textual sobre Big Data |

---

# Antes de comenzar

## Si Beeline continúa abierto

Si todavía aparece un prompt similar a:

```text
0: jdbc:hive2://localhost:10000>
```

no es necesario hacer nada.

Puedes comenzar directamente con los ejercicios.

---

## Si cerraste Beeline pero el contenedor sigue activo

Abrir una terminal y ejecutar:

```bash
sudo docker exec -it myhiveserver beeline -u 'jdbc:hive2://localhost:10000/'
```

Cuando aparezca:

```text
0: jdbc:hive2://localhost:10000>
```

ya puedes volver a ejecutar consultas HiveQL.

---

## Si el contenedor está detenido

Comprobar su estado:

```bash
sudo docker ps -a
```

Si `myhiveserver` aparece como `Exited`, iniciarlo:

```bash
sudo docker start myhiveserver
```

Después conectarse nuevamente con Beeline:

```bash
sudo docker exec -it myhiveserver beeline -u 'jdbc:hive2://localhost:10000/'
```

> Si Hive acaba de iniciarse, puede tardar unos segundos en aceptar conexiones.

No es necesario volver a crear el contenedor ni volver a cargar los datos.

Si aparece algún error diferente, consultar:

[troubleshooting_hive.md](../troubleshooting_hive.md)


---

# Verificación inicial

Antes de comenzar, comprobar que la tabla sigue disponible:

```sql
SHOW TABLES;
```

Y visualizar algunos registros:

```sql
SELECT *
FROM opiniones
LIMIT 5;
```

Si aparecen datos correctamente, comenzar el ejercicio.

---

# Ejercicio 1 — ¿Cuántos países diferentes aparecen?

Determinar cuántos **países distintos** existen en la tabla.

El resultado debe devolver un único valor.

### Pista

Pensar cómo evitar contar varias veces el mismo país.

---

# Ejercicio 2 — Participación por sexo y país

Mostrar cuántas personas de cada sexo aparecen en cada país.

El resultado debe incluir:

- país;
- sexo;
- cantidad de registros.

Ordenar los resultados para que las combinaciones con mayor cantidad aparezcan primero.

### Pregunta

¿Qué combinación de país y sexo tiene mayor número de registros?

---

# Ejercicio 3 — Crear una clasificación por edad

Crear una nueva columna llamada `categoria_edad` que clasifique a cada persona según su edad:

- `Joven` → menores de 30 años;
- `Adulto` → entre 30 y 49 años;
- `Adulto 50+` → 50 años o más.

La consulta debe mostrar:

- `id`;
- `edad`;
- `categoria_edad`.

---

# Ejercicio 4 — Buscar palabras dentro de las opiniones

Mostrar los registros cuya opinión contenga la palabra:

```text
datos
```

El resultado debe mostrar:

- `id`;
- `pais_donde_vive`;
- `opinion_big_data`.

### Pista

Pensar qué operador SQL permite buscar texto dentro de una cadena.

---

# Ejercicio 5 — Analizar la longitud de las opiniones

Identificar las opiniones con mayor cantidad de caracteres.

Mostrar:

- `id`;
- `pais_donde_vive`;
- `opinion_big_data`;
- longitud del texto.

Ordenar el resultado de la opinión más larga a la más corta y mostrar únicamente las **5 primeras**.

### Pregunta

¿Cuál es la opinión más larga del conjunto de datos?

---

# Ejercicio 6 — Comparar edades por sexo

Calcular para cada valor de `sexo`:

- edad mínima;
- edad máxima;
- edad promedio;
- número de personas.

El resultado debe mostrar una fila por cada grupo.

### Pregunta

¿Existen diferencias entre los grupos?

---

# Ejercicio 7 — Crear una tabla derivada

Crear una nueva tabla llamada:

```text
opiniones_jovenes
```

que contenga únicamente las personas menores de 30 años.

La nueva tabla debe conservar las columnas:

- `id`;
- `edad`;
- `sexo`;
- `pais_donde_vive`;
- `opinion_big_data`.

Después comprobar:

1. que la tabla se ha creado;
2. cuántos registros contiene;
3. sus primeros 10 registros.

---

# Ejercicio 8 — Consulta libre

Crear una consulta propia utilizando al menos **tres** de los siguientes elementos:

- `WHERE`;
- `GROUP BY`;
- `ORDER BY`;
- `COUNT`;
- `AVG`;
- `DISTINCT`;
- `LIKE`;
- `LIMIT`.

La consulta debe responder a una pregunta concreta sobre los datos.

Antes de escribir el código, indicar:

**¿Qué quiero averiguar?**

Después ejecutar la consulta y explicar brevemente el resultado obtenido.

---

# Al finalizar

Con estos ejercicios se habrá practicado:

- selección de datos;
- búsqueda de valores distintos;
- filtros;
- búsquedas sobre texto;
- agrupaciones;
- agregaciones;
- ordenamientos;
- creación de categorías;
- creación de nuevas tablas a partir de consultas.

Para salir de Beeline:

```text
Ctrl + D
```