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
    "name": "Web - Button PopUp",
    "version": "1.0",
    "depends": [
        "web",
    ],
    #"price": 30.50,
    #"currency": "EUR",
    "author": "César Cordero Rodríguez <cesar.cordero.r@gmail.com>",
    "website": "https://rockcesar.github.io/",
    'images': ['static/description/popup.png'],
    "contributors": [
        "César Cordero Rodríguez <cesar.cordero.r@gmail.com>",
    ],
    "category": "Extra Tools",
    "summary": "",
    "data": [
        "views/template.xml",
        "views/demo_popup_view.xml",
        "security/ir.model.access.csv",
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
    "installable": True,
}
