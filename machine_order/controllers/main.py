from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError

class InquireWebsite(http.Controller):

    @http.route('/submit_inquire', type='http', auth="public", website=True, csrf=False)
    def submit_inquire(self, **post):
        # Retrieve form data
        name = post.get('name')
        email = post.get('email')
        interested = post.get('interested')
        phones = post.get('phones')
        project = post.get('project')
        talk = post.get('talk')
        subject = post.get('subject')

        #
        # date = post.get('date')
        # time = post.get('time')
        # guests = int(post.get('guests'))
        # location = post.get('location')
        # meal = post.get('meal')
        # breakfast = post.get('breakfast')
        # lunch = post.get('lunch')
        # dinner = post.get('dinner')
        # more = post.get('more')
        # suggestion = post.get('suggestion')


        # Create a new reservation record
        reservation = request.env['product.inquire'].sudo().create({
            'name': name,
            'email': email,
            'phones': phones,
            'interested': interested,
            'project': project,
            'talk': talk,
            'subject': subject,
            # 'meal': meal,
            # 'breakfast': breakfast,
            # 'lunch': lunch,
            # 'dinner': dinner,
            # 'more': more,
            # 'suggestion': suggestion,

        })

        try:
            machine_order.validate_and_update()
        except ValidationError as e:
            return request.redirect('/error_page')  # Redirect to an error page if validation fails

        return request.redirect('/thank_you_page')  # Redirect to a thank you page after successful submission
