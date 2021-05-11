# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError

class house(models.Model):
    _name = "house"
    _description = "House"
    _inherit = ['house']

    house_number = fields.Char('House number')
