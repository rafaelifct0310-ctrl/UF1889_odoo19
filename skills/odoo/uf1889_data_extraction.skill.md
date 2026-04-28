# Skill: UF1889 - Extracción de datos ERP (Odoo 19)

## Objetivo

Realizar la extracción y procesamiento de los datos
- número se seguimientos por cliente
- uso del ORM
- campo calculado
- exportación CSV
- simulación API JSON

## Modelos implicados

- res.partner -> clientes
- mail.activity -> seguimientos

## Paso 1: Identificación 

El cliente es el modelo principal.
El seguimiento es la actividad asociada.

Relación:
- Un cliente tiene muchos seguimientos.

## Paso 2: Consulta ORM

Usar `read_group` para optimizar:

```python
seguimientos = self.env['mail.activity'].read_group(
    domain=[('res_model', '=', 'res.partner')],  # dominio/filtro
    fields=['res_id'],                           # campos a leer/agrupar
    groupby=['res_id']                            # campo por el que se agrupa
)
```