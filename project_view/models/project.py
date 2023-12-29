from odoo import api, models, fields, _


class ProjectManagement(models.Model):
    _name = 'project.management'
    _description = 'Project Management'

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    name = fields.Char(string="Name")
    employee_ids = fields.Many2many('hr.employee',string="")
    employee_count = fields.Integer(string="Employee Count", compute='_compute_employee_count', default=0)
    client_id = fields.Many2one('res.users', string="Client")
    project_cost = fields.Float(string="Project Cost")
    site = fields.Char(string="Site")
    address = fields.Text(string="Site Address")
    state = fields.Selection([('draft', 'Draft'),
                              ('run', 'Running'),
                              ('close', 'Close')], string="Status", default='draft')

    shift_time = fields.Char(string="Shift Timing")

    @api.depends('employee_ids')
    def _compute_employee_count(self):
        for rec in self:
            if rec.employee_ids:
                rec.employee_count = len(rec.employee_ids.ids)
            else:
                rec.employee_count = 0
