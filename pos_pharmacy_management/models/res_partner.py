from odoo import api, models, fields, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_doctor = fields.Boolean(string='Is a Doctor')


