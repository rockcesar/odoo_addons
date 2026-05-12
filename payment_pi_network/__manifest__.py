{
    'name': 'Pi Network Payment Provider',
    'version': '1.0',
    'category': 'Accounting/Payment Providers',
    'summary': 'Permite recibir pagos con Pi Coin en tu e-commerce.',
    'description': """
                       This module is made with AI. Test with caution.
                       Módulo de proveedor de pagos para integrar la SDK de Pi Network en Odoo 18.
                   """,
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
