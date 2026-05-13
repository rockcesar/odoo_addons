{
    'name': 'Payment Provider for Pi Network',
    'version': '1.0',
    'category': 'Accounting/Payment Providers',
    'summary': 'Allows you to receive payments with Pi Coin in your e-commerce store.',
    'description': """
                       This module is made with AI. Test with caution.
                       
                       Adapt to your business.
                       
                       Payment provider module to integrate the Pi Network SDK into Odoo 18.
                       
                       Repo:
                       https://github.com/rockcesar/odoo_addons/tree/18.0
                       
                       Make sure to create the Pi currency in Odoo to make works the following line:
                       https://github.com/rockcesar/odoo_addons/blob/e7c5efd6004c52ff15abaeac9a0ebc3c3d20d749/payment_pi_network/models/payment_provider.py#L25
                       res |= self.env['res.currency'].search([('name', '=', 'PI')])
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
