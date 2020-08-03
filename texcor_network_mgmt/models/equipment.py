# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Equipment(models.Model):
    _name = 'texcor.equipment'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    MANUFACTURER = [
        ('Moxa', 'Moxa'),
        ('Cisco', 'Cisco'),
        ('Cambium', 'Cambium'),
        ('Palo Alto', 'Palo Alto'),
    ]

    MODEL = 	[
        ["PA-850","PA-850"],
        ["WS-C3650-24TS-L","WS-C3650-24TS-L"],
        ["ICS-G7826A-20GSFP-4GTXSFP-2XG-HV-HV","ICS-G7826A-20GSFP-4GTXSFP-2XG-HV-HV"],
        ["EDS-P506E-4PoE-2GTXSFP-T","EDS-P506E-4PoE-2GTXSFP-T"],
        ["ePMP 1000","ePMP 1000"]
    ]

    DEVICE_TYPE = [
        ["Backbone","Backbone"],
        ["Wireless PTP","Wireless PTP"],
        ["Wireless PTMP","Wireless PTMP"],
        ["L2 Switch","L2 Switch"],
        ["Edge","Edge"]
    ]

    MODULE_MODE = 	[
        ["ePTP Master","ePTP Master"],
        ["ePTP Slave","ePTP Slave"],
        ["AP","AP"]
    ]
    
    oldid = fields.Integer(string='Old x_model reference')

    name = fields.Char(string='DNS Hostname')
    serial_number = fields.Char(string='Serial Number')
    mac_address = fields.Char(string='Eth Mac Address')
    firmware_version = fields.Char(string='Firmware Version')

    in_service = fields.Boolean(string='In Service')
    cpe_device = fields.Boolean(string='CPE Device')
    number_of_ports = fields.Integer(string='Number of Ports')

    model = fields.Selection(MODEL, 'Model')
    device_type = fields.Selection(DEVICE_TYPE, 'Device Type')
    manufacturer = fields.Selection(MANUFACTURER, 'Manufacturer')
    
    ip_management_id = fields.Many2one(string='Management IP', comodel_name='texcor.ip_management', ondelete='cascade')
    pop_id = fields.Many2one(string='POP', comodel_name='texcor.pop', ondelete='cascade')
    circuit_ids = fields.One2many(string='Circuit IDs', comodel_name='texcor.circuit', inverse_name='ap_name_id', ondelete='cascade')
    tower_id = fields.Many2one(string='Tower', comodel_name='texcor.tower', ondelete='cascade')
    wireless_ssid = fields.Char(string='Wireless SSID')
    wireless_mac = fields.Char(string='Wireless MAC')
    module_mode = fields.Selection(MODULE_MODE, 'Wireless Module Mode')
