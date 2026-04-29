# Skill: Desarrollo de módulos Odoo 19

## Objetivo

Ayudar a crear, revisar y explicar módulos personalizados para Odoo 19, usando buenas prácticas de desarrollo, ORM, vistas XML, seguridad, datos demo y documentación.

## Contexto del proyecto

- ERP/CRM: Odoo 19
- Base de datos: PostgreSQL
- Entorno: Ubuntu Server en máquina virtual
- IDE: Kiro 
- Control de versiones: Git
- Desarrollo local en carpeta `addons/` 

## Reglas generales

1. Usar siempre ORM de Odoo cuando sea posible.
2. Evitar SQL directo salvo que se justifique.
3. Explicar cada archivo creado.
4. Separa modelos, vistas, seguridad y datos.
5. Mantener nombres técnicos en `snake_case`.
6. Usar modelos con nombres tipo:
   - `academy.student`
   - `academy.tutoring`
   - `clinic.patient`
   - `clinic.appointment`

## Estructura mínima de un módulo

Cuando se cree un módulo Odoo, genera esta estructura:

```text
nombre_modulo/
|-- __init__.py
|-- __manifest__.py
|-- models/
|   |-- __init__.py
|   |-- modelo.py
|-- views/
|   |-- modelo_views.xml
|-- security/
|   |ir.model.access.csv
|--README.md

```
