from odoo import models,fields

class Discount(models.Model):
    _name = 'discount.discount'

    name = fields.Char('Name')
    customer_ids = fields.Char('customer_ids')
    amount = fields.Float(string='Amount')
    tax = fields.Float(string='Tax')
    discount = fields.Selection([('14% off', '14% Off'),
                             ('35% off', '35% Off'),
                             ('70% off', '70% Off')
                             ], 'discount'
                            )

    cars = fields.Selection([('ford', 'Ford'),
                             ('shift', 'Shift'),
                             ('honda', 'Honda'),
                             ('bmw', 'Bmw'),
                             ('shift', 'Shift'),
                             ('lexus', 'Lexus'),
                             ('kia', 'Kia'),
                             ('jeep', 'Jeep'),
                             ('acura', 'Acura'),
                             ('audi', 'audi')
                             ], 'Category'
                            )

    seater = fields.Selection([('4', '4'),
                               ('5', '5'),
                               ('7', '7'),
                               ('8', '8')
                               ], 'Seater'
                              )
    fuel = fields.Selection([('petrol', 'Petrol'),
                              ('diesel', 'Diesel')
                              ], 'Fuel'
                             )
    discount_ids = fields.One2many('discount.details', 'car_id', string='Discount Details')


class DiscountDetails(models.Model):
    _name = 'discount.details'

    car_id = fields.Many2one('discount.discount',string='Car')

