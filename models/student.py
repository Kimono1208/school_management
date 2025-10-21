from odoo import fields, models

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student Information'
    
    name = fields.Char(string='Name', required=True)                     # Char 
    age = fields.Integer(string='Age')                                  # Integer 
    birth_date = fields.Date(string='Date of Birth')                    # Date 
    email = fields.Char(string='Email')                                 # Char 
    active = fields.Boolean(string='Active', default=True)              # Boolean, por defecto True