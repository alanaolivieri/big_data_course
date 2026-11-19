# PySpark

Material del curso de Big Data de Eurecat IT Academy. Empezamos con Python y pandas, pasamos al procesamiento con Spark y aplicamos lo aprendido a modelos, visualización y análisis de texto.

## Antes de empezar

- Abre la [guía de preparación del entorno](00_environment_python.md) para configurar el teclado de la máquina virtual, elegir entre Colab, Jupyter Notebook y VS Code, y comprobar que Python funciona.
- Para el cuaderno `00` necesitarás pandas. Después, sigue la [guía de preparación del entorno de PySpark](01_environment_pyspark.md) para instalar y comprobar Java y PySpark antes del cuaderno `01`.
- Ejecuta las celdas de cada notebook de arriba abajo. Antes de avanzar, cierra la sesión de Spark si el cuaderno incluye un paso para hacerlo.

## Ruta principal hasta visualización

La ruta del 00 al 09 cubre Python, Spark, formatos de datos, preparación, análisis exploratorio, estadística y visualización. El aprendizaje automático se trabaja después.

| Paso | Archivo | Qué haremos |
| --- | --- | --- |
| 00 | [Primeros pasos con Python](notebooks/00_intro_python.ipynb) | `print()`, tipos, operaciones, conversiones, listas, tuplas, diccionarios y `for`. Introduce DataFrames con pandas e incluye ejercicios de inspección, concatenación, duplicados y resúmenes por grupos. |
| Entre 00 y 01 | [Preparación del entorno de PySpark](01_environment_pyspark.md) | Comprueba Java, instala PySpark en el kernel y verifica que Spark puede ejecutar un cálculo. |
| 01 | [Introducción a PySpark](notebooks/01_intro_pyspark.ipynb) | Inicia Spark y sigue un ejemplo guiado con pedidos de mercado para practicar RDD, filtros, acciones y caché. Termina con un ejercicio breve de reservas de turismo. |
| 02 | [Ejercicio de RDD](notebooks/02_rdd_exercise.ipynb) | Crea un RDD, muestra sus datos, aplica transformaciones y filtros y ejecuta acciones. |
| 03 | [DataFrames de Spark](notebooks/03_spark_dataframes.ipynb) | Lee el CSV de accidentes de Barcelona con Spark, selecciona, filtra y agrupa registros. Con un ejemplo de pedidos, une tablas y calcula importes. |
| 04 | [Ejercicios de DataFrames](notebooks/04_df_exercise.ipynb) | Explora los nacimientos de Barcelona en 2024 con ejercicios de inspección, filtrado, ordenación y estadísticas descriptivas. |
| 05 | [CSV vs. Parquet con PySpark](notebooks/05_csv_vs_parquet_pyspark.ipynb) | Guarda los mismos pedidos en ambos formatos y compara tamaños, esquemas y resultados. |
| 06 | [Parquet con pandas y PySpark](notebooks/06_parquet_pandas_vs_pyspark.ipynb) | Lee dos columnas del Parquet del 05 con pandas y PySpark, agrupa por zona y compara el resultado y la ejecución. |
| 07 | [Spark y HDFS](notebooks/07_spark_hdfs.ipynb) | Lee pedidos de HDFS, agrupa por zona y guarda el resumen en HDFS. |
| 08 | [EDA y estadística con pandas](notebooks/08_data_preparation_and_analysis.ipynb) | Revisa la encuesta de empleados y añade el contexto de las ciudades. Explora la normalidad con Shapiro–Wilk, la correlación con Pearson y Spearman y la independencia con chi-cuadrado. |
| 09 | [Visualización de datos](notebooks/09_data_visualization.ipynb) | Prepara datos del censo y construye gráficos de frecuencia, histogramas, diagramas de caja y una pirámide poblacional, entre otros. |

## Aprendizaje automático con PySpark

Los cuadernos 10 a 13 son independientes y contienen datos simulados. Para una clase corta, recorre el 10, el 11 y el 13. El 12 aplica K-Means a textos y se puede mostrar después del 13.
| Paso | Archivo | Contenido |
| --- | --- | --- |
| 10 | [Regresión lineal](notebooks/10_census_linear_regression.ipynb) | Predice un salario simulado, compara el error con una referencia e interpreta los coeficientes. Incluye diagnóstico de residuos y escalado robusto como ampliaciones. |
| 11 | [Regresión logística](notebooks/11_census_logistic_regression.ipynb) | Predice si una persona termina un curso. Lee probabilidades, exactitud y matriz de confusión. |
| 12 | [Análisis de texto](notebooks/12_spark_text_analysis.ipynb) | Convierte titulares en español a TF-IDF, forma grupos y revisa sus términos frecuentes. |
| 13 | [Segmentación con K-Means](notebooks/13_census_kmeans.ipynb) | Escala las variables, compara dos valores de k y describe los perfiles en las unidades originales. |

## Módulo final · Visualización y valor

- [14 · Día 1: Visualizar siniestros](notebooks/14_visualizacion_siniestros_dia_1.ipynb). Seaborn, mapa geográfico con Folium y ejercicio final.
- [15 · Día 2: Panel con subplots](notebooks/15_panel_siniestros_dia_2.ipynb). Combina el indicador y tres gráficos. Exporta la tabla común para los cuadernos 16 y 17.
- [16 · Día 2: Plotly, Streamlit y Dash](notebooks/16_panel_streamlit_y_dash_dia_2.ipynb). Tres formas de mostrar el mismo panel sobre el CSV exportado.
- [17 · Día 3: Power BI y valor](notebooks/17_power_bi_y_valor_dia_3.ipynb). Reconstruye el panel en BI y defiende una decisión. Incluye una ruta equivalente en Looker Studio.

## Soluciones

Consulta las soluciones después de intentar los ejercicios.

- [Solución del ejercicio de RDD](notebooks/02_rdd_solution.ipynb). Implementación para comparar después de resolver el ejercicio.
- [Soluciones de DataFrames](notebooks/04_df_solution.ipynb). Resoluciones de las actividades y una nota sobre la actividad 12.

## Datos

- El paso `03` usa el [CSV de accidentes de Barcelona](data/2023_accidents_causa_conductor_gu_bcn_.csv), incluido en el repositorio.
- El ejercicio de DataFrames `04` y su solución usan el [CSV de nacimientos de Barcelona de 2024](data/2024_pad_nai_mdbas.csv), incluido en el repositorio.
- El paso `08` usa [empleados_curso.csv](data/empleados_curso.csv) y [ciudades_contexto.csv](data/ciudades_contexto.csv).
- El cuaderno de visualización usa `personas_ext_26_02.csv`.
- Los cuadernos 10, 11 y 13 generan la misma encuesta simulada. El 12 incluye sus propios titulares ficticios.

Para los CSV que no están incluidos, coloca el archivo correspondiente en el directorio de trabajo del kernel o ajusta la ruta de la celda.
