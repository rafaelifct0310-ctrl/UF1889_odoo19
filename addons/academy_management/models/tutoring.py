# -*- coding: utf-8 -*-

from odoo import fields, models


class AcademyTutoring(models.Model):
    _name = 'academy.tutoring'
    _description = 'Tutoring'

    name = fields.Char(string='Name', required=True)
    student_id = fields.Many2one(
        'academy.student',
        string='Student',
        required=True
    )
    course = fields.Char(string='Course')
    date = fields.Date(string='Date')
    duration = fields.Float(string='Duration (hours)')
    notes = fields.Text(string='Notes')