from odoo import models, fields, api
from datetime import datetime,date


class Customer(models.Model):
    _name = "customer.customer"

    customer_id= fields.Integer(string="Customer id")
    first_name= fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    name= fields.Char(string="Name")
    dob = fields.Date(string="DOB")
    current_date = fields.Date(string="Current Date")
    age = fields.Integer(string="Age")
    phone_no = fields.Char(string="Phone no")
    email_id = fields.Char(string="Email_id")
    address = fields.Char(string='Address')
    flat_no= fields.Char(string="Flat_no")
    area= fields.Char(string="Area")
    city = fields.Char(string="City")
    pin_no = fields.Char(string="Pin_no")
    image = fields.Image(string='Image')
    car_detail_ids= fields.Many2many('vehicle.vehicle', string="Car_details")
    car_id = fields.Many2one('vehicle.vehicle',string="Car")

@api.onchange('first_name', 'last_name')
def onchange_first_name(self):
    if self.first_name and self.last_name:
        self.name = '{} {}' .format(self.first_name, self.last_name)

    @api.onchange('dob')
    def _onchange_dob(self):
        current_date = date.today()
        current_year = current_date.year
        date_of_birth_year = self.dob.year
    # if self.date_of_birth:
        self.age = current_year - date_of_birth_year

