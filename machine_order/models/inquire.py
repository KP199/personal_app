from odoo import api, fields, models, _
from lxml import etree
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.exceptions import ValidationError




class Productinquire(models.Model):
    _name = "product.inquire"
    _description = 'Product inquire'

    look = fields.Boolean(string="EVO - the best machine to get started with CNC milling")
    looki = fields.Boolean(string="PRO - a professional and powerful machine to cut through wood, metal and more'")
    lookii = fields.Boolean(string="FAB - our biggest CNC machine, designed to mill entire panels with high precision")
    # interested = fields.Selection[('Evo', ' EVO - the best machine to get started with CNC milling'),
    #                                ('Pro', 'PRO - a professional and powerful machine to cut through wood, metal and more'),
    #                                ('Fab', 'FAB - our biggest CNC machine, designed to mill entire panels with high precision')],
    #                                  string='Which machine model are you most interested in?')
    project = fields.Char(string='Tell us more about your project *')
    name = fields.Char(string='What is your full name?')
    email = fields.Char(string='What is your email address?')
    phones = fields.Char(string='Phone number',size=10)
    subject = fields.Char(string='Subject')
    talk = fields.Selection([('en', 'English'),
                             ('fr', 'Français'),
                             ('nl', 'Nederlands')],
                             string='In which language would you rather talk? *')