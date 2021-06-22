from odoo import fields, models


class Client(models.Model):
    _name = 'Shop Client'
    _description = 'Client'
    id = fields.integer('ID')
    role = fields.many2many('roles.id')
    info = fields.Char('Name, Phone')
