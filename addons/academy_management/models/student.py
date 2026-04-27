# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AcademyStudent(models.Model):
    _name = 'academy.student'
    _description = 'Student online academy'

    name = fields.Char(
        string='Name',
        required=True
    )
    email = fields.Char(
        string='Email'
    )
    phone = fields.Char(
        string='Phone'
    )
    birth_date = fields.Date(
        string='Birth Date'
    )
    address = fields.Char(
        string='Address'
    )
    active = fields.Boolean(
        string='Activo',
        default=True
    )

    tutoring_ids = fields.One2many(
        comodel_name='academy.tutoring',
        inverse_name='student_id',
        string='Tutorías'
    )

    tutoring_count = fields.Integer(
        compute='_compute_tutoring_count',
        string='Total Tutorías'
    )

    last_tutoring_date = fields.Date(
        compute='_compute_last_tutoring_date',
        string='Última Tutoría'
    )

    @api.depends('tutoring_ids')
    def _compute_tutoring_count(self):
        for record in self:
            record.tutoring_count = len(record.tutoring_ids)

    @api.depends('tutoring_ids')
    def _compute_last_tutoring_date(self):
        for record in self:
            if record.tutoring_ids:
                dates = record.tutoring_ids.mapped('date')
                record.last_tutoring_date = max(d for d in dates if d)
            else:
                record.last_tutoring_date = False