from odoo import api, models, fields, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_pharma_product = fields.Boolean(string="Is Pharma Product")
    is_medicine = fields.Boolean(string="Is a Medicine")
    medicine_usage_ids = fields.Many2many('medicine.usage', string="Medicine Uses")
    side_effect_ids = fields.Many2many('medicine.side.effect', string="Side Effects")
    medicine_salt_ids = fields.Many2many('medicine.salt', string="Medicine Salt")
    fact_box_ids = fields.Many2many('fact.box', string="Fact Box")
    alternate_medicine_ids = fields.Many2many('product.product', 'product_product_medicine_rel', 'product_id', 'id',
                                              string="Alternate Medicines")
    basic_salt_ids = fields.Many2many('basic.salt', string="Interaction with drugs")
    manage_multi_uom = fields.Boolean('Manage Multi UOM Price')
    product_price_uom_ids = fields.Many2many('medicine.multi.price', string="Multiple Price UOM")
    medicine_safety_device_ids = fields.Many2many('medicine.safety.advice', string="Safety Device")
    medicine_manufacture_id = fields.Many2one('medicine.manufacture', string="Manufacturer")
    storage_type = fields.Selection([('storage_top', 'Storage Top'), ('storage_below', 'Storage Below')],
                                    string="Storage")
    store_temperature = fields.Char(string="Temperature")


