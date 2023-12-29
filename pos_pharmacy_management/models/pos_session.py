from odoo import api, models, fields, _


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        res = super(PosSession, self)._pos_ui_models_to_load()
        res.append('medicine.usage')
        res.append('basic.salt')
        res.append('medicine.safety.advice')
        res.append('medicine.manufacture')
        return res



    def _loader_params_product_product(self):
        res = super(PosSession, self)._loader_params_product_product()
        res['search_params']['fields'].append('medicine_manufacture_id')
        res['search_params']['fields'].append('medicine_usage_ids')
        res['search_params']['fields'].append('storage_type')
        res['search_params']['fields'].append('store_temperature')
        res['search_params']['fields'].append('basic_salt_ids')
        res['search_params']['fields'].append('medicine_safety_device_ids')
        res['search_params']['fields'].append('alternate_medicine_ids')
        return res


    def _loader_params_res_partner(self):
        res = super(PosSession, self)._loader_params_res_partner()
        res['search_params']['fields'].append('is_doctor')
        return res

    def _loader_params_medicine_manufacture(self):
        return {
            'search_params': {
                'domain': [],
                'fields': ['name', 'id'],
            },
        }

    def _get_pos_ui_medicine_manufacture(self, params):
        return self.env['medicine.manufacture'].search_read(**params['search_params'])

    def _loader_params_medicine_usage(self):
        return {
            'search_params': {
                'domain': [],
                'fields': ['name', 'id', 'description'],
            },
        }

    def _get_pos_ui_medicine_usage(self, params):
        return self.env['medicine.usage'].search_read(**params['search_params'])

    def _loader_params_basic_salt(self):
        return {
            'search_params': {
                'domain': [],
                'fields': ['name', 'id'],
            },
        }

    def _get_pos_ui_basic_salt(self, params):
        return self.env['basic.salt'].search_read(**params['search_params'])

    def _loader_params_medicine_safety_advice(self):
        return {
            'search_params': {
                'domain': [],
                'fields': ['name', 'id','safety_advice'],
            },
        }

    def _get_pos_ui_medicine_safety_advice(self, params):
        return self.env['medicine.safety.advice'].search_read(**params['search_params'])

