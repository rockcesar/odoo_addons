# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError

import logging

_logger = logging.getLogger(__name__)

class person(models.Model):
    _name = "person"
    _description = "Persona"

    name = fields.Char('Name')
    last_name = fields.Char('Last name')
    age = fields.Integer('Age')
    wallet = fields.Float('Wallet')
    sex = fields.Selection([
                            ('male', 'Male'),
                            ('female', 'Female'),],
                            string='Sex', default='male')
    houses_ids = fields.Many2many(
        comodel_name='house',
        relation='person_house_rel',
        column1='person_id',
        column2='house_id',
        string=u'Houses of the person',
        help=u'Houses of the person'
    )
    car_ids = fields.One2many(
        comodel_name='car',
        inverse_name='person_id',
        string=u'Cars',
        help=u'Cars of the person'
    )
    photo = fields.Binary(
                string=u'Photo of the person',
                required=False
    )
    photo_litle = fields.Binary(string='Photo of the person',
                                compute="_compute_photo_depends",
                                store=False)
    first_module_onboarding_car_state = fields.Selection([('option1', 'Option1'), ('option2', 'Option2')], string="Options")
    
    @api.depends('photo')
    def _compute_photo_depends(self):
        for person in self:
            if person.photo:
                person.photo_litle = person.photo
            else:
                person.photo_litle = False

    @api.model
    def create(self, vals):
        person_id = super(person, self).create(vals)

        return person_id
    
    def write(self, vals):
        if 'houses_ids' in vals:
            house_obj = self.env['house']
            _logger.info("Self " + str(vals['houses_ids']))
            house_ids = house_obj.search([('id', 'in', vals['houses_ids'][0][2])])
            _logger.info("Houses " + str(house_ids))
            house_result = house_obj.browse(vals['houses_ids'][0][2])
            _logger.info("House result " + str(house_result))
            house_read = house_obj.search_read([('id', 'in', vals['houses_ids'][0][2])], ['id','description'])
            _logger.info("House read " + str(house_read))

        result = super(person, self).write(vals)

        return result
    
    def unlink(self):
        unlink_result = super(person, self).unlink()
        
        return unlink_result
    
    @api.model
    def action_button_1(self):
        action = self.env["ir.actions.actions"]._for_xml_id("first_module.car_onboarding_action")
        #return action
        car = self.env['car'].search([], limit=1)
        if len(car) > 0:
            action.update({'res_id': car[0].id})
        
        _logger.info(str(action))
        
        return action
        
        """
        return {'type': 'ir.actions.act_window',
               'name': _('Mark as Done'),
               'res_model': 'car',
               'target': 'new',
               'view_id': self.env.ref('first_module.car_view_form').id,
               'view_mode': 'form',
               #'context': {'default_person_id': self.id}
               }
        """
    
    @api.model
    def action_button_2(self):
        return {'type': 'ir.actions.act_window',
               'name': _('Mark as Done'),
               'res_model': 'car',
               'target': 'new',
               'view_id': self.env.ref('first_module.car_view_form').id,
               'view_mode': 'form',
               #'context': {'default_person_id': self.id}
               }
