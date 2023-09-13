# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
{
    'name': 'Criptolago payment for Odoo',
    'category': 'Website/Website',
    'sequence': 54,
    'summary': 'Criptolago payment for Odoo',
    'version': '2.1',
    "author": "César Cordero Rodríguez <cesar.cordero.r@gmail.com>",
    "website": "https://rockcesar.github.io/",
    "contributors": [
        "César Cordero Rodríguez <cesar.cordero.r@gmail.com>",
    ],
    'description': """
Suscríbete a https://criptolago.io, y verifica tu usuario.

Para usar el módulo, debes agregarte como administrador del módulo al grupo: Criptolago Admin Group

Luego debes agregar el código de cliente en el menú Config Admin Criptolago -> Admin Criptolago

Main page: /criptolago

Más información aquí: https://dev-rockcesar.blogspot.com/2020/09/pagar-con-criptolago.html""",
    'depends': ['website'],
    'data': [
        'views/website_criptolago_templates.xml',
        'security/groups_security.xml',
        'views/admin_criptolago_v.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
    ],
    'images': ['static/description/icon.png'],
    'qweb': [],
    'installable': True,
    'auto_install': True,
}
