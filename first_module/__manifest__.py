# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'First module (for learning Odoo)',
<<<<<<< HEAD
    'depends': ['base', 'web', 'website'],
=======
    'depends': ['base', 'web', 'website', 'point_of_sale'],
>>>>>>> 961b5f77435db53686f600f11b302b3f8d9aa107
    'author': 'César Cordero Rodríguez <cesar.cordero.r@gmail.com>',
    'website': 'https://cr-innova.negocio.site/',
    'contributors': [
        'César Cordero Rodríguez <cesar.cordero.r@gmail.com>',
    ],
    'images': ['static/description/first.png'],
    'description': """
        
        Primer módulo.
        
    """,
    'category': 'Extra Tools',
    'sequence': 32,
    'demo': [
    ],
    'data': [
        'reports/template_report.xml',
        'views/person_templates.xml',
        'views/car_v.xml',
        'views/house_v.xml',
        'views/person_v.xml',
        'views/res_partner_h.xml',
        'security/groups_security.xml',
        'views/menus_v.xml',
        'security/ir.model.access.csv',
    ],
<<<<<<< HEAD
    'qweb': [
=======
    'qweb': [ 'static/src/xml/OrderReceipt.xml'
>>>>>>> 961b5f77435db53686f600f11b302b3f8d9aa107
    ],
    "installable": True,
}
