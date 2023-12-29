# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _


class ProjectTask(models.Model):
    _inherit = 'project.task'

    project_user_id = fields.Many2one('res.users', related='project_id.activity_user_id', string="Project User")



class ReportProjectTaskUser(models.Model):
    _inherit = 'report.project.task.user'

    is_project_user = fields.Boolean('Project User', compute='_compute_project_user')


    def _compute_project_user(self):
        for rec in self:
            if rec.project_id.activity_user_id == self.env.user.id:
                rec.is_project_user = True
            else:
                rec.is_project_user = False


