from odoo import fields, models, api


class bahan_makanan(models.Model):
    _name = 'restaurant.bahan_makanan'
    _description = 'Description'

    name = fields.Char('Nama Bahan')
    satuan = fields.Selection(
        string='Satuan',
        selection=[('kg', 'Kg'),
                   ('liter', 'Liter'),
                   ('pack','Pack'),
                   ('ekor','Ekor'),],
        required=False, )
    qty = fields.Integer(string='Kuantitas',
                         required=False)
    tgl_datang = fields.Date(string='Tanggal Datang',
                             required=False,
                             default=fields.Date.today())
    kadaluarsa = fields.Date(string='Kadaluarsa',
                             required=False,
                             )
    harga = fields.Integer(string='Harga',
                           required=False)

    supplier_id = fields.Many2one(
        comodel_name='restaurant.supplier',
        string='Nama Supplier',
        required=False)

