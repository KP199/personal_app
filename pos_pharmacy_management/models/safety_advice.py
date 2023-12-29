from odoo import api, models, fields, _


class MedicineSafetyAdvice(models.Model):
    _name = 'medicine.safety.advice'
    _description = 'Safety Advice'

    name = fields.Char(string="Name",required=True)
    safety_advice = fields.Text(string="Safety Advice")
