from odoo import fields, models, api


class inventory(models.Model):
    _name = 'restaurant.inventory'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Description'

    name = fields.Char('Nama Alat',
                       tracking=True)
    kuantitas = fields.Integer(string='Kuantitas',
                               required=False,
                               tracking=True)
    jenis = fields.Selection(string='Jenis',
                             selection=[('alat_makan', 'Alat Makan'),
                                        ('alat_masak', 'Alat Masak'), ],
                             required=False, tracking = True)
