# TechnicalTest-CoolebraSpA

El presente repositorio contiene el desarrollo de la prueba técnica para postular a la oferta de trabajo como practicante Full-Stack en Coolebra SpA.

A continuación se detallan los archivos y carpetas que componen la solución de la prueba técnica:

-   `main.ipynb`: Este archivo contiene el desarrollo de las pregunta, 1,2 y 3 (a) de la prueba técnica. Tiene los resultados ejecutados para revisar el funcionamiento del código. Eso se hizo a fin de facilitar la revisión del código.
-   `/python-version`: Esta carpeta contiene el desarrollo de las preguntas 1 y 3 (a) de la prueba técnica en archivos .py. A continuación se detalla el contenido de la carpeta:
    -   `create_data_function.py`: Este archivo contiene la función que crea los datos para la pregunta 1 y 3.
    -   `create_query_function.py`: Este archivo contiene la consulta solicitada en la pregunta 2.
    -   `groupby_function.py`: Este archivo contiene la función que agrupa los datos para la pregunta 3 (a).
    -   `main.py`: Este archivo ejecuta las funciones de los archivos anteriores y muestra los resultados en consola.
-   `/coolebra-app`: Esta carpeta contiene la aplicación con React que fue solicitada para la pregunta 3 (b).

## Consideraciones

-   Para la pregunta 1 se crea una base de datos usando la librería sqlite3 de Python. Se crean las distintas tablas detalladas en la imagen del enunciado de la prueba técnica.

-   Para la aplicación en React se usa el arreglo de diccionario generado en la pregunta 3 (a), se guarda en `src/data/productsData.js`.

-   A fin de facilitar la revisión del funcionamiento de la app cuando se limpia por completo el input de búsqueda, se muestra en consola el arreglo de diccionario completo, es decir, sin filtrar.

-   Para la creación de la aplicación en React se usó el comando `npx create-react-app coolebra-app`, para ejecutar la aplicación se debe usar el comando `npm start` en la carpeta `/coolebra-app`. En caso de ser necesario también se debe ejecutar el comando `npm install` para instalar las dependencias necesarias.

## Supuestos

-   Para la tabla de Prices se asumio que "active" sería un booleano que indica si el precio está activo o no. En caso de ser 1 el precio está activo, en caso de ser 0 el precio no está activo.

-   Para la consulta de la pregunta 1 se asumió que el menor precio tiene más importancia que la fecha más reciente al momento de obtener el último menor precio activo.
