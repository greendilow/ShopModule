from odoo import fields, models



class Product(models.Model):
    _name = 'Shop Product'
    _description = 'Product'
    id = fields.integer('ID')
    name = fields.Char('Product name')
    price = fields.float('Price')
    weight = fields.float('Weight')
    seller_id = fields.many2one('res.users.id')
