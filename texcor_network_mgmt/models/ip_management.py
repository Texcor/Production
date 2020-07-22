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

    AVAILABILITY = [
        ('assigned', 'Assigned'),
        ('reserved', 'Reserved'),
        ('available', 'Available'),
    ]

    name = fields.Char(string='Network')
    
    net_mask = fields.Char(string='Net Mask')
    network_ip = fields.Char(string='Network')
    provider_ip = fields.Char(string='Gateway IP')
    network_address = fields.Char(string='Network Address')

    cidr = fields.Selection(CIDR, 'CIDR')
    availability = fields.Selection(AVAILABILITY, 'Availability')

    management_ip = fields.Boolean(string='Management IP')
    parent_network = fields.Boolean(string='Parent Network')
    internal_use = fields.Boolean(string='Internal Use')

    equipment_id = fields.Many2one(string='Equipment', comodel_name='equipment', ondelete='cascade')
    circuit_id = fields.Many2one(string='Circuit IDs', comodel_name='circuit', ondelete='cascade')
    location_id = fields.Many2one(string='Service Location', comodel_name='res.partner', ondelete='cascade')
    
    description = fields.Text(string='Description')
    network_cidr = fields.Char(string='Network Address/CIDR')

    @api.depends('cidr', 'network_address')
    def _compute_network_cidr(self):
        if self.cidr == False:
            cidr = str("/??")
        for record in self:
            if self.cidr == False:
                cidr = str("/??")
            else:
                cidr = str(record.cidr)
                record['network_cidr'] = str(record.network_address + cidr)