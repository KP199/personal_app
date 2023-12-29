# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.addons.website_sale.controllers.variant import WebsiteSaleVariantController
from odoo.addons.website_sale_renting.controllers.product import parse_date
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.http import request

class WebsiteSaleRentingVariantController(WebsiteSaleVariantController):
    @http.route()
    def get_combination_info_website(
        self, *args, context=None, start_date=None, end_date=None, **kwargs
    ):
        """ Override to parse and add to context optional pickup and return dates.
        """
        context = context if context is not None else {}
        if start_date and end_date:
            context.update(start_date=parse_date(start_date), end_date=parse_date(end_date))
        return super().get_combination_info_website(
            *args, context=context, start_date=start_date, end_date=end_date, **kwargs
        )

class RentalAccount(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super(RentalAccount, self)._prepare_home_portal_values(counters)
        if 'rental_count' in counters:
            rental_count = request.env['sale.order'].search_count([('is_rental_order', '=', True)])
            values['rental_count'] = rental_count
        return values
