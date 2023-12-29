{
    'name': 'Pharmacy Management System',
    'author': 'Destiny Solutions',
    'website': 'www.destinysolutions.com',
    'summary': 'Pharmacy Management System',
    'depends': [
        'point_of_sale',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_pharmacy_management/static/src/scss/style.css',
            'pos_pharmacy_management/static/src/xml/**/*',
            'pos_pharmacy_management/static/src/**/*.js',
            'pos_pharmacy_management/static/src/js/medicinepopop.js',
            'pos_pharmacy_management/static/src/js/advance_search_popup.js',
            'pos_pharmacy_management/static/src/js/alternatemedicinepopup.js',
            'pos_pharmacy_management/static/src/js/models.js',
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/action_class.xml',
        'views/basic_salt.xml',
        'views/disease.xml',
        'views/medicine_manu.xml',
        'views/medicine_salt.xml',
        'views/res_config_setting.xml',
        'views/medicine_usage.xml',
        'views/safety_advice.xml',
        'views/salt_unit.xml',
        'views/side_effect.xml',
        'views/product_template_view.xml',
        'views/thera_class.xml',
        'views/menu.xml',
    ]
}
