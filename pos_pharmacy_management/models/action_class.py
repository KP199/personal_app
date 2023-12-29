from odoo import api, models, fields, _

class ActionClass(models.Model):
    _name = 'action.class'
    _description = 'Action Class'

    name = fields.Char(string="Name", required=True)