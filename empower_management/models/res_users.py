# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    project_ids = fields.One2many('project.project', 'activity_user_id', string="Projects")


