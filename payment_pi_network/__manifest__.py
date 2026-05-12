{
    'name': 'Pi Network Payment Provider',
    'version': '1.0',
    'category': 'Accounting/Payment Providers',
    'summary': 'Allows you to receive payments with Pi Coin in your e-commerce store.',
    'description': """
                       This module is made with AI. Test with caution.
                       Payment provider module to integrate the Pi Network SDK into Odoo 18.
                   """,
    'version': '1.0',
    "author": "César Cordero Rodríguez <cesar.cordero.r@gmail.com>",
    "website": "https://rockcesar.github.io/",
    'depends': ['payment', 'website_sale'],
    'data': [
        'views/payment_provider_views.xml',
        'views/payment_templates.xml',
        'data/payment_provider_data.xml',
    ],
    'images': ['static/description/icon.png'],
    'application': False,
    'installable': True,
    'license': '',
}
