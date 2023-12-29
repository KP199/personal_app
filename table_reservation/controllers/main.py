from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError

class ReservationWebsite(http.Controller):

    @http.route('/submit_reservation', type='http', auth="public", website=True, csrf=False)
    def submit_reservation(self, **post):
        # Retrieve form data
        name = post.get('name')
        email = post.get('email')
        phone = post.get('phone')
        date = post.get('date')
        time = post.get('time')
        guests = int(post.get('guests'))
        location = post.get('location')
        meal = post.get('meal')
        breakfast = post.get('breakfast')
        lunch = post.get('lunch')
        dinner = post.get('dinner')
        more = post.get('more')
        suggestion = post.get('suggestion')


        # Create a new reservation record
        reservation = request.env['restaurant.reservation'].sudo().create({
            'name': name,
            'email': email,
            'phone': phone,
            'date': date,
            'time': time,
            'guests': guests,
            'location': location,
            'meal': meal,
            'breakfast': breakfast,
            'lunch': lunch,
            'dinner': dinner,
            'more': more,
            'suggestion': suggestion,

        }
        )

        try:
            reservation.validate_and_update()
        except ValidationError as e:
            return request.redirect('/error_page')  # Redirect to an error page if validation fails

        return request.redirect('/thank_you_page')  # Redirect to a thank you page after successful submission
