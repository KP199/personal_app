
from odoo import http
from odoo.http import request

class KitchenScreenBase(http.Controller):

    @http.route('/get/chatbot', type="json", auth="public")
    def _get_chatbot(self):
        settings = request.env['res.config.settings'].sudo()
        whis_settings = settings.get_values()
        if whis_settings['show_chat_bot'] and whis_settings['chat_bot_id']:
            return {'id': whis_settings['chat_bot_id'], 'front_end': whis_settings['show_chat_bot_f'], 'back_end': whis_settings['show_chat_bot_b'] }
        else:
            return False