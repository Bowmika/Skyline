from odoo import models, fields, api

class Vehicle(models.Model):
    _name = "vehicle.vehicle"

    @api.model
    def _default_user(self):
        return self.env.user.id

    cars = fields.Selection([  ('ford', 'Ford'),
         ('shift', 'Shift'),
         ('honda', 'Honda'),
         ('bmw', 'Bmw'),
         ('shift', 'Shift'),
         ('lexus','Lexus'),
         ('kia','Kia'),
         ('jeep','Jeep'),
         ('acura', 'Acura'),
         ('audi', 'audi'),
        ], 'Cars'
     )

    seater= fields.Selection([  ('4', '4'),
         ('5', '5'),
         ('7', '7'),
         ('8', '8'),
          ], 'Seater'
      )
    fuel= fields.Selection([ ('petrol', 'petrol'),
         ('diesel', 'diesel'),
        ],  'fuel'
     )
    customer_details = fields.One2many('customer.customer', 'car_id', string='Customer Details')
    customer_id = fields.Many2one('customer.customer',string='Customer id')
    user_id = fields.Many2one('res.users', string='User', default=_default_user)

    # @api.model
    # def create(self, vals):
    #     print('bbbbbbbbbb', vals)
    #     vals['name'] = 'Honda'
    #     return super(Vehicle,self).create(vals)
