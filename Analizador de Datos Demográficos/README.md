# Demographic Data Analyzer
**Check the [`README.md`](../README.md) for necessary information about this project.**

En este desafío debe analizar los datos demográficos usando Pandas. Se le da un conjunto de datos demográficos que fueron extraidos de la base de datos del censo de 1994. Aquí hay un ejemplo de cómo se debería ver:

|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |

Debes usar Pandas para responder a las siguientes preguntas:

¿Cuántas personas de cada raza están representadas en este set de datos? This should be a Pandas series with race names as the index labels. (columna race)
¿Cuál es la edad promedio de los hombres?
¿Cuál es el porcentaje de personas que tienen un grado de licenciatura (Bachelor's degree)?
¿Qué porcentaje de personas con una educación avanzada (Bachelors, Masters o Doctorate) ganan más de 50k?
¿Qué porcentaje de personas sin una educación avanzada generan más de 50k?
¿Cuál es el mínimo número de horas que una persona trabaja por semana?
¿Qué porcentaje de personas que trabajan el mínimo de horas por semana tiene un salario de más de 50k?
¿Qué país tiene el porcentaje más alto de personas que ganan >50k y cuál es ese porcentaje?
Identifica la ocupación más popular de aquellos que ganan >50k en India.
Use the starter code in the file demographic_data_analyzer.py. Update the code so all variables set to None are set to the appropriate calculation or code. Redondea todos los decimales a la décima más cercana.

## Desarrollo
Write your code in demographic_data_analyzer.py. For development, you can use main.py to test your code.

## Pruebas
The unit tests for this project are in test_module.py. Importamos las pruebas de test_module.py a main.py para tu conveniencia.

## Envío
Copia el enlace de tu proyecto y envíalo a freeCodeCamp.

## Fuente de datos
Dua, D. y Graff, C. (2019). UCI Machine Learning Repositorio. Irvine, CA: University of California, School of Information and Computer Science.

## Solución
[Solucion Link](https://github.com/ElJoamy/freeCodeCampPython/tree/main/Analizador%20de%20Datos%20Demogr%C3%A1ficos)