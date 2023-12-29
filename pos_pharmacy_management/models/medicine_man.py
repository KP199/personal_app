from odoo import api, models, fields, _


class MedicineManufacture(models.Model):
    _name = 'medicine.manufacture'
    _description = 'Medicine Manufacture'

    name = fields.Char(string="Name",required=True)
    parent_id = fields.Many2one('medicine.manufacture', string='Category')



