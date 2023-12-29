from odoo import api, models, fields, _


class MedicineMultiPrice(models.Model):
    _name = 'medicine.multi.price'
    _description = 'Medicine Multi Price'

    name = fields.Char(string="Name", required=True)
    quantity = fields.Float(string="Quantity")
    unit_price = fields.Float(string="Unit Price")
    total_price = fields.Float(string="Price")

    @api.onchange('quantity', 'unit_price')
    def onchange_qty_price(self):
        for rec in self:
            rec.total_price = rec.quantity * rec.unit_price
