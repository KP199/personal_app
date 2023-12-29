{
    'name': 'Reservation Management',
    'version': '1.0',
    'summary': 'Manage reservations for your restaurant.',
    'author': 'Ashish',
    'website': 'https://www.oddo.com',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/reservation_view.xml',
        'views/reservation_menu.xml'

    ],
    'installable': True,
    'application': True,

}


