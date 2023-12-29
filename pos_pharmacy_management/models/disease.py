from odoo import api, models, fields, _

class Disease(models.Model):
    _name = 'disease.disease'
    _description = 'Disease'

    name = fields.Char(string="Name",required=True)
    description = fields.Char(string="Description",required=True)

