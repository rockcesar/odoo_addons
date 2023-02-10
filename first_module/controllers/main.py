# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

from odoo import SUPERUSER_ID

import json

class ControllerTranslate(http.Controller):
    
    @http.route(['/person_website'], type='json', auth='user', csrf=False, website=True)
    def translate_text(self, **kwargs):
        values = kwargs
        
        values.update({'docs': request.env['person'].sudo(SUPERUSER_ID).search([])})
        
        return request.render("first_module.person_website", values)

    @http.route(['/person_onboard'], type='json', auth='user', csrf=False, website=True)
    def onboard(self, **kwargs):
        values = kwargs
        
        values.update({'docs': request.env['person'].sudo(SUPERUSER_ID).search([])})
        
        return {
            'html': request.env.ref('first_module.person_onboard')._render(values)
        }
        
    @http.route('/call-fuction-example', type='http', auth="user", website=True, csrf=False, methods=['POST'])
    def call_fuction_example(self, **kw):
        _logger.info(kw['var_1'])
        
        return json.dumps({'result': kw['var_1']})

    @http.route('/firs_module/person_onboarding', auth='user', type='json')
    def person_invoice_onboarding(self):
        company = request.env.company
        person = request.env["person"].search([], limit=1)
        if len(person) == 0:
            return {}
        person = person[0]
        if not request.env.is_admin() or \
                person.first_module_onboarding_car_state == 'option1':
            return {}

        return {
            'html': request.env.ref('first_module.person_onboarding_panel')._render({
                'company': company,
                'state': {'first_module_onboarding_car_state': person.first_module_onboarding_car_state}
                })
        }
