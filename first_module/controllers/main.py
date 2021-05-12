# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

from odoo import SUPERUSER_ID

class ControllerTranslate(http.Controller):

    @http.route(['/person_website'], type='http', auth='user', website=True)
    def translate_text(self, **kwargs):
        values = kwargs
        
        values.update({'docs': request.env['person'].sudo(SUPERUSER_ID).search([])})

        return request.render("first_module.person_website", values)
