from odoo import fields, models, api


class orderdetail(models.Model):
    _name = 'restaurant.orderdetail'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Description'







