# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Circuits(models.Model):
    _name = 'ip_management'

    CIDR = [
        ('/18', '/18'),
        ('/19', '/19'),
        ('/20', '/20'),
        ('/21', '/21'),
        ('/22', '/22'),
        ('/23', '/23'),
        ('/24', '/24'),
        ('/25', '/25'),
        ('/26', '/26'),
        ('/27', '/27'),
        ('/28', '/28'),
        ('/29', '/29'),
        ('/30', '/30'),
    ]

    name = fields.Char(string='Network')
    network_ip = fields.Char(string='Network')
    gateway_ip = fields.Char(string='Gateway IP')
    status = fields.Selection(CIDR, 'CIDR')

    parent_network = fields.Boolean(string='Parent Network')
    internal_use = fields.Boolean(string='Internal Use')

    circuit_id = fields.Many2one(string='Circuit IDs', comodel_name='circuit', ondelete='cascade')
    location_id = fields.Many2one(string='Service Location', comodel_name='res.partner', ondelete='cascade')
    