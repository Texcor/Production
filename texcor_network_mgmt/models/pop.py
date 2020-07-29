# -*- coding: utf-8 -*-

from odoo import models, fields, api

class POP(models.Model):
    _name = 'pop'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    POP_TYPE = 	[
        ["Main Line","Main Line"],
        ["Lateral","Lateral"],
        ["Network Only","Network Only"]
    ]

    oldid = fields.Integer(string='Old x_model reference')
    
    name = fields.Char(string='POP Name')
    hut_number = fields.Integer(string='Hut Number')
    geo_cooridinates = fields.Char(string='GEO Cooridinates', widget='char')
    pop_type = fields.Selection(POP_TYPE, 'POP Type')

    network_info = fields.One2many(string='Network Info', comodel_name='equipment', inverse_name='pop_id', ondelete='cascade')
    tower_ids = fields.One2many(string='Towers', comodel_name='tower', inverse_name='pop_id', ondelete='cascade')
    circuit_ids = fields.One2many(string='Circuit IDs', comodel_name='circuit', inverse_name='pop_id', ondelete='cascade')
