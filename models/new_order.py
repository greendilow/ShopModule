from odoo import fields, models


class Order(models.Model):
    _name = 'Shop Order'
    _description = 'Order'
    id = fields.integer('ID')
    product_id = fields.many2many('product.id')
    client_info = fields.many2one('client.info')
    price_id = fields.integer('Bill')
    
