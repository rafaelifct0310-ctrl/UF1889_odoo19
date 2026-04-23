# Ejercicio 1. Identificar modelos y relaciones
#### Tema: Academia online

### 1. Que aprender
- Identificar en modelo que contiene la entidad principal
- Identificar el modelo que contiene la actividad o interacción
- Entender como se relaionan ambos modelos

### Este razonamiento es la base de la práctica
- primero identificas los datos
- consultas con ORM
- después agregas, los muestras y los exportas

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

- 