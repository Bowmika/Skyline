from odoo import fields, models


class SubjectInfo(models.Model):
    _name = "subject.subject"

    name = fields.Char(string="Subject")
    teacher_id = fields.Many2one('teacher.teacher', string='Teacher')
