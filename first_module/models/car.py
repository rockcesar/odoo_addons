# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError

class car(models.Model):
    _name = "car"
    _description = "Car"

    name = fields.Char('Name')
    description = fields.Char('Description')
    person_id = fields.Many2one(
        'person',
        ondelete='restrict',
        string=u'Persona',
        required=False,
    )
    photo_person = fields.Binary(related="person_id.photo")
<<<<<<< HEAD
=======
    

    def method_2(self):
        return True
>>>>>>> 961b5f77435db53686f600f11b302b3f8d9aa107
