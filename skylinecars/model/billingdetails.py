from odoo import models, fields


class Customer(models.Model):
    _name = "billing.billing"

    customer_id= fields.Integer(string="Customer id")
    pay_on_delivery= fields.Boolean(string="Pay on Delivery")
    upi= fields.Boolean(string="UPI")
    debit = fields.Boolean(string="Debit")
    credit = fields.Boolean(string="Credit")
    billing_method = fields.Selection([('pay_on_delivery','Pay On Delivery'),
                                ('upi','UPI'),
                                ('debit','Debit'),
                                ('credit','credit')
                                       ],'Billing Method')

class CustomerDetails(models.Model):
    _name = "customer.details"

    customer_id = fields.Many2one('customer.customer',string="Customer")
