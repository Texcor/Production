# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tower(models.Model):
    _name = 'towers'

    ARRAY_TYPE = [
        ('ptp', 'PTP'),
        ('ptmp', 'PTMP'),
    ]

    name = fields.Char(string='Name')
    pop_id = fields.Many2one(string='POP', comodel_name='x_pop', inverse_name='pop_id', ondelete='cascade')
    array_type = fields.Selection(ARRAY_TYPE, 'Array Type')