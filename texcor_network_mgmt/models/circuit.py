# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Circuit(models.Model):
    _name = 'circuit'

    STATUS = [
        ('preturnup', 'Pre-Turnup'),
        ('circuitActive', 'Active'),
        ('maintenance', 'Maintenance'),
        ('testturnup', 'Test & Turnup'),
    ]

    name = fields.Char(string='CircuitID')
    circuit_id = fields.Char(string='CircuitID')
    status = fields.Selection(STATUS, 'Status')

    pop_id = fields.Many2one(string='POP', comodel_name='pop', ondelete='cascade')
    sale_order_id = fields.Many2one(string='Service Order', comodel_name='sale.order', ondelete='cascade')

    customer_id = fields.Many2one(string='Customer', comodel_name='res.partner', ondelete='cascade')
    location_id = fields.Many2one(string='Service Location', comodel_name='res.partner', ondelete='cascade')
