from odoo import models, fields

class Suggestion(models.Model):
    _name = "suggestion.suggestion"

    suggestion= fields.Text(string="Suggestion")



