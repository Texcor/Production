# -*- coding: utf-8 -*-

from odoo import models, fields, api

class QOS(models.Model):
    _name = 'qos'
    
    name = fields.Char(string='Name')
    oldid = fields.Integer(string='Old x_model reference')
    