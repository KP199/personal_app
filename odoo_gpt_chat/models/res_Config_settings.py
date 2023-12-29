from odoo import api, fields, models, _

class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    chat_bot_id = fields.Char("Chat bot ID")
    show_chat_bot = fields.Boolean("Show chat Bot", default=False)
    show_chat_bot_f = fields.Boolean("Show chat Bot in frontend", default=True)
    show_chat_bot_b = fields.Boolean("Show chat Bot in backend", default=True)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        config_parameter_obj = self.env['ir.config_parameter'].sudo()
        res.update(
           show_chat_bot=config_parameter_obj.get_param('whisperchat_bits.show_chat_bot', False),
           show_chat_bot_f=config_parameter_obj.get_param('whisperchat_bits.show_chat_bot_f', True),
           show_chat_bot_b=config_parameter_obj.get_param('whisperchat_bits.show_chat_bot_b', True),
           chat_bot_id=config_parameter_obj.get_param('whisperchat_bits.chat_bot_id', False)
           
        )
        return res

    @api.model
    def set_values(self):
        config_parameter_obj = self.env['ir.config_parameter'].sudo()
        config_parameter_obj.set_param('whisperchat_bits.chat_bot_id', self.chat_bot_id) 
        config_parameter_obj.set_param('whisperchat_bits.show_chat_bot', self.show_chat_bot) 
        config_parameter_obj.set_param('whisperchat_bits.show_chat_bot_f', self.show_chat_bot_f) 
        config_parameter_obj.set_param('whisperchat_bits.show_chat_bot_b', self.show_chat_bot_b) 
        super(ResConfigSettings, self).set_values()