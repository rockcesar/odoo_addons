# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import OrderedDict

from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from datetime import datetime, timedelta
from odoo import http
from odoo.exceptions import AccessError
from odoo.http import request
from odoo.tools.translate import _
import logging
_logger = logging.getLogger(__name__)

from odoo import SUPERUSER_ID

class ControllerTranslate(http.Controller):

    """
    @http.route(['/translate_website'], type='http', auth='public', website=True)
    def translate_website(self, **kwargs):
        values = {}
        values.update({'languages': request.env['language'].search([])})
        values.update({'type_of_input_list': [{'code': 'using_text_field', 'name': 'Using Text Field'}, 
                                    {'code': 'using_file', 'name': 'Using File'}]})
        return request.render("translator_odoo.translator_website", values)
    """

    @http.route(['/translate_website'], type='http', auth='public', website=True)
    def translate_text(self, **kwargs):
        values = kwargs
        
        if 'language' in values:
            #values.update({'name': 'Translation ' + str((datetime.now()).strftime(DEFAULT_SERVER_DATETIME_FORMAT))})
            
            if values['name'] == "":
                del values['name']
            if 'language'in values and values['language'] == "":
                del values['language']
            if 'text' in values and values['text'] == "":
                del values['text']
            if 'term_translated' in values and values['term_translated'] == "":
                del values['term_translated']
            if 'code' in values and values['code'] == "":
                del values['code']
            
            if 'type_of_input' in values and (values['type_of_input'] == "" or values['type_of_input'] == "using_file"):
                if 'name_of_file' in values:
                    if type(values['name_of_file']) != str:
                        values['name_of_file'] = values['name_of_file'].read().decode("utf-8").replace('\\ n', '\n').replace('\\n', '\n')
            
            language_id = request.env['language'].sudo(SUPERUSER_ID).search([('code', '=', values['language'])])
            values.update({'language': language_id.id})
            translate_it = request.env['translator'].sudo(SUPERUSER_ID).create(values)
            
            term_translated = translate_it.sudo(SUPERUSER_ID).translate_to_website()
            
            if len(term_translated) > 0:
                values.update({'term_translated': term_translated[0]})
            else:
                values.update({'term_translated': ''})
            
            values.update({'language_selected': language_id.code})
            values.update({'type_of_input_selected': values['type_of_input']})
        
        values.update({'languages': request.env['language'].sudo(SUPERUSER_ID).search([])})
        values.update({'type_of_input_list': [{'code': 'using_text_field', 'name': 'Using Text Field'}, 
                                    {'code': 'using_file', 'name': 'Using File'}]})

        return request.render("translator_odoo.translator_website", values)
