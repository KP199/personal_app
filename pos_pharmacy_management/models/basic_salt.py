from odoo import api, models, fields, _

class BasicSalt(models.Model):
    _name = 'basic.salt'
    _description = 'Basic Salt'

    name = fields.Char(string="Basic Salt",required=True)

