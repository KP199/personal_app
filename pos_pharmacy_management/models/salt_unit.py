from odoo import api, models, fields, _

class SaltUnit(models.Model):
    _name = 'salt.unit'
    _description = 'Salt Unit'

    name = fields.Char(string="Salt Unit",required=True)
