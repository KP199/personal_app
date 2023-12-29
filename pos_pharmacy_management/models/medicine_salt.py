from odoo import api, models, fields, _


class MedicineSalt(models.Model):
    _name = 'medicine.salt'
    _description = 'Medicine Salt'

    name = fields.Char(string="Medicine Salt", required=True)
    basic_salt_id = fields.Many2one('basic.salt', string="Basic Salt")
    quantity = fields.Float(string="Quantity")
    salt_unit_id = fields.Many2one('salt.unit', string="Salt Unit")

