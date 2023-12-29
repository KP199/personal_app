{
    'name': 'aeromen',
    'version': '1.0',
    'summary': 'Aromen snippet',
    'author': 'Ashish',
    'website': 'https://www.oddo.com',
    'depends': ['website', 'website_sale'],
    'data': [
        'views/website_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'Parroat_16/static/src/scss/website.scss',
        ],
    },
    'installable': True,
    'application': True,

}