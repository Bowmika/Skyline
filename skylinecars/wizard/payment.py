from odoo import fields, models


class PaymentWizard(models.TransientModel):
    _name =  'payment.payment'
    _description = 'Payment'

    name = fields.Char('Name')
    amount = fields.Float(string='Amount')
    tax = fields.Float(string='Tax')


    def create_payments(self):
        worker_id = self.env.context.get('active_id')
        print ('bbbbbbbbbbbbbbbbbbbbbbbb', worker_id)

        discount = self.env['discount.discount'].create({
                'name': self.name,
                'amount': self.amount,
                'tax': self.tax
            })

    # def create_payments(self):
    #     customer_id = self.env.context.get('active_id')
    #     print('uuuuuuuuuuuuuuuuuu', customer_id)
    #     car = self.env['discount.discount'].browse(customer_id)
    #     car.write({
    #         'car': [
    #             (0, 0, {'car_ids': 7, 'price': 100}),
    #         ]
    #     })

    # class calculation(models.Model):
    #     _name = 'calculation.calculation'
    #
    #     name = fields.Many2one('payment.payment', string='Name')
    #     customer_id = fields.Many2one(
    #         'billing.billing',
    #         string="Customer_id"
    #     )





