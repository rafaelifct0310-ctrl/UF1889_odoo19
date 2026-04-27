# Ejercicio 1. Identificar modelos y relaciones
#### Tema: Academia online

### 1. Que aprender
- Identificar en modelo que contiene la entidad principal
- Identificar el modelo que contiene la actividad o interacción
- Entender como se relaionan ambos modelos

### Este razonamiento es la base de la práctica
- primero identificas los datos
- consultas con ORM
- después agregas, las muestras y los exportas

### 2. Análisis del caso
La academia quiere saber:

| cuántas tutorías ha recibido cada alumno

De esta frase salen dos preguntas:

¿Sobre quién queremos resumir la información?

Sobre el alumno

¿Qué evento o interacción queremos contar?

Las tutorias

Por lo tanto:

- academy.student = modelo principal
- academy.tutoring = modelo de actividad o detalle

### 3. Identificación de modelos
### Modelo principal: `academy.student`
Representa al alumno

Es el modelo desde el que tiene sentido resumir información como:

- nombre
- email
- número total de tutorías
- última tutoría
- estado académico

Es la entidad "quién"

### Modelo de actividad: `academy.tutoring`

Representa cada tutoría realizada o registrada

Cada registro de este modelo representa una interacción concreta:

- asunto
- fecha
- notas
- alumno al que pertenece

Es la entidad "qué ocurrió"

### 4. Relación entre los modelos

La relación lógica del negocio es:
- Un alumno puede tener muchas tutorías
- Una tutoría pertenece a un solo alumno

Esto es una relación 1 a N:
- 1 alumno
- N tutorías
En Odoo, esto se modela así:
- en `academy.tutoring`: un `Many2one` hacia `academy.student`
-  en `academy.student`: un `One2many` hacia `academy.tutoring`

### 5. Por qué la relación se diseña así
No sólo poner código, sino justificarlo.

La relación es 1-N porque:
- el alumno es la entidad acumuladora de actividad
- la tutoría es una ocurrencia en el tiempo
- necesitamos poder contar tutorías por alumno
- necesitamos navegar desde el alumno a sus tutorías y desde la tutoría al alumno

Dicho de otro modo:
- `academy.student` responde a "quién es"
- `academy.tutoring` responde a "qué interacción hubo"

Este es el patrón que aparece en los dominios
- alumnos - > tutorías
