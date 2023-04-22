from datetime import date

from odoo import _,models, fields, api
from odoo.exceptions import UserError


class Customer(models.Model):
    _name = "customer.customer"

    customer_id= fields.Integer(string="Customer id")
    first_name= fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    name= fields.Char(string="Name")
    dob = fields.Date(string="DOB")
    # current_date = fields.Date(string="Current Date")
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
    total=fields.Float('Total', compute='price_total')


    _sql_constraints = [
        ('car_id_uniq', 'unique (car_id)', 'The Car Number must be unique !')
    ]

    @api.onchange('first_name', 'last_name')
    def onchange_first_name(self):
        if self.first_name and self.last_name:
            self.name = '{} {}' .format(self.first_name, self.last_name)

    # _sql_constraints = [
    #     ('car_id_uniq', 'unique (car_id)', 'The Car Number must be unique !')
    # ]

    @api.onchange('dob')
    def _onchange_dob(self):
        if self.dob:
           current_date = date.today()
           current_year = current_date.year
           date_of_birth_year = self.dob.year
           self.age = current_year - date_of_birth_year

    @api.constrains('customer_id')
    def constraints_customer_id(self):
        for record in self:
            if self.customer_id < 3:
                raise UserError(_("Customer ID must be in 3 number!"))


    # _sql_constraints = [
    #     ('customer_id_uniq', 'unique (customer_id)', 'The Customer ID must be unique !')
    # ]


