from odoo import models, fields


class Student(models.Model):
    _name = "student.student"

    name = fields.Char(string="Name")
    roll_no = fields.Integer(string="Roll No")
    age = fields.Integer(string="Age")
    dob= fields.Date("Student date of birth")
    present = fields.Integer(string="Present")
    absent = fields.Integer(string="Absent")
    teacher_id = fields.Many2one('teacher.teacher', string="Teacher id")
    image = fields.Image(string= 'Image')