# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError
from odoo.modules.module import get_module_resource

_logger = logging.getLogger(__name__)

class DemoPopup(models.Model):
    _name = 'demo.popup'
    
    urls = fields.Selection(string="URLs",selection = [("URL:https://www.google.com", "https://www.google.com"),("URL:https://www.wikipedia.com", "https://www.wikipedia.com"),("URL:http://localhost:8069", "http://localhost:8069")])
