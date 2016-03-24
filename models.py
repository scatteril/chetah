# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title py", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible py", index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions py2")


class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(string="Name py", required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days py")
    seats = fields.Integer(string= "Number of seats py")
    instructor_id = fields.Many2one('res.partner', string="Instructor py", domain=['|', ('instructor', '=', True), ('category_id.name', 'ilike', "Teacher")])
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course py", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees py2")

class School(models.Model):
    _name = 'openacademy.school'

    name = fields.Char(string="Institute name ", required=True)
    responsible_idd = fields.Many2one('res.users', ondelete='set null', string="manager py", index=True)
    phone_number = fields.Integer(string="his phone number py")
