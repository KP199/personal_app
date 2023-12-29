from odoo import models, fields


class ChemicalClass(models.Model):
    _name = 'chemical.class'
    _description = 'Chemical Class'

    name = fields.Char(string="Name",required=True)

