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

    CIRCUIT_TYPE = [
        ('fiber', 'Fiber'),
        ('wireless', 'Wireless'),
    ]

    name = fields.Char(string='CircuitID')
    circuit_id = fields.Char(string='CircuitID')

    # Circuit Informaiton
    circuit_type = fields.Selection(CIRCUIT_TYPE , 'Circuit Type')

    pop_id = fields.Many2one(string='POP', comodel_name='pop', required=True, ondelete='cascade')
    customer = fields.Many2one(string='Customer', comodel_name='res.partner', required=True, ondelete='cascade')
    location_id = fields.Many2one(string='Service Location', comodel_name='res.partner', ondelete='cascade')

    customer_id = fields.Integer(string='Customer ID', related='customer.id')
    service_order_id = fields.Many2one(string='Service Order', comodel_name='sale.order', ondelete='cascade')
    
    status = fields.Selection(STATUS, 'Status')
    
    qos_id = fields.Many2one(string='QOS', comodel_name='qos', ondelete='cascade')
    vlan_id = fields.Integer(string='VLANID')

    ap_name_id = fields.Many2one(string='AP Name', comodel_name='equipment', invisible='[("circuit_type", "!=", "Wireless")]', ondelete='cascade')
    tower_id = fields.Many2one(string='Tower', comodel_name='tower', related='ap_name_id.tower_id', invisible='[("circuit_type","!=","Wireless")]')
    
    pe_switch_id = fields.Many2one(string='PE Switch', comodel_name='equipment', invisible='[["circuit_type","=","Wireless"]]', ondelete='cascade')
    pe_switch_port = fields.Integer(string='PE Switch Port', help='Enter the Port Number i.e. 1/0/0', invisible='[["circuit_type","=","Wireless"]]')

    # Customer Site Information
    tech_name_id = fields.Many2one(string='Tech Name', comodel_name='res.partner', ondelete='cascade')
    
    tech_phone = fields.Char(string='Tech Phone', related='tech_name_id.phone')
    tech_email = fields.Char(string='Tech Email', related='tech_name_id.email')
    
    address = fields.Char(string='Address', related='customer.street')
    city = fields.Char(string='City', related='location_id.city')
    state = fields.Char(string='State', related='customer.state_id.name', help='Administrative divisions of a country. E.g. Fed. State, Departement, Canton')
    dmarc_location = fields.Char(string='DMARC Location')

    order_line_ids = fields.One2many(string='Order Lines', comodel_name='sale.order.line', related='service_order_id.order_line')
    ip_management_ids = fields.One2many(string='IP Addressing', comodel_name='ip_management', inverse_name='circuit_id', ondelete='cascade')

    # Additional Info
    documents = fields.Binary(string='Test and Turn Up Acceptance')
    notes = fields.Text(string='Notes', widget='text')
    sales_person = fields.Char(string='Sales Person', related='service_order_id.user_id.name')
