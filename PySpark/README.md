# PySpark

Material del curso de Big Data de Eurecat IT Academy. Empezamos con Python y pandas, pasamos al procesamiento con Spark y aplicamos lo aprendido a modelos, visualización y análisis de texto.

## Antes de empezar

- Abre la [guía de preparación del entorno](00_environment_python.md) para configurar el teclado de la máquina virtual, elegir entre Colab, Jupyter Notebook y VS Code, y comprobar que Python funciona.
- Para el cuaderno `00` necesitarás pandas. Después, sigue la [guía de preparación del entorno de PySpark](01_environment_pyspark.md) para instalar y comprobar Java y PySpark antes del cuaderno `01`.
- Ejecuta las celdas de cada notebook de arriba abajo. Antes de avanzar, cierra la sesión de Spark si el cuaderno incluye un paso para hacerlo.

## Ruta principal hasta visualización

Los pasos 00 a 10 cubren Python, Spark, formatos de datos, preparación, análisis exploratorio, estadística y visualización. El aprendizaje automático se trabaja después.

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
| 08 | [EDA y estadística con PySpark](notebooks/08_data_preparation_and_analysis.ipynb) | Prepara la encuesta de empleados con Spark y calcula resúmenes, Welch, chi-cuadrado, Pearson y Spearman. |
| 09 | [EDA y estadística con pandas](notebooks/09_eda_y_estadistica_bigdata.ipynb) | Repite los pasos del 08 sobre la misma encuesta para comparar la limpieza, los resúmenes y los resultados estadísticos. |
| 10 | [Visualización de datos](notebooks/10_data_visualization.ipynb) | Prepara datos del censo y construye gráficos de frecuencia, histogramas, diagramas de caja y una pirámide poblacional, entre otros. |

## Aprendizaje automático con PySpark

Los cuadernos 11 a 14 son independientes y contienen datos simulados. Para una clase corta, recorre el 11, el 12 y el 14. El 13 aplica K-Means a textos y se puede mostrar después del 14.
| Paso | Archivo | Contenido |
| --- | --- | --- |
| 11 | [Regresión lineal](notebooks/11_census_linear_regression.ipynb) | Predice un salario simulado, compara el error con una referencia e interpreta los coeficientes. |
| 12 | [Regresión logística](notebooks/12_census_logistic_regression.ipynb) | Predice si una persona termina un curso. Lee probabilidades, exactitud y matriz de confusión. |
| 13 | [Análisis de texto](notebooks/13_spark_text_analysis.ipynb) | Convierte titulares en español a TF-IDF, forma grupos y revisa sus términos frecuentes. |
| 14 | [Segmentación con K-Means](notebooks/14_census_kmeans.ipynb) | Escala las variables, compara dos valores de k y describe los perfiles en las unidades originales. |

## Módulo final · Visualización y valor

- [15 · Día 1: Visualizar siniestros](notebooks/15_visualizacion_siniestros_dia_1.ipynb). Seaborn, mapa geográfico con Folium y ejercicio final.
- [16 · Día 2: Panel con subplots](notebooks/16_panel_siniestros_dia_2.ipynb). Combina el indicador y tres gráficos. Exporta la tabla común para los cuadernos 17 y 18.
- [17 · Día 2: Plotly, Streamlit y Dash](notebooks/17_panel_streamlit_y_dash_dia_2.ipynb). Tres formas de mostrar el mismo panel sobre el CSV exportado.
- [18 · Día 3: Power BI y valor](notebooks/18_power_bi_y_valor_dia_3.ipynb). Reconstruye el panel en BI y defiende una decisión. Incluye una ruta equivalente en Looker Studio.

## Soluciones y versiones alternativas

Consulta las soluciones después de intentar los ejercicios. Las dos ampliaciones del 11 son opcionales.

- [Solución del ejercicio de RDD](notebooks/02_rdd_solution.ipynb). Implementación para comparar después de resolver el ejercicio.
- [Soluciones de DataFrames](notebooks/04_df_solution.ipynb). Resoluciones de las actividades y una nota sobre la actividad 12.
- [Diagnóstico de errores de la regresión](notebooks/11_census_linear_regression_original.ipynb). Revisa los residuos y compara el error por jornada.
- [Escalado robusto en regresión](notebooks/11_census_linear_regression_modeling.ipynb). Compara el MAE del mismo modelo con y sin escalado.

## Datos

- El paso `03` usa el [CSV de accidentes de Barcelona](data/2023_accidents_causa_conductor_gu_bcn_.csv), incluido en el repositorio.
- El ejercicio de DataFrames `04` y su solución usan el [CSV de nacimientos de Barcelona de 2024](data/2024_pad_nai_mdbas.csv), incluido en el repositorio.
- Los pasos `08` y `09` usan [empleados_curso.csv](data/empleados_curso.csv) y [ciudades_contexto.csv](data/ciudades_contexto.csv).
- El cuaderno de visualización usa `personas_ext_26_02.csv`.
- Los cuadernos 11, 12 y 14 generan la misma encuesta simulada. El 13 incluye sus propios titulares ficticios.

Para los CSV que no están incluidos, coloca el archivo correspondiente en el directorio de trabajo del kernel o ajusta la ruta de la celda.
