# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Tower(models.Model):
    _name = 'texcor.tower_type'
    
    name = fields.Char(string='Tower Type')
    oldid = fields.Integer(string='Old x_model reference')