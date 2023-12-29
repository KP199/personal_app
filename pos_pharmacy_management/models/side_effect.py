from odoo import api, models, fields, _


class MedicineSideEffect(models.Model):
    _name = 'medicine.side.effect'
    _description = 'Medicine Side Effect'

    name = fields.Char(string="Name",required=True)
    side_effect = fields.Char(string="Side Effect")
    
