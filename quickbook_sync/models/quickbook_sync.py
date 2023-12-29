from odoo import api, fields, models, _
from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer

class ResCompany(models.Model):
    _inherit = 'res.company'

    client_id = fields.Char(string="Client ID")
    client_sec = fields.Char(string="Client Secret")
    acc_token_expire = fields.Datetime(string="Access Token expire in")
    ref_token_expire = fields.Datetime(string="Refresh Token expire in")
    minor_version = fields.Integer(string="Minor Version")
    auth_url = fields.Char(string="Authorization URL")
    auth_token_url = fields.Char(string="Authorization Token URL")
    redirect_url = fields.Char(string="Redirect URL")
    api_url = fields.Char(string="API URL")
    qbo_domain = fields.Selection([('sandbox', 'Sandbox')], string="QBO Domain")
    auth_id = fields.Char(string="Auth ID")


    def action_quickbook_auth(self):
        auth_client = AuthClient(
            client_id=self.client_id,
            client_secret=self.client_sec,
            environment=self.qbo_domain,
            redirect_uri='http://localhost:8069',
        )
        client = QuickBooks(
            auth_client=auth_client,
            refresh_token='AB11707976928Bu5YDawp1njNOmIYOkrmFzqmqXdgZnhsWEhqD',
            company_id=4620816365326192720,
        )
        customers = Customer.all(qb=client)
        print("/xzc/czcx/czxc/zxcxccxzc", customers)


    def action_quickbook_refresh_token(self):
        print("c/////////xxxxxxxxxxxxxx")







