from odoo import api, models, fields, _


class MedicineUsage(models.Model):
    _name = 'medicine.usage'
    _description = 'Medicine Usage'

    name = fields.Char(string="Name",required=True)
    description = fields.Text(string="Description",required=True)
    


