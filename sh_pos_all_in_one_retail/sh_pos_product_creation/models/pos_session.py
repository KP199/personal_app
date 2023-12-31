# Copyright (C) Softhealer Technologies.
# Part of Softhealer Technologies.

import re
from odoo import models,fields

class PosSessionInherit(models.Model):
    _inherit = "pos.session"

    def _loader_params_account_tax(self):
        result = super(PosSessionInherit,
                       self)._loader_params_account_tax()
        result['search_params']['fields'].append('type_tax_use')
        return result

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()

        if 'product.category' not in result:
            result.append('product.category')
       
        return result

    def _loader_params_product_category(self):
        return {'search_params': {'domain': [], 'fields': ['display_name','id'], 'load': False}}

    def _get_pos_ui_product_category(self, params):
        return self.env['product.category'].search_read(**params['search_params'])
    
    def _pos_data_process(self, loaded_data):
        super()._pos_data_process(loaded_data)
        loaded_data['product_categories_by_id'] = {data['id']: data for data in loaded_data['product.category']}
       