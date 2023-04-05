from odoo import models, fields

class Vehicle(models.Model):
    _name = "vehicle.vehicle"

    name= fields.Integer(string="Car name")
    price= fields.Char(string="Price")
    color = fields.Char(string="Color")
    car_number = fields.Char(string="Car number")
    seater = fields.Char(string='Seater')
    customer_details = fields.One2many('customer.customer', 'car_id', string='Customer Details')
    customer_id = fields.Many2one('customer.customer',string='Customer id')




