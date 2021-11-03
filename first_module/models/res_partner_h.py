# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError

class res_partner(models.Model):
    _name = "res.partner"
    _description = "Res Partner"
    _inherit = ['res.partner']

    partner_number = fields.Char('Partner number')
