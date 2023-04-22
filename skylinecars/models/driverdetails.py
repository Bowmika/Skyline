from datetime import date

from odoo import _, models,fields, api
from odoo.exceptions import UserError


class DriverDetails(models.Model):
    _name = 'driver.driver'

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    name = fields.Char(string='Employee Name')
    phone_number = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    driver_id = fields.Char(string='Driver Id')
    address = fields.Char(string='Address')
    image = fields.Image(string='Images')
    date_of_birth = fields.Date(string='DOB')
    age = fields.Integer(string='Age')
    driver_details= fields.Char(string='Driver_Details')

    _sql_constraints = [
        ('driver_id_uniq', 'unique (driver_id)', 'The Driver Id must be unique !')
    ]

    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, '%s (%s)' % (record.date_of_birth, record.name)))
        return res

    @api.onchange('first_name', 'last_name')
    def onchange_first_name(self):
        if self.first_name and self.last_name:
            self.name = '{} {}'.format(self.first_name, self.last_name)

    @api.onchange('date_of_birth')
    def _onchange_dob(self):
        if self.date_of_birth:
            current_date = date.today()
            current_year = current_date.year
            date_of_birth_year = self.date_of_birth.year
            self.age = current_year - date_of_birth_year

    @api.constrains('driver_id')
    def _constraints_driver_id(self):
        for record in self:
            if self.age < 18:
                raise UserError(_("Driver Age must be above 25!"))

    # def write(self, vals):
    #     vals = self.set_driver_details(vals)
    #     res = super(DriverDetails, self).write(vals)
    #     return res

