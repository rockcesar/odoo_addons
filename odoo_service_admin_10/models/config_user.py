# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models
from odoo import tools, _
from odoo import exceptions
from odoo.exceptions import ValidationError
from odoo.modules.module import get_module_resource

_logger = logging.getLogger(__name__)

class ConfigUserServers(models.Model):
    _name = "config.user.servers"
    _description = "Configuration User Servers"
    _rec_name = "server_id"
    
    def _default_admin(self):
        return self.env['config.admin.servers'].search([('user_id', '=', self.env.user.id)])
    
    config_admin_id = fields.Many2one('config.admin.servers', string='Config Admin', default=_default_admin, domain="[('user_id', '=', uid)]", compute="_curr_user", store=True)
    server_ids = fields.Many2many('config.server', 'config_user_config_server_rel', 'config_user_id', 'config_server_id', compute="_curr_server", string="Severs IDS")
    server_id = fields.Many2one('config.server', string='Server', required=True, domain="[('id', 'in', server_ids)]")
    command = fields.Char('Command', related='server_id.command')
    status = fields.Char('Status', compute="_get_status", store=False)
    can_start = fields.Boolean('Can start', store=False, compute="_can")
    can_stop = fields.Boolean('Can stop', store=False, compute="_can")
    can_restart = fields.Boolean('Can restart', store=False, compute="_can")
    
    @api.model
    def _get_status(self):
        for s in self:
            s.status = s.server_id.status
        
    @api.onchange('server_id')
    def _get_status(self):
        for s in self:
            s.status = s.server_id.status
    
    @api.model
    def _can(self):
        for s in self:
            result = self.env['config.server.list'].search([('config_admin_id', '=', s.config_admin_id.id), 
                                                            ('server_id', '=', s.server_id.id)])
            
            if len(result) > 0:
                s.can_start = result.can_start
                s.can_stop = result.can_stop
                s.can_restart = result.can_restart
            else:
                s.can_start = False
                s.can_stop = False
                s.can_restart = False
    
    @api.onchange('server_id')
    def _can_server(self):
        result = self.env['config.server.list'].search([('config_admin_id', '=', self.config_admin_id.id), 
                                                        ('server_id', '=', self.server_id.id)])
        
        if len(result) > 0:
            self.can_start = result.can_start
            self.can_stop = result.can_stop
            self.can_restart = result.can_restart
        else:
            self.can_start = False
            self.can_stop = False
            self.can_restart = False
    
    #@api.multi
    #def write(self, vals):
    #    #print str(self.env.context)
    #    #raise exceptions.UserError(_('This is not to edit, just to Start, Stop or Restart Odoo servers'))
    
    @api.model
    def _curr_user(self):
        for s in self:
            s.config_admin_id = self.env['config.admin.servers'].search([('user_id', '=', self.env.user.id)])
    
    @api.depends('config_admin_id.server_ids')
    def _curr_server(self):
        for s in self:
            result = list()
            for i in self.config_admin_id.server_ids:
                result.append(i.server_id.id)
            
            s.server_ids = self.env["config.server"].search([('id','in',result)])
    
    def stop_service(self):
        for s in self:
            s.server_id.stop_service()
    
    def start_service(self):
        for s in self:
            s.server_id.start_service()
    
    def restart_service(self):
        for s in self:
            s.server_id.restart_service()
    
    def refresh_service(self):
        for s in self:
            s.server_id.refresh_service()
    
    _sql_constraints = [
        ('unique_config_admin_server_id', 'UNIQUE(config_admin_id, server_id)', 'The user must have just one configuration per server')
    ]
