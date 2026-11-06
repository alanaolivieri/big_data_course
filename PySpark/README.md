# PySpark

Material del curso de Big Data de Eurecat IT Academy. Empezamos con Python y pandas, pasamos al procesamiento con Spark y aplicamos lo aprendido a modelos, visualización y análisis de texto.

## Antes de empezar

- Abre la [guía de preparación del entorno](00_environment_python.md) para configurar el teclado de la máquina virtual, elegir entre Colab, Jupyter Notebook y VS Code, y comprobar que Python funciona.
- Para el cuaderno `00` necesitarás pandas. Después, sigue la [guía de preparación del entorno de PySpark](01_environment_pyspark.md) para instalar y comprobar Java y PySpark antes del cuaderno `01`.
- Ejecuta las celdas de cada notebook de arriba abajo. Antes de avanzar, cierra la sesión de Spark si el cuaderno incluye un paso para hacerlo.

## Orden de ejecución

| Paso | Archivo | Qué haremos |
| --- | --- | --- |
| 00 | [Primeros pasos con Python](notebooks/00_intro_python.ipynb) | `print()`, tipos, operaciones, conversiones, listas, tuplas, diccionarios y `for`. Introduce DataFrames con pandas e incluye ejercicios de inspección, concatenación, duplicados y resúmenes por grupos. |
| Entre 00 y 01 | [Preparación del entorno de PySpark](01_environment_pyspark.md) | Comprueba Java, instala PySpark en el kernel y verifica que Spark puede ejecutar un cálculo. |
| 01 | [Introducción a PySpark](notebooks/01_intro_pyspark.ipynb) | Inicia Spark y sigue un ejemplo guiado con pedidos de mercado para practicar RDD, filtros, acciones y caché. Termina con un ejercicio breve de reservas de turismo. |
| 02 | [Ejercicio de RDD](notebooks/02_rdd_exercise.ipynb) | Crea un RDD, muestra sus datos, aplica transformaciones y filtros y ejecuta acciones. |
| 03 | [DataFrames de Spark](notebooks/03_spark_dataframes.ipynb) | Lee el CSV de accidentes de Barcelona con Spark, selecciona, filtra y agrupa registros. Con un ejemplo de pedidos, une tablas y calcula importes. |
| 04 | [Ejercicios de DataFrames](notebooks/04_df_exercise.ipynb) | Explora los nacimientos de Barcelona en 2024 con ejercicios de inspección, filtrado, ordenación y estadísticas descriptivas. |
| 05 | [CSV con Python y PySpark](notebooks/05_csv_python_vs_pyspark.ipynb) | Procesa el mismo CSV con Python y PySpark y compara resultados y tiempos. |
| 06 | [Parquet con Python y PySpark](notebooks/06_parquet_python_vs_pyspark.ipynb) | Observa el formato, compara tamaños y procesa el mismo Parquet con PyArrow y PySpark. |
| 07 | [Spark y HDFS](notebooks/07_spark_hdfs.ipynb) | Lee pedidos de HDFS, agrupa por zona y guarda el resumen en HDFS. |
| 08 | [Preparación de datos para el análisis](notebooks/08_data_preparation_and_analysis.ipynb) | Comprueba calidad, guarda la tabla en Parquet y practica estadísticas descriptivas e interpretación con los nacimientos de Barcelona. |
| 09 | [Visualización de datos](notebooks/09_data_visualization.ipynb) | Prepara datos del censo y construye gráficos de frecuencia, histogramas, diagramas de caja y una pirámide poblacional, entre otros. |
| 10 | [Análisis de texto](notebooks/10_spark_text_analysis.ipynb) | Limpia y tokeniza resúmenes científicos, elimina palabras vacías, representa los textos con TF-IDF. Deja la agrupación de documentos para después del cuaderno 13. |

## Modelado para más adelante

Este bloque se trabaja después de completar los pasos 05 a 10.

| Paso | Archivo | Contenido |
| --- | --- | --- |
| 11 | [Regresión lineal con el censo](notebooks/11_census_linear_regression.ipynb) | Explora y limpia datos del censo, entrena una regresión lineal e interpreta la evaluación y los coeficientes. Compara modelos con y sin `RobustScaler`. |
| 12 | [Regresión logística](notebooks/12_census_logistic_regression.ipynb) | Explora y prepara datos del censo para entrenar y evaluar un modelo supervisado de clasificación. |
| 13 | [Segmentación con K-Means](notebooks/13_census_kmeans.ipynb) | Prepara los datos del censo, agrupa observaciones y evalúa la calidad de los grupos. |

## Soluciones y versiones alternativas

Consulta las soluciones después de intentar los ejercicios. Las versiones alternativas de regresión pertenecen al bloque complementario de modelado.

- [Solución del ejercicio de RDD](notebooks/02_rdd_solution.ipynb). Implementación para comparar después de resolver el ejercicio.
- [Soluciones de DataFrames](notebooks/04_df_solution.ipynb). Resoluciones de las actividades y una nota sobre la actividad 12.
- [Versión alternativa de regresión lineal](notebooks/11_census_linear_regression_original.ipynb). Otra versión del práctico completo con exploración, limpieza y comparación de modelos.
- [Variante centrada en la regresión](notebooks/11_census_linear_regression_modeling.ipynb). Tras la carga del censo, pasa al entrenamiento, la evaluación y la comparación de los modelos.

## Datos

- El paso `03` usa el [CSV de accidentes de Barcelona](data/2023_accidents_causa_conductor_gu_bcn_.csv), incluido en el repositorio.
- El ejercicio de DataFrames `04`, su solución y el módulo de preparación `08` usan el [CSV de nacimientos de Barcelona de 2024](data/2024_pad_nai_mdbas.csv), incluido en el repositorio.
- Los cuadernos de regresión, segmentación y visualización usan `personas_ext_26_02.csv`.
- El cuaderno de análisis de texto lee `metadata.csv`.

Para los CSV que no están incluidos, coloca el archivo correspondiente en el directorio de trabajo del kernel o ajusta la ruta de la celda.
