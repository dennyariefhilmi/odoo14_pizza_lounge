from odoo import fields, models, api


class bahan_makanan(models.Model):
    _name = 'restaurant.bahan_makanan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Description'

    name = fields.Char('Nama Bahan')
    satuan = fields.Selection(string='Satuan',
                              selection=[('kg', 'Kg'),
                                         ('liter', 'Liter'),
                                         ('pack', 'Pack'),
                                         ('ekor', 'Ekor'), ],
                              required=False,
                              tracking=True)
    qty = fields.Integer(string='Kuantitas',
                         required=False,
                         tracking=True)
    tgl_datang = fields.Date(string='Tanggal Datang',
                             required=False,
                             default=fields.Date.today(),
                             tracking=True)
    kadaluarsa = fields.Date(string='Kadaluarsa',
                             required=False,
                             tracking=True)
    harga = fields.Integer(string='Harga',
                           required=False,
                           tracking=True)

    supplier_id = fields.Many2one(comodel_name='restaurant.supplier',
                                  string='Nama Supplier',
                                  required=False,
                                  tracking=True)
