# pina-tech

# Diseño e implementación de un sistema de aprendizaje automático para la predicción de la Capacidad de Intercambio Catiónico CIC

La tecnología relacionada con el análisis de datos y la inteligencia artificial en el sector agrícola colombiana es desconocida o poco utilizada, especialmente en entornos de pequeña y mediana producción. No obstante, la integración de herramientas para el análisis del suelo es de gran importancia para la optimización del cultivo. El uso de técnicas de análisis de datos e inteligencia artificial es una alternativa para contribuir a crear modelos de aprendizaje autónomo que facilitan la predicción de las condiciones del suelo, en relación con el fertilizante y el tipo de cultivo a emplear. Diseñar un sistema de aprendizaje automático para la estimación del cultivo y los fertilizantes más adecuados para un determinado suelo, a partir del análisis de los datos suministrados por la base de datos Resultados de Análisis de Laboratorio Suelos en Colombia del año 2020 de AGROSAVIA. La metodología utilizada en este proyecto se puede dividir en las siguientes etapas: Identificación y selección detallada de la información, Preprocesamiento de datos, Diseño e implementación del sistema de aprendizaje automático siguiendo una evaluación y comparación de resultados en condiciones de laboratorio. Cómo resultado del diseño de este algoritmo se obtuvo porcentajes de precisión cuadrático por encima del 95% de precisión en la estimación de la variable objetivo, utilizando los algoritmos de regresión RNA, KNN Regressor, Decision Tree Regressor y Random Forest Regressor, los cuales son considerados como uno de los mejores modelos para este problema.

Palabras clave: Agricultura de precisión, aprendizaje automático, análisis de suelos, ciencia de datos



<p align="center">
<img src="" />
</p>
En el sector de la producción agrícola colombiana, se identifica que el uso de tecnologías relacionadas con el análisis de datos y la inteligencia artificial, son desconocidos o poco implementados, especialmente en entornos de pequeña y mediana producción. El no uso de este tipo de algoritmos, afecta la toma de decisiones que sobre el manejo de este puede llevarse a cabo, verbigracia, cuántos y qué cantidad de fertilizante necesita una plantación específica.

# [Dataset]()
Resultados de Análisis de Laboratorio Suelos en Colombia. (2020). Resultados del Servicio de Análisis de Suelos que el Laboratorio de Química y Física de Suelos de AGROSAVIA.
* https://www.datos.gov.co/Agricultura-y-Desarrollo-Rural/Resultados-de-An-lisis-de-Laboratorio-Suelos-en-Co/ch4u-f3i5 


### [Attributes information:]()

* **pH agua:suelo 2.5:1.0** - xxxx
* **Materia orgánica (MO) %** - xxxx
* **Fósforo (P) Bray II mg/kg** - xxxx
* **Azufre (S) Fosfato monocalcico mg/kg** -  xxx
* **Calcio (Ca) intercambiable cmol(+)/kg** - xxxx
* **Magnesio (Mg) intercambiable cmol(+)/kg** - xxxx
* **Acidez (Al+H) KCL cmol(+)/kg** - xxxxx
* **Aluminio (Al) intercambiable cmol(+)/kg** - xxxxx
* **Potasio (K) intercambiable cmol(+)/kg** - xxxxx
* **Sodio (Na) intercambiable cmol(+)/kg** - xxxxx
* **Conductividad electrica (CE) relacion 2.5:1.0 dS/m** - xxxxx
* **Hierro (Fe) disponible olsen mg/kg** - xxxxx
* **Cobre (Cu) disponible mg/kg** - xxxxx
* **Manganeso (Mn) disponible Olsen mg/kg** - xxxxx
* **Zinc (Zn) disponible Olsen mg/kg** - xxxxx
* **Boro (B) disponible mg/kg** - xxxxx

### [Experiment Results:]()
* **Data Analysis**
    * All columns contain outliers except for N.
 * **Performance Evaluation**
    * Splitting the dataset by 80 % for training set and 20 % validation set.
 * **Training and Validation**
    * GausianNB gets a higher accuracy score than other classification models.
    * GaussianNB ( 99 % accuracy score )
 * **Performance Results**
    * Training Score: 99.5%
    * Validation Score: 99.3%

 
# Demo
Live Demo: https://agronomia.onrender.com/

![]()

# References
Azuela, JHS y Cortés, FR (2021). Inteligencia artificial aplicada a Robótica y Automatización (1ª ed.). Marcombo. Obtenido de https://www.perlego.com/book/2703191/inteligencia-artificial-aplicada-a-robtica-y-automatizacin-pdf   (Trabajo original publicado en 2021)

Resultados de Análisis de Laboratorio Suelos en Colombia. (2020). Resultados del Servicio de Análisis de Suelos que el Laboratorio de Química y Física de Suelos de AGROSAVIA. Recuperado de la base de datos de Datos abiertos del Gobierno de Colombia - Ministerio de Agricultura y Desarrollo rural. https://www.datos.gov.co/Agricultura-y-Desarrollo-Rural/Resultados-de-An-lisis-de-Laboratorio-Suelos-en-Co/ch4u-f3i5 

Bonilla Segovia, J. S., Dávila Rojas, F. A., & Villa Quishpe, M. W. (2021). Estudio del uso de técnicas de inteligencia artificial aplicadas para análisis de suelos para el sector agrícola. RECIMUNDO, 5(1), 4-19. 
https://doi.org/10.26820/recimundo/5.(1).enero.2021.4-19 

Escobar Iza, R. D., Maliza Bedon, D. S., & Cadena Moreano, J. A. (2021). Análisis de suelos utilizando redes neuronales en las florícolas de Rosas del Sector Norte de la Provincia de Cotopaxi. RECIMUNDO, 5(2), 316-330. https://doi.org/10.26820/recimundo/5.(2).abril.2021.316-330  

Galarza Rodríguez, J. (2019.). Aplicación web-móvil para el control de producción agrícola de una red de agricultores. Universidad del Valle.
http://hdl.handle.net/10893/15698  

Diaz-Gonzalez, F. A., Vuelvas, J., Correa, C. A., Vallejo, V. E. & Patino, D. (2021) Machine learning and remote sensing techniques applied to estimate soil indicators. Ecological Indicators. https://doi.org/10.1016/j.ecolind.2021.108517 


LEAL PABÓN, J, Rodriguez Tenjo, J y Gallardo Pérez, O. (2018-07-01.). Fertilcacao: software para la automatización del proceso de fertilización de los suelos gremio cacao cultores. Mundo FESC. https://repositorio.ufps.edu.co/handle/ufps/481
