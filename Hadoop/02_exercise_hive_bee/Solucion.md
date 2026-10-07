# Soluciones — Ejercicio práctico Hive

## Ejercicio 1 — ¿Cuántos países diferentes aparecen?

Para contar países distintos utilizamos `COUNT(DISTINCT ...)`:

```sql
SELECT COUNT(DISTINCT pais_donde_vive) AS total_paises
FROM opiniones;
```

---

## Ejercicio 2 — Participación por sexo y país

Agrupamos por país y sexo y contamos cuántos registros hay en cada combinación:

```sql
SELECT
    pais_donde_vive,
    sexo,
    COUNT(*) AS cantidad
FROM opiniones
GROUP BY pais_donde_vive, sexo
ORDER BY cantidad DESC;
```

La primera fila del resultado corresponderá a la combinación de país y sexo con mayor número de registros.

---

## Ejercicio 3 — Crear una clasificación por edad

Crear una nueva columna llamada `categoria_edad` que clasifique a cada persona según su edad:

- `Joven` → menores de 30 años;
- `Adulto` → entre 30 y 49 años;
- `Adulto 50+` → 50 años o más.

La consulta debe mostrar:

- `id`;
- `edad`;
- `categoria_edad`.

```sql
SELECT
    id,
    edad,
    CASE
        WHEN edad < 30 THEN 'Joven'
        WHEN edad < 50 THEN 'Adulto'
        ELSE 'Adulto 50+'
    END AS categoria_edad
FROM opiniones;
```

La columna `categoria_edad` no existe originalmente en la tabla. Se genera en el resultado de la consulta mediante `CASE WHEN`.

---

## Ejercicio 4 — Buscar palabras dentro de las opiniones

Para buscar opiniones que contengan la palabra `datos` utilizamos `LIKE`:

```sql
SELECT
    id,
    pais_donde_vive,
    opinion_big_data
FROM opiniones
WHERE opinion_big_data LIKE '%datos%';
```

El símbolo `%` indica que puede existir cualquier texto antes o después de la palabra buscada.

---

## Ejercicio 5 — Analizar la longitud de las opiniones

Utilizamos `LENGTH()` para calcular la cantidad de caracteres de cada opinión:

```sql
SELECT
    id,
    pais_donde_vive,
    opinion_big_data,
    LENGTH(opinion_big_data) AS longitud
FROM opiniones
ORDER BY longitud DESC
LIMIT 5;
```

La primera fila corresponde a la opinión con mayor número de caracteres.

---

## Ejercicio 6 — Comparar edades por sexo

Agrupamos por `sexo` y utilizamos varias funciones de agregación:

```sql
SELECT
    sexo,
    MIN(edad) AS edad_minima,
    MAX(edad) AS edad_maxima,
    AVG(edad) AS edad_promedio,
    COUNT(*) AS cantidad_personas
FROM opiniones
GROUP BY sexo;
```

Este resultado permite comparar la distribución de edades entre los diferentes grupos.

---

## Ejercicio 7 — Crear una tabla derivada

Crear una nueva tabla que contenga únicamente personas menores de 30 años:

```sql
CREATE TABLE opiniones_jovenes AS
SELECT
    id,
    edad,
    sexo,
    pais_donde_vive,
    opinion_big_data
FROM opiniones
WHERE edad < 30;
```

### Comprobar que la tabla existe

```sql
SHOW TABLES;
```

Debería aparecer:

```text
opiniones_jovenes
```

### Contar cuántos registros contiene

```sql
SELECT COUNT(*) AS cantidad
FROM opiniones_jovenes;
```

### Visualizar los primeros 10 registros

```sql
SELECT *
FROM opiniones_jovenes
LIMIT 10;
```

---

## Ejercicio 8 — Consulta libre

En este ejercicio pueden existir muchas soluciones correctas.

### Ejemplo

**¿Qué quiero averiguar?**

Quiero saber qué países tienen más personas mayores de 30 años y cuál es su edad promedio.

```sql
SELECT
    pais_donde_vive,
    COUNT(*) AS cantidad_personas,
    AVG(edad) AS edad_promedio
FROM opiniones
WHERE edad > 30
GROUP BY pais_donde_vive
ORDER BY cantidad_personas DESC
LIMIT 5;
```

Esta consulta utiliza:

- `WHERE` para filtrar personas mayores de 30 años;
- `COUNT()` para contar registros;
- `AVG()` para calcular la edad promedio;
- `GROUP BY` para agrupar por país;
- `ORDER BY` para ordenar los resultados;
- `LIMIT` para mostrar únicamente los cinco primeros.

---

# Resumen de funciones utilizadas

| Elemento | Uso |
|---|---|
| `COUNT()` | Contar registros |
| `DISTINCT` | Evitar valores repetidos |
| `GROUP BY` | Agrupar registros |
| `ORDER BY` | Ordenar resultados |
| `CASE WHEN` | Crear categorías según condiciones |
| `LIKE` | Buscar patrones en texto |
| `LENGTH()` | Calcular la longitud de un texto |
| `MIN()` | Obtener el valor mínimo |
| `MAX()` | Obtener el valor máximo |
| `AVG()` | Calcular el promedio |
| `LIMIT` | Limitar el número de resultados |

Para salir de Beeline:

```text
Ctrl + D
```