# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_add_pos_menu = fields.Boolean(string="Add a Menu Bar")
    is_pos_advance_search = fields.Boolean(string="Advance Search")
    is_show_product_manu = fields.Boolean(string="Is Show Detail Product Manufacturer")
    is_storage_show = fields.Boolean(string="Is Storage Detail Show")
    is_medicine_use = fields.Boolean(string="Use Of Medicine")
    is_salt_alter = fields.Boolean(string="Salt Alternate")
    is_salt_comp = fields.Boolean(string="Salt Composition")
    is_substitute = fields.Boolean(string="Substitute")
    is_side_effect = fields.Boolean(string="Side Effects")
    is_safety_advice = fields.Boolean(string="Safety Advice")
    is_basic_salt = fields.Boolean(string="Basic Salt")
    is_show_medicine_info = fields.Boolean(string="Medicine Info")
    is_quick_pay_button = fields.Boolean(string="Quick Pay Button")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        is_add_pos_menu = params.get_param('is_add_pos_menu',
                                           default=False)
        is_pos_advance_search = params.get_param('is_pos_advance_search',
                                                 default=False)
        is_show_product_manu = params.get_param('is_show_product_manu',
                                                default=False)
        is_storage_show = params.get_param('is_storage_show',
                                           default=False)
        is_medicine_use = params.get_param('is_medicine_use',
                                           default=False)
        is_salt_alter = params.get_param('is_salt_alter',
                                         default=False)
        is_salt_comp = params.get_param('is_salt_comp',
                                        default=False)
        is_substitute = params.get_param('is_substitute',
                                         default=False)
        is_side_effect = params.get_param('is_side_effect',
                                          default=False)
        is_safety_advice = params.get_param('is_safety_advice',
                                            default=False)
        is_basic_salt = params.get_param('is_basic_salt',
                                         default=False)
        is_show_medicine_info = params.get_param('is_show_medicine_info',
                                                 default=False)
        is_quick_pay_button = params.get_param('is_quick_pay_button',
                                               default=False)

        res.update(is_add_pos_menu=is_add_pos_menu,
                   is_pos_advance_search=is_pos_advance_search,
                   is_show_product_manu=is_show_product_manu,
                   is_storage_show=is_storage_show,
                   is_medicine_use=is_medicine_use,
                   is_salt_alter=is_salt_alter,
                   is_salt_comp=is_salt_comp,
                   is_substitute=is_substitute,
                   is_side_effect=is_side_effect,
                   is_safety_advice=is_safety_advice,
                   is_basic_salt=is_basic_salt,
                   is_show_medicine_info=is_show_medicine_info,
                   is_quick_pay_button=is_quick_pay_button)
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            "is_add_pos_menu",
            self.is_add_pos_menu)
        self.env['ir.config_parameter'].sudo().set_param(
            "is_pos_advance_search",
            self.is_pos_advance_search)
        self.env['ir.config_parameter'].sudo().set_param(
            "is_show_product_manu",
            self.is_show_product_manu)
        self.env['ir.config_parameter'].sudo().set_param(
            "is_storage_show",
            self.is_storage_show)
        self.env['ir.config_parameter'].sudo().set_param(
            "is_medicine_use",
            self.is_medicine_use)
        self.env['ir.config_parameter'].sudo().set_param(
            "is_salt_alter",
            self.is_salt_alter)
        self.env['ir.config_parameter'].sudo().set_param(
            "is_salt_comp",
            self.is_salt_comp)
        self.env['ir.config_parameter'].sudo().set_param(
            "is_substitute",
            self.is_substitute)
        self.env['ir.config_parameter'].sudo().set_param(
            "is_side_effect",
            self.is_side_effect)
        self.env['ir.config_parameter'].sudo().set_param(
            "is_safety_advice",
            self.is_safety_advice)
        self.env['ir.config_parameter'].sudo().set_param(
            "is_basic_salt",
            self.is_basic_salt)
        self.env['ir.config_parameter'].sudo().set_param(
            "is_show_medicine_info",
            self.is_show_medicine_info)
        self.env['ir.config_parameter'].sudo().set_param(
            "is_quick_pay_button",
            self.is_quick_pay_button)

