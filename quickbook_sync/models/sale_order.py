from odoo import api, fields, models, _
from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer
import requests
from requests_oauthlib import OAuth2Session


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_fetch_tax_quickbook(self):
        auth_client = AuthClient(
            client_id=self.env.user.company_id.client_id,
            client_secret=self.env.user.company_id.client_sec,
            environment=self.env.user.company_id.qbo_domain,
            redirect_uri='http://localhost:8069',
        )
        base_url = 'https://sandbox-quickbooks.api.intuit.com'
        client = QuickBooks(
            auth_client=auth_client,
            refresh_token='AB11707990156dOdVooLa3VS0bkRMSHsDU6H9mFRoZSTtvtAVq',
            company_id=4620816365326192720,
        )
        tax_records_endpoint = f'{base_url}/v3/company/4620816365326192720/query?query=select * from TaxRate'
        response = client.get(tax_records_endpoint)
        tax_list = []
        if response.get("QueryResponse"):
            for record in response['QueryResponse']['TaxRate']:
                tax_rec = self.env['account.tax'].search([('name', '=', record['Name']),
                                                          ('amount', '=', record['RateValue'])], limit=1)
                if not tax_rec:
                    tax_rec = self.env['account.tax'].create({
                        'name': record['Name'],
                        'amount': record['RateValue'],

                    })
                tax_list.append(tax_rec.id)
        for res in self.order_line:
            res.tax_id = [(6, 0, tax_list)]
