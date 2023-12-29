from odoo import api, models, fields, _

class FactBox(models.Model):
    _name = 'fact.box'
    _description = 'Fact Box'

    name = fields.Char(string="Name",required=True)