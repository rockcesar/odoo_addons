# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError
from odoo.modules.module import get_module_resource

_logger = logging.getLogger(__name__)

class ConfigAdminServers(models.Model):
    _name = "config.admin.servers"
    _description = "Configuration Admin Servers"
    _rec_name = "name_config"
    
    name_config = fields.Char('Name for the configuration', help='Name for the configuration')
    user_id = fields.Many2one('res.users', string='Users')
    server_ids = fields.One2many('config.server.list', 'config_admin_id', string='Servers')
    #can_stop = fields.Boolean('Can stop')
    #can_start = fields.Boolean('Can start')
    #can_restart = fields.Boolean('Can restart')

    def write(self, vals):
        result = super(ConfigAdminServers, self).write(vals)
        
        #result_self = self.search([('id', '=', self.id)])
        
        #result_config = self.env['config.user.servers'].search([('config_admin_id', '=', self.id), ('server_id', 'not in', [x.id for x in result_self.server_ids])])
        
        #_logger.info(str(result_config))
        
        #result_config.unlink()
        
        return result
    
    _sql_constraints = [
        ('unique_user_id', 'UNIQUE(user_id)', 'The user must have just one configuration')
    ]
