# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EquipmentTable(models.Model):
    _name = 'equipment_table'

    manufacturer = fields.Char(string='Manufacturer')
    model  = fields.Char(string='Model')
    l3_capable = fields.Boolean(string='L3 Capable')
    type_name = fields.Char(string='Type')

    l2_capable = fields.Boolean(string='L2 Capable')
    class_name = fields.Char(string='Class')
    name = fields.Char(string='Name')
    