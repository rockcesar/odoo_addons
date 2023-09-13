# -*- coding: utf-8 -*-
{   'active': True,
    'author': u'César Cordero Rodríguez <cesar.cordero.r@gmail.com>',
    'website': 'https://rockcesar.github.io/',
    'category': 'Translation',
    'demo_xml': [],
    'depends': [
        'base',
    ],
    'description': '''
        This is a new translator.

        Libraries to install:

	    This library py_translator:

                https://pypi.org/project/py-translator/

	    Download the library:

                wget https://files.pythonhosted.org/packages/17/37/27d6e7fa49cf383d556e8470a4ec39133a66f19bc24823ce1e395ed93d38/py_translator-2.1.9.tar.gz

                tar -xvf py_translator-2.1.9.tar.gz

                cd py_translator-2.1.9

                python3 setup.py install

	    Install Tor:
                aptitude install torsocks tor
    ''',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': u'Translator for Odoo',
    'test': [],
    'data': [
        'security/translator_odoo_security.xml',
        'security/ir.model.access.csv',
        'views/translator_views.xml',
        'views/languages_views.xml',
        'views/translator_templates.xml',
    ],
    'images': ['static/description/description.png'],

    'version': '',
    'application': True,
}
