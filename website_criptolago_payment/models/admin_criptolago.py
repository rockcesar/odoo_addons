# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError

class admin_criptolago(models.Model):
    _name = "admin.criptolago"
    _description = "Admin Criptolago"
    
    _sql_constraints = [
        # Partial constraint, complemented by a python constraint (see below).
        ('admin_criptolago_unique_key', 'unique (active_code)', 'You can not have two active_code with the same Código activo!'),
    ]

    name = fields.Char('Nombre')
    active_code = fields.Boolean('Código activo', required=True)
    client_code = fields.Char('Código cliente', required=True)
    url_cancel = fields.Char('URL Cancel', required=True)
    url_fail = fields.Char('URL Fail', required=True)
    url_works = fields.Char('URL Works', required=True)
