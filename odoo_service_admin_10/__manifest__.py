# -*- encoding: utf-8 -*-
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
    "name": "Odoo Service Admin",
    "version": "1.0",
    "depends": [
        "base",
    ],
    #"price": ,
    #"currency": "",
    "author": "César Cordero Rodríguez <cesar.cordero.r@gmail.com>",
    "website": "https://rockcesar.github.io/",
    'images': ['static/description/description.png'],
    "contributors": [
        "César Cordero Rodríguez <cesar.cordero.r@gmail.com>",
    ],
    "category": "Industries",
    "summary": "",
    "data": [
        "security/config_security.xml",
        "security/ir.model.access.csv",
        "views/administration_view.xml",
        "views/servers_view.xml",
        "views/user_view.xml",
    ],
    'qweb': [
    ],
    "installable": True,
}
