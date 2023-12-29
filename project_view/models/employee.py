from odoo import api, models, fields, _


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    agreement_id = fields.Many2one('project.management', string="Agreement")


