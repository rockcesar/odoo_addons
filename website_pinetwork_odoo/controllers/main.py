# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json

import requests

import logging
_logger = logging.getLogger(__name__)

from odoo.addons.website.controllers.main import Website

"""
class Website(Website):
    @http.route('/', type='http', auth="public", website=True)
    def index(self, **kw):
        super(Website, self).index(**kw)
        return http.request.render('website_pinetwork_odoo.mainpage', {})
"""

class PiNetworkBaseController(http.Controller):
    @http.route('/mainpage', type='http', auth="public", website=True)
    def index(self, **kw):
                    
        return http.request.render('website_pinetwork_odoo.mainpage')
    
    @http.route('/example', type='http', auth="public", website=True)
    def example(self, **kw):
        admin_app_list = request.env["admin.apps"].sudo().search([('app', '=', 'auth_first_app')])
        
        if len(admin_app_list) == 0:
            sandbox = False
        else:
            sandbox = admin_app_list[0].sandbox
        
        return http.request.render('website_pinetwork_odoo.example', {'sandbox': sandbox})
    
    @http.route('/get-user', type='http', auth="public", website=True, csrf=False, methods=['POST'])
    def get_user(self, **kw):
        pi_users_list = request.env["pi.users"].sudo().search([('pi_user_code', '=', kw['pi_user_code'])])
        
        if len(pi_users_list) == 0:
            return json.dumps({'result': False})
        
        return json.dumps({'result': True, 'pi_user_id': pi_users_list[0].pi_user_id, 'pi_user_code': pi_users_list[0].pi_user_code,
                            'points': pi_users_list[0].points, 'points_chess': pi_users_list[0].points_chess, 
                            'points_sudoku': pi_users_list[0].points_sudoku,
                            'points_snake': pi_users_list[0].points_snake, 'unblocked': pi_users_list[0].unblocked})
        
    @http.route('/pi-api', type='http', auth="public", website=True, csrf=False, methods=['POST'])
    def pi_api(self, **kw):
        return request.env["admin.apps"].pi_api(kw)
        
    @http.route('/pi-points', type='http', auth="public", website=True, csrf=False, methods=['POST'])
    def pi_points(self, **kw):
        pi_users_list = request.env["pi.users"].sudo().search([('pi_user_code', '=', kw['pi_user_code'])])
        
        if len(pi_users_list) == 0:
            request.env["pi.users"].sudo().create({'name': kw['pi_user_code'],
                                                    'pi_user_id': kw['pi_user_id'],
                                                    'pi_user_code': kw['pi_user_code'],
                                                    'points': 0,
                                                    'points_chess': 0,
                                                    'points_sudoku': 0,
                                                    'points_snake': 0,
                                                    'paid': 0,
                                                    'unblocked': False
                                                })
        else:
            if pi_users_list[0].unblocked:
                values = {'name': kw['pi_user_code'],
                                'pi_user_id': kw['pi_user_id'],
                                'pi_user_code': kw['pi_user_code'],
                            }
                if 'app_client' in kw:
                    if kw['app_client'] == "auth_platform":
                        values.update({'points_chess': pi_users_list[0].points_chess + float(kw['points'])})
                    elif kw['app_client'] == "auth_pidoku":
                        values.update({'points_sudoku': pi_users_list[0].points_sudoku + float(kw['points'])})
                    elif kw['app_client'] == "auth_snake":
                        values.update({'points_snake': pi_users_list[0].points_snake + float(kw['points'])})
                    
                pi_users_list[0].sudo().write(values)
        
        return json.dumps({'result': True})
        
    @http.route('/get-points/<string:pi_user_code>', type='http', auth="public", website=True)
    def get_points_user(self, pi_user_code, **kw):
        pi_users_list = request.env["pi.users"].sudo().search([], limit=50, order="points desc,unblocked desc,id asc")
        
        pi_user = request.env["pi.users"].sudo().search([('pi_user_code', '=', pi_user_code)])
        
        return http.request.render('website_pinetwork_odoo.list_points', {'pi_users_list': pi_users_list, 'pi_user': pi_user})
        
    @http.route('/get-points/', type='http', auth="public", website=True)
    def get_points(self, **kw):
        pi_users_list = request.env["pi.users"].sudo().search([], limit=50, order="points desc,unblocked desc,id asc")
        
        return http.request.render('website_pinetwork_odoo.list_points', {'pi_users_list': pi_users_list})
