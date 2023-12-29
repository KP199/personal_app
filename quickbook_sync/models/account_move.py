import json

from odoo import api, fields, models, _
from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer
import requests
from requests_oauthlib import OAuth2Session


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_quickbook_sync = fields.Char(string="Quickbook Sync")

    def _action_auto_export_invoice_cron(self):
        auth_client = AuthClient(
            client_id=self.env.user.company_id.client_id,
            client_secret=self.env.user.company_id.client_sec,
            environment=self.env.user.company_id.qbo_domain,
            redirect_uri='http://localhost:8069',
        )
        base_url = 'https://sandbox-quickbooks.api.intuit.com'
        client = QuickBooks(
            auth_client=auth_client,
            refresh_token='AB117080801050Dbm17BBq8UxGejFxhjxvv7NjtwNDFGQrEPtH',
            company_id=4620816365326192720,
        )
        moves = self.env['account.move'].search([('is_quickbook_sync', '=', False)])
        invoice_endpoint = f'{base_url}/v3/company/4620816365326192720/invoice'
        for move in moves:
            invoice_params = {}
            invoice_params['Line'] = []
            for line in move.invoice_line_ids:
                invoice_params['Line'].append({
                    "DetailType": "SalesItemLineDetail",
                    "Amount": line.price_subtotal,
                    "SalesItemLineDetail": {
                        "ItemRef": {
                            "value": '31'
                        },
                        "Qty": line.quantity,
                    }
                })
            invoice_params['CustomerRef'] = {
                'value': '58'
            }
            invoice_response = client.post(invoice_endpoint, json.dumps(invoice_params))
            if invoice_response:
                move.is_quickbook_sync = True


    def action_quickbook_link(self):
        self.env['mail.mail'].sudo().create({
            'author_id': self.env.user.partner_id.id,
            'auto_delete': True,
            'body_html': '',
            'email_from': self.env.user.company_id.catchall_formatted or self.env.user.company_id.email_formatted,
            'email_to': self.env.user.partner_id.email,
            'subject': "Invoice %s Link" % (self.name),
            'state': 'outgoing'
        })

    def action_export_invoice_quickbook(self):
        auth_client = AuthClient(
            client_id=self.env.user.company_id.client_id,
            client_secret=self.env.user.company_id.client_sec,
            environment=self.env.user.company_id.qbo_domain,
            redirect_uri='http://localhost:8069',
        )
        base_url = 'https://sandbox-quickbooks.api.intuit.com'
        client = QuickBooks(
            auth_client=auth_client,
            refresh_token='AB117080801050Dbm17BBq8UxGejFxhjxvv7NjtwNDFGQrEPtH',
            company_id=4620816365326192720,
        )
        customer_endpoint = f'{base_url}/v3/company/4620816365326192720/customer'
        params = {
            "DisplayName": self.partner_id.name,
            "Suffix": "Jr",
            "Title": "Mr",
            "MiddleName": "B",
            "FamilyName": "King",
            "PrimaryPhone": {
                "FreeFormNumber": self.partner_id.mobile
            },
            "CompanyName": self.env.user.company_id.name,
            "BillAddr": {
                "CountrySubDivisionCode": self.partner_id.state_id.code,
                "City": self.partner_id.city,
                "PostalCode": self.partner_id.zip,
                "Line1": self.partner_id.street,
                "Country": self.partner_id.country_id.name
            },
            "GivenName": self.partner_id.name.split(" ")[0]
        }

        invoice_endpoint = f'{base_url}/v3/company/4620816365326192720/invoice'
        invoice_params = {}
        invoice_params['Line'] = []
        for line in self.invoice_line_ids:
            invoice_params['Line'].append({
                        "DetailType": "SalesItemLineDetail",
                        "Amount": line.price_subtotal,
                        "SalesItemLineDetail": {
                            "ItemRef": {
                                "value": '31'
                            },
                            "Qty": line.quantity,
                        }
            })
        invoice_params['CustomerRef'] = {
            'value': '58'
        }
        invoice_response = client.post(invoice_endpoint, json.dumps(invoice_params))
        if invoice_response:
            self.is_quickbook_sync = True
        tax_list = []
