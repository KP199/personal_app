from odoo import api, fields, models, _
from lxml import etree
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from odoo.exceptions import ValidationError




class RestaurantReservation(models.Model):
    _name = "restaurant.reservation"
    _description = 'Restaurant Reservation'

    name = fields.Char(string='Reservation Name')
    email = fields.Char(string='Email-Id')
    # phone = fields.Char(string='contact no',size=10)
    phones = fields.Char(string='Coontact no',size=10)
    date = fields.Date(string='Reservation Date')
    # times = fields.Datetime(string='Reservation Date')
    time = fields.Float(string="What time")

    times = fields.Selection([('Am', '7.30 AM To 8.30 AM'),
                                 ('Bm', '8.30 AM To 9.30 AM'),
                                 ('C', '9.30 AM To 10.30 AM'),
                                 ('D', '10.30 AM To 11.30 AM'),
                                 ('E', '11.30 AM To 12.30 AM'),
                                 ('G', '1.30 AM To 2.30 AM'),
                                 ('H', '2.30 AM To 3.30 AM'),
                                 ('8', '3.30 AM To 4.30 AM'),
                                 ('9', '4.30 AM To 5.30 AM'),
                                 ('10', '5.30 AM To 6.30 AM'),
                                 ('11', '6.30 AM To 7.30 AM'),
                                 ('12', '7.30 AM To 8.30 AM'),
                                 ('13', '8.30 AM To 9.30 AM'),
                                 ('14', '9.30 AM To 10.30 AM'),
                                 ('15', '10.30 AM To 11.30 AM'),
                                 ('16', '11.30 AM To 12.30 AM'),
                                 ('T', '12.30 AM To 00.30 AM')],
                                string='Reservation Time')
    guests = fields.Integer(string='Number of Guests')
    location = fields.Selection([('NY', 'Northside Grill & Deli - New York City NY'),
                                 ('FL', 'Southside Pizzeria - Miami, FL'),
                                 ('CA', 'Westside BBQ Shack - Los Angeles, CA'),
                                 ('MA', 'Eastside Bistro - Boston, MA')],
                                 string = 'Restaurant Location')
    meal = fields.Selection([('Breakfast', 'Sunrise feast'),
                                 ('lunch', 'Midday Meal'),
                                 ('Dinner', 'Dinnertime Delights')],
                                string='Choose your meal')
    breakfast = fields.Selection([('avacado', 'Classic American Breakfast'),
                                 ('toast', 'Avocado Toast')],
                                string='Sunrise Feast')
    lunch = fields.Selection([('salad', 'Caesar Salad'),
                                 ('chicken', 'Grilled Chicken Panini')],
                                string='Meadday Meal')
    dinner = fields.Selection([('mignon', 'Filet Mignon'),
                                 ('lobster', 'Lobster Linguine')],
                                string='Dinnertime Delights')
    more = fields.Selection([('dessert', 'Sweet Endings'),
                                 ('Burger', 'Sub & Patty'),
                                 ('N/A', 'May be Later')],
                                string='Wanna Taste more')
    dessert = fields.Selection([('cake', 'Molten Lava Cake'),
                                 ('fruit', 'Fresh Fruit Parfait')],
                                string='Sweet Endings')
    burger = fields.Selection([('burger', 'BBQ Bacon Burger'),
                                 ('wrap', 'Veggie Wrap')],
                                string='Sub & Patty')
    suggestion = fields.Char(string='Any special advice')

    @api.constrains('phones')
    def _check_phone_number_length(self):
        for record in self:
            if record.phones and len(record.phones) != 10:
                raise ValidationError('Phone number must be exactly ten digits.')