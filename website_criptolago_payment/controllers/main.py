# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json

import requests

import logging
_logger = logging.getLogger(__name__)

class CriptolagoController(http.Controller):
    @http.route(['/criptolago', '/donation'], type='http', auth="public", website=True)
    def index(self, **kw):
        admin_criptolago_list = request.env["admin.criptolago"].sudo().search([('active_code', '=', True)])
        
        if len(admin_criptolago_list) == 0:
            client_code = ""
            url_cancel = ""
            url_fail = ""
            url_works = ""
        else:
            client_code = admin_criptolago_list[0].client_code
            url_cancel = admin_criptolago_list[0].url_cancel
            url_fail = admin_criptolago_list[0].url_fail
            url_works = admin_criptolago_list[0].url_works
        
        return http.request.render('website_criptolago_payment.criptolago', {'client_code': client_code, 
                                                                            'url_cancel': url_cancel, 'url_fail': url_fail,
                                                                            'url_works': url_works})
