# -*- coding: utf-8 -*-

from odoo import models, fields, api

class POP(models.Model):
    _name = 'pop'

    POP_TYPE = [
        ('lateral', 'Lateral'),
        ('mainline', 'Main Line'),
        ('networkonly', 'Network Only'),
    ]

    name = fields.Char(string='POP Name')
    geo_cooridinates = fields.Char(string='GEO Cooridinates')
    pop_type = fields.Selection(POP_TYPE, 'POP Type')

    tower_id = fields.One2many(string='Towers', comodel_name='towers', inverse_name='pop_id', ondelete='cascade')
    circuit_ids = fields.One2many(string='Circuit IDs', comodel_name='circuit', inverse_name='pop_id', ondelete='cascade')
