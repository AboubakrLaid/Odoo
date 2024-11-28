from odoo import models, fields

class Category(models.Model):
    _name = 'services.category'
    _description = 'Service Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')

class Service(models.Model):
    _name = 'services.service'
    _description = 'Service'

    name = fields.Char(string='Service Name', required=True)
    description = fields.Text(string='Description')
    category_id = fields.Many2one('services.category', string='Category')
    price = fields.Float(string='Price')
