# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tower(models.Model):
    _name = 'tower'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    ARRAY_TYPE = [
        ["PTP","PTP"],
        ["PTMP","PTMP"],
    ]

    WIRELESS_FREQUENCY = 	[
        ["3.6Ghz","3.6Ghz"],
        ["5.8Ghz","5.8Ghz"]
    ]

    oldid = fields.Integer(string='Old x_model reference')

    name = fields.Char(string='Name')

    # Tower info
    tower_type_id = fields.Many2one(string='Tower Type', comodel_name='tower_type', ondelete='cascade')
    pop_id = fields.Many2one(string='POP', comodel_name='pop', ondelete='cascade')
    geo_location = fields.Char(string='Geo Location')
    tower_height = fields.Integer(string='Tower Height (in ft)')

    # Wireless info
    array_type = fields.Selection(ARRAY_TYPE, 'Array Type')
    wireless_frequency = fields.Selection(WIRELESS_FREQUENCY, 'Wireless Frequency')
    array_height = fields.Integer(string='Array Height (in ft)')

    # Network info
    ap_name_id = fields.Many2one(string='AP Name', comodel_name='equipment', ondelete='cascade')
    circuit_ids = fields.One2many(string='Circuit IDs', comodel_name='circuit', inverse_name='tower_id', ondelete='cascade')

    # Sector 1
    sector_1 = fields.Char(string='Sector 1')
    h_azimuth_1 = fields.Char(string='H Azimuth')
    v_azimuth_1 = fields.Char(string='V Azimuth')

    # Sector 2
    sector_2 = fields.Char(string='Sector 2')
    h_azimuth_2 = fields.Char(string='H Azimuth')
    v_azimuth_2 = fields.Char(string='V Azimuth')

    # Sector 3
    sector_3 = fields.Char(string='Sector 3')
    h_azimuth_3 = fields.Char(string='H Azimuth')
    v_azimuth_3 = fields.Char(string='V Azimuth')

    # Sector 4
    sector_4 = fields.Char(string='Sector 4')
    h_azimuth_4 = fields.Char(string='H Azimuth')
    v_azimuth_4 = fields.Char(string='V Azimuth')

    circuits_ids = fields.Many2many(string='Circuits IDs', comodel_name='circuit', relation='texcor_circuits_towers', ondelete='cascade')