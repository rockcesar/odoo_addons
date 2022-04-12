# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models
from odoo import tools, _
from odoo import exceptions
from odoo.exceptions import ValidationError
from odoo.modules.module import get_module_resource

import subprocess
import sys
from subprocess import Popen, PIPE

import configparser as ConfigParser

import os
import os.path

from os import listdir
from os.path import isfile, join

_logger = logging.getLogger(__name__)

class ConfigServer(models.Model):
    _name = "config.server"
    _description = "Configuration Server"
    _rec_name = "name"
    
    def get_curr_directory(self):
        try:
            Config = ConfigParser.ConfigParser()
            config_path = os.path.join(
                os.path.dirname(__file__),
                "../config/config.ini"
            )
            Config.read(config_path)
            return Config.get('ODOO_SERVERS', 'COMMAND_DIRECTORY')
        except:
            return False
            
    def _get_directory_list(self):
        curr_path = self.get_curr_directory()
        
        if not curr_path:
            raise exceptions.UserError(_('Look for the COMMAND_DIRECTORY inside this Odoo Addon path.'))
        
        list_files = []
        for path, subdirs, files in os.walk(curr_path):
            for subdir in subdirs:
                list_files.append((subdir, join(path,subdir)))
        
        return list_files
    
    """
    @api.model
    def _get_commands_list(self):
        curr_path = self.get_curr_directory()
        
        if not curr_path:
            raise exceptions.UserError(_('Look for the COMMAND_DIRECTORY inside this Odoo Addon path.'))
        
        list_files = []
        for path, subdirs, files in os.walk(curr_path):
            for name in files:
                list_files.append((name, join(path, name)))
        
        #_logger.info(str(list_files))
        return list_files
    """
    
    @api.depends('command_directory_list', 'command_directory')
    @api.onchange('command_directory_list', 'command_directory')
    def _get_commands_list_domain(self):
        for record in self:
            #_logger.info("self.command_directory " + str(record.command_directory))
            #_logger.info("self.command_directory_list " + str(record.command_directory_list))
            if record.command_directory and self.command_directory_list:
                curr_path = join(record.command_directory, record.command_directory_list)
                
                if os.path.exists(curr_path):
                    record.command_directory_list_domain = ', '.join([f for f in listdir(curr_path) if os.path.exists(join(curr_path, f)) and isfile(join(curr_path, f))])
                else:
                    record.write({'command_directory_list': False})
                    record.command_directory_list = False
                    record.command_directory_list_domain = ''
            elif record.command_directory:
                curr_path = record.command_directory
                
                if os.path.exists(curr_path):
                    record.command_directory_list_domain = ', '.join([f for f in listdir(curr_path) if os.path.exists(join(curr_path, f)) and isfile(join(curr_path, f))])
                else:
                    record.command_directory_list_domain = ''
            else:
                record.command_directory_list_domain = ''
    
    name = fields.Char("Name of server")
    command_directory = fields.Char("Command directory", compute="_curr_directory", default=get_curr_directory, store=False)
    command_directory_list = fields.Selection(_get_directory_list, "Command subdirectory list")
    #commands_list = fields.Selection(_get_commands_list, "Command list")
    command = fields.Char("Command", store=True)
    status = fields.Char('Status', compute="_curr_state")
    status_detailed = fields.Text('Status detailed', compute="_curr_state")
    command_directory_list_domain = fields.Char("Commands list available", compute="_get_commands_list_domain")
    
    #_sql_constraints = [
    #    ('unique_command', 'UNIQUE(command)', 'Command must be unique')
    #]
    
    #@api.onchange('commands_list')
    #def _on_change_commands_list(self):
    #    self.command = self.commands_list
    
    #@api.one
    #@api.depends('commands_list')
    #def _on_compute_commands_list(self):
    #    self.command = self.commands_list
    
    @api.model
    def _curr_directory(self):
        for s in self:
            directory = s.get_curr_directory()
            
            if not directory:
                raise exceptions.UserError(_('Look for the COMMAND_DIRECTORY inside this Odoo Addon path.'))
            
            s.command_directory = directory
    
    @api.model
    def file_command_exists(self):
        if not self.command_directory:
            raise exceptions.UserError(_('Look for the COMMAND_DIRECTORY inside this Odoo Addon path.'))
        
        file_stored = self.command_directory
        
        if self.command_directory_list:
            file_stored = join(file_stored, self.command_directory_list)
        
        if not self.command:
            return False
            #raise exceptions.UserError(_('You must set a command.'))
        
        file_stored = join(file_stored, self.command)
            
        return os.path.isfile(file_stored)
    
    @api.model    
    def get_file_command(self):
        if not self.command_directory:
            raise exceptions.UserError(_('Look for the COMMAND_DIRECTORY inside this Odoo Addon path.'))
        
        file_stored = self.command_directory
        
        if self.command_directory_list:
            file_stored = join(file_stored, self.command_directory_list)
        
        if not self.command:
            raise exceptions.UserError(_('You must set a command.'))
        
        file_stored = join(file_stored, self.command)
            
        return file_stored
    
    @api.model
    def _curr_state(self):
        for s in self:
            if not s.file_command_exists():
                s.status = ""
                s.status_detailed = ""
                return 
                #raise exceptions.UserError(_('Command file doesn\'t exists'))
            
            p = Popen(s.get_file_command() + " status | grep Active", shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
            err = p.stderr.read()
            out = p.stdout.read()
            p.communicate()
            return_val = str(p.wait())
            
            s.status = out
            
            p = Popen(s.get_file_command() + " status", shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
            err = p.stderr.read()
            out = p.stdout.read()
            p.communicate()
            return_val = str(p.wait())
            
            s.status_detailed = out
    
    @api.onchange('name', 'command')
    def _curr_state_change(self):
        if not self.file_command_exists():
            return 
            #raise exceptions.UserError(_('Command file doesn\'t exists'))
            
        p = Popen(self.get_file_command() + " status | grep Active", shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        err = p.stderr.read()
        out = p.stdout.read()
        p.communicate()
        return_val = str(p.wait())
        
        self.status = out
        
        p = Popen(self.get_file_command() + " status", shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        err = p.stderr.read()
        out = p.stdout.read()
        p.communicate()
        return_val = str(p.wait())
        
        self.status_detailed = out
    
    def refresh_service(self):
        self._curr_state_change()
    
    def start_service(self):
        
        if not self.file_command_exists():
            raise exceptions.UserError(_('Command file doesn\'t exists'))
        
        config_admin_id = self.env['config.admin.servers'].search([('user_id', '=', self.env.user.id)])
        
        if len(config_admin_id) == 0:
            raise exceptions.UserError(_('There isn\'t a configuration for this server'))
        
        result = self.env['config.server.list'].search([('config_admin_id', '=', config_admin_id.id), 
                                                        ('server_id', '=', self.id)])
        
        if len(result) == 0:
            raise exceptions.UserError(_('There isn\'t a configuration for this server'))
        
        if not result.can_start:
            raise exceptions.UserError(_('There isn\'t permissions'))
        
        p = Popen("sudo " + self.get_file_command() + " start", shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        err = p.stderr.read()
        out = p.stdout.read()
        p.communicate()
        return_val = str(p.wait())
        
        self.refresh_service()
    
    def stop_service(self):
        if not self.file_command_exists():
            raise exceptions.UserError(_('Command file doesn\'t exists'))
        
        config_admin_id = self.env['config.admin.servers'].search([('user_id', '=', self.env.user.id)])
        
        if len(config_admin_id) == 0:
            raise exceptions.UserError(_('There isn\'t a configuration for this server'))
        
        result = self.env['config.server.list'].search([('config_admin_id', '=', config_admin_id.id), 
                                                        ('server_id', '=', self.id)])
        
        if len(result) == 0:
            raise exceptions.UserError(_('There isn\'t a configuration for this server'))
        
        if not result.can_stop:
            raise exceptions.UserError(_('There isn\'t permissions'))

        p = Popen("sudo " + self.get_file_command() + " stop", shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        err = p.stderr.read()
        out = p.stdout.read()
        p.communicate()
        return_val = str(p.wait())
        
        self.refresh_service()
    
    def restart_service(self):
        if not self.file_command_exists():
            raise exceptions.UserError(_('Command file doesn\'t exists'))
        
        config_admin_id = self.env['config.admin.servers'].search([('user_id', '=', self.env.user.id)])
        
        if len(config_admin_id) == 0:
            raise exceptions.UserError(_('There isn\'t a configuration for this server'))
        
        result = self.env['config.server.list'].search([('config_admin_id', '=', config_admin_id.id), 
                                                        ('server_id', '=', self.id)])
        
        if len(result) == 0:
            raise exceptions.UserError(_('There isn\'t a configuration for this server'))
        
        if not result.can_restart:
            raise exceptions.UserError(_('There isn\'t permissions'))
            
        p = Popen("sudo " + self.get_file_command() + " restart", shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        err = p.stderr.read()
        out = p.stdout.read()
        p.communicate()
        return_val = str(p.wait())
        
        self.refresh_service()
    
    @api.model
    def create(self, vals):
        
        #raise exceptions.UserError(_('Command file doesn\'t exists'))
        admin_user = False
        for g_id in self.env.user.groups_id:
            if g_id.name == "Admin user (Setting servers)":
                admin_user = True
                break
        
        if not admin_user:
            if len(vals.keys()) != 2 or ('status' not in vals.keys() and 'status_detailed' not in vals.keys()):
                raise exceptions.UserError(_('You must be Admin User, contact the System Administrator'))
        
        result = super(ConfigServer, self).create(vals)
        
        if not result.file_command_exists():
            raise exceptions.UserError(_('Command file doesn\'t exists'))
            
        return result
    
    def write(self, vals):
        #raise exceptions.UserError(_('Command file doesn\'t exists'))
        admin_user = False
        for g_id in self.env.user.groups_id:
            if g_id.name == "Admin user (Setting servers)":
                admin_user = True
                break
        
        if not admin_user:
            _logger.info(str(vals.keys()))
            _logger.info(str(len(vals.keys()) != 1 or ('status' not in vals.keys() and 'status_detailed' not in vals.keys())))
            if len(vals.keys()) != 1 or ('status' not in vals.keys() and 'status_detailed' not in vals.keys()):
                raise exceptions.UserError(_('You must be Admin User, contact the System Administrator'))
        
        result = super(ConfigServer, self).write(vals)
        
        #if not self.file_command_exists():
        #    raise exceptions.UserError(_('Command file doesn\'t exists'))
        
        return result
    
    #_sql_constraints = [
    #    ('unique_user_id', 'UNIQUE(user_id)', 'The user must have just one configuration')
    #]

class ConfigServerList(models.Model):
    _name = "config.server.list"
    _description = "Configuration Server List"
    _rec_name = "name"
    
    server_id = fields.Many2one("config.server", "Server")
    config_admin_id = fields.Many2one("config.admin.servers", "Config", compute="_curr_user", store=True)
    name = fields.Char("Name of server", related="server_id.name", store=False)
    command = fields.Char("Command", related="server_id.command", store=False)
    status = fields.Char('Status', related="server_id.status", store=False)
    status_detailed = fields.Text('Status detailed', related="server_id.status_detailed", store=False)
    can_stop = fields.Boolean('Can stop')
    can_start = fields.Boolean('Can start')
    can_restart = fields.Boolean('Can restart')
    
    @api.model
    def _curr_user(self):
        for s in self:
            s.config_admin_id = self.env['config.admin.servers'].search([('user_id', '=', self.env.user.id)])
    
    @api.onchange('server_id')
    def _curr_user_2(self):
        self.config_admin_id = self.env['config.admin.servers'].search([('user_id', '=', self.env.user.id)])
    
    _sql_constraints = [
        ('unique_server_id', 'UNIQUE(server_id,config_admin_id)', 'The user must have only one configuration per Server')
    ]
