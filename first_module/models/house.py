# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError

class house(models.Model):
    _name = "house"
    _description = "House"

    name = fields.Char('Name')
    description = fields.Char('Description')
    persons_ids = fields.Many2many(
        comodel_name='person',
        relation='person_house_rel',
        column1='house_id',
        column2='person_id',
        string=u'Persons which lives',
        help=u'Persons which lives'
    )
