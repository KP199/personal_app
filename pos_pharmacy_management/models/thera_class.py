from odoo import api, models, fields, _


class TheraClass(models.Model):
    _name = 'thera.class'
    _description = 'Therapeutic Class'

    name = fields.Char(string="Name", required=True)
