# Visualizador de datos médicos

In this project, you will visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. Los valores del conjunto de datos (dataset) se recogieron durante los exámenes médicos.

## Descripción de datos
Las filas del conjunto de datos representan a los pacientes y las columnas representan información como medidas corporales, resultados de varios análisis de sangre y opciones de estilo de vida. Utilizarás el conjunto de datos para explorar la relación entre enfermedades cardiacas, medidas del cuerpo, indicadores sanguíneos y opciones de estilo de vida.

Nombre del archivo: medical_examination.csv

<table>
<thead>
<tr>
<th align="center">Feature</th>
<th align="center">Variable Type</th>
<th align="center">Variable</th>
<th align="center">Value Type</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">Age</td>
<td align="center">Objective Feature</td>
<td align="center"><code>age</code></td>
<td align="center">int (days)</td>
</tr>
<tr>
<td align="center">Height</td>
<td align="center">Objective Feature</td>
<td align="center"><code>height</code></td>
<td align="center">int (cm)</td>
</tr>
<tr>
<td align="center">Weight</td>
<td align="center">Objective Feature</td>
<td align="center"><code>weight</code></td>
<td align="center">float (kg)</td>
</tr>
<tr>
<td align="center">Gender</td>
<td align="center">Objective Feature</td>
<td align="center"><code>gender</code></td>
<td align="center">categorical code</td>
</tr>
<tr>
<td align="center">Systolic blood pressure</td>
<td align="center">Examination Feature</td>
<td align="center"><code>ap_hi</code></td>
<td align="center">int</td>
</tr>
<tr>
<td align="center">Diastolic blood pressure</td>
<td align="center">Examination Feature</td>
<td align="center"><code>ap_lo</code></td>
<td align="center">int</td>
</tr>
<tr>
<td align="center">Cholesterol</td>
<td align="center">Examination Feature</td>
<td align="center"><code>cholesterol</code></td>
<td align="center">1: normal, 2: above normal, 3: well above normal</td>
</tr>
<tr>
<td align="center">Glucose</td>
<td align="center">Examination Feature</td>
<td align="center"><code>gluc</code></td>
<td align="center">1: normal, 2: above normal, 3: well above normal</td>
</tr>
<tr>
<td align="center">Smoking</td>
<td align="center">Subjective Feature</td>
<td align="center"><code>smoke</code></td>
<td align="center">binary</td>
</tr>
<tr>
<td align="center">Alcohol intake</td>
<td align="center">Subjective Feature</td>
<td align="center"><code>alco</code></td>
<td align="center">binary</td>
</tr>
<tr>
<td align="center">Physical activity</td>
<td align="center">Subjective Feature</td>
<td align="center"><code>active</code></td>
<td align="center">binary</td>
</tr>
<tr>
<td align="center">Presence or absence of cardiovascular disease</td>
<td align="center">Target Variable</td>
<td align="center"><code>cardio</code></td>
<td align="center">binary</td>
</tr>
</tbody>
</table>

## Tareas
<p>Create a chart similar to <code>examples/Figure_1.png</code>, where we show the counts of good and bad outcomes for the <code>cholesterol</code>, <code>gluc</code>, <code>alco</code>, <code>active</code>, and <code>smoke</code> variables for patients with <code>cardio=1</code> and <code>cardio=0</code> in different panels.</p>

<p>Use the data to complete the following tasks in <code>medical_data_visualizer.py</code>:</p>

<ul>
<li>Add an <code>overweight</code> column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is &gt; 25 then the person is overweight. Use the value <code>0</code> for NOT overweight and the value <code>1</code> for overweight.</li>
<li>Normalize the data by making <code>0</code> always good and <code>1</code> always bad. If the value of <code>cholesterol</code> or <code>gluc</code> is <code>1</code>, make the value <code>0</code>. If the value is more than <code>1</code>, make the value <code>1</code>.</li>
<li>Convert the data into long format and create a chart that shows the value counts of the categorical features using <code>seaborn</code>'s <code>catplot()</code>. The dataset should be split by <code>Cardio</code> so there is one chart for each <code>cardio</code> value. The chart should look like <code>examples/Figure_1.png</code>.</li>
<li>Clean the data. Filter out the following patient segments that represent incorrect data:
<ul>
<li>diastolic pressure is higher than systolic (Keep the correct data with <code>(df['ap_lo'] &lt;= df['ap_hi'])</code>)</li>
<li>height is less than the 2.5th percentile (Keep the correct data with <code>(df['height'] &gt;= df['height'].quantile(0.025))</code>)</li>
<li>height is more than the 97.5th percentile</li>
<li>weight is less than the 2.5th percentile</li>
<li>weight is more than the 97.5th percentile</li>
</ul>
</li>
<li>Create a correlation matrix using the dataset. Plot the correlation matrix using <code>seaborn</code>'s <code>heatmap()</code>. Mask the upper triangle. The chart should look like <code>examples/Figure_2.png</code>.</li>
</ul>

<p>Any time a variable is set to <code>None</code>, make sure to set it to the correct code.</p>

<p>Unit tests are written for you under <code>test_module.py</code>.</p>

## Instrucctions
<p>By each number in the <code>medical_data_visualizer.py</code> file, add the code from the associated instruction number below.</p>

<ol>
<li>Import the data from <code>medical_examination.csv</code> and assign it to the <code>df</code> variable</li>
<li>Create the <code>overweight</code> column in the <code>df</code> variable</li>
<li>Normalize data by making <code>0</code> always good and <code>1</code> always bad. If the value of <code>cholesterol</code> or <code>gluc</code> is 1, set the value to <code>0</code>. If the value is more than <code>1</code>, set the value to <code>1</code>.</li>
<li>Draw the Categorical Plot in the <code>draw_cat_plot</code> function</li>
<li>Create a DataFrame for the cat plot using <code>pd.melt</code> with values from <code>cholesterol</code>, <code>gluc</code>, <code>smoke</code>, <code>alco</code>, <code>active</code>, and <code>overweight</code> in the <code>df_cat</code> variable.</li>
<li>Group and reformat the data in <code>df_cat</code> to split it by <code>cardio</code>. Show the counts of each feature. You will have to rename one of the columns for the <code>catplot</code> to work correctly.</li>
<li>Convert the data into <code>long</code> format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import : <code>sns.catplot()</code></li>
<li>Get the figure for the output and store it in the <code>fig</code> variable</li>
<li>Do not modify the next two lines</li>
<li>Draw the Heat Map in the <code>draw_heat_map</code> function</li>
<li>Clean the data in the <code>df_heat</code> variable by filtering out the following patient segments that represent incorrect data:
<ul>
<li>height is less than the 2.5th percentile (Keep the correct data with <code>(df['height'] &gt;= df['height'].quantile(0.025))</code>)</li>
<li>height is more than the 97.5th percentile</li>
<li>weight is less than the 2.5th percentile</li>
<li>weight is more than the 97.5th percentile</li>
</ul>
</li>
<li>Calculate the correlation matrix and store it in the <code>corr</code> variable</li>
<li>Generate a mask for the upper triangle and store it in the <code>mask</code> variable</li>
<li>Set up the <code>matplotlib</code> figure</li>
<li>Plot the correlation matrix using the method provided by the <code>seaborn</code> library import: <code>sns.heatmap()</code></li>
<li>Do not modify the next two lines</li>
</ol>

## Desarrollo
<p>Write your code in <code>medical_data_visualizer.py</code>. For development, you can use <code>main.py</code> to test your code.</p>

## Pruebas
<p>The unit tests for this project are in <code>test_module.py</code>. Hemos importado las pruebas de <code>test_module.py</code> a <code>main.py</code> para tu conveniencia.</p>

## Solución
[Solution Link](https://github.com/ElJoamy/freeCodeCampPython/tree/main/Visualizador%20de%20datos%20m%C3%A9dicos)