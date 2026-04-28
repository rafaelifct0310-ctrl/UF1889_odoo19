from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    seguimientos_count = fields.Integer(
        string='Seguimientos',
        compute='_compute_seguimientos_count',
        compute_sudo=True,
    )

    def _compute_seguimientos_count(self):
        for partner in self:
            if partner.id:
                domain = [
                    ('res_model', '=', 'res.partner'),
                    ('res_id', '=', partner.id)
                ]
                seguimientos = self.env['mail.activity'].search_count(domain)
                partner.seguimientos_count = seguimientos
            else:
                partner.seguimientos_count = 0