from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_enable_quick_export = fields.Boolean(string="Enable Auto Export")

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            is_enable_quick_export=self.env['ir.config_parameter'].sudo(
            ).get_param('quickbook_sync.is_enable_quick_export'),
        )
        return res


    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'quickbook_sync.is_enable_quick_export', self.is_enable_quick_export)
        return res






