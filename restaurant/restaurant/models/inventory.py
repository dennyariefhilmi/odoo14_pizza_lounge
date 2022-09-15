from odoo import fields, models, api


class inventory(models.Model):
    _name = 'restaurant.inventory'
    _description = 'Description'

    name = fields.Char('Nama Alat')
    kuantitas = fields.Integer(string='Kuantitas',
                               required=False)
    jenis = fields.Selection(string='Jenis',
                             selection=[('alat_makan', 'Alat Makan'),
                                        ('alat_masak', 'Alat Masak'), ],
                             required=False, )




