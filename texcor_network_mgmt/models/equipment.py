# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Equipment(models.Model):
    _name = 'equipment'

    MANUFACTURER = [
        ('moxa', 'Moxa'),
        ('cisco', 'Cisco'),
        ('cambium', 'Cambium'),
        ('paloalto', 'Palo Alto'),
    ]

    MODEL = [
        ('PA-850', 'PA-850'),
        ('ePMP 1000', 'ePMP 1000'),
        ('WS-C3650-24TS-L', 'WS-C3650-24TS-L'),
        ('EDS-P506E-4PoE-2GTXSFP-T', 'EDS-P506E-4PoE-2GTXSFP-T'),
        ('ICS-G7826A-20GSFP-4GTXSFP-2XG-HV-HV', 'ICS-G7826A-20GSFP-4GTXSFP-2XG-HV-HV'),
    ]

    name = fields.Char(string='DNS Hostname')
    in_service = fields.Boolean(string='In Service')
    serial_number = fields.Char(string='Serial Number')

    model  = fields.Selection(MODEL, 'Model')
    manufacturer = fields.Selection(MANUFACTURER, 'Manufacturer')
    
    ip_management_id = fields.Many2one(string='Management IP', comodel_name='ip_management', ondelete='cascade')
    pop_id = fields.Many2one(string='POP', comodel_name='pop', ondelete='cascade')
