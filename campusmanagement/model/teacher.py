from odoo import models, fields


class Teacher(models.Model):
    _name = "teacher.teacher"

    name = fields.Char(string="Name")
    employee_id= fields.Integer(string="Employee id")
    dob = fields.Date(string="DOB")
    age = fields.Integer(string="Age")
    present= fields.Integer(string="Present")
    absent= fields.Integer(string="Absent")
    meeting_start = fields.Datetime(string="Meeting Start")
    meeting_end = fields.Datetime(string="meeting End")
    student_details = fields.One2many('student.details', 'teacher_id', string='Student Details')


class StudentDetails(models.Model):
    _name="student.details"

    teacher_id = fields.Many2one('teacher.teacher', string='Teacher')
    student_id = fields.Many2one('student.student', string='Student',domain="[('teacher_id','=',teacher_id)]")
    teacher_emp = fields.Integer(related='teacher_id.employee_id', string='Teacher emp')
    subject_ids = fields .Many2many('subject.subject', string='Subject')
