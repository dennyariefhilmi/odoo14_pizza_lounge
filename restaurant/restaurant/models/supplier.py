from odoo import fields, models, api


class supplier(models.Model):
    _name = 'restaurant.supplier'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Description'

    name = fields.Char('Nama Supplier', tracking=True)
    keterangan = fields.Selection(string='Keterangan',
                                  selection=[('supplier_alat_masak', 'Supplier Alat Masak'),
                                             ('supplier_alat_makan', 'Supplier Alat Makan'),
                                             ('supplier_pertanian', 'Supplier Pertanian'),
                                             ('supplier_peternakan', 'Supplier Peternakan'),
                                             ('supplier_seafood', 'Supplier Seafood'),],
                                  required=False, tracking=True)

    alamat = fields.Char(string='Alamat', required=False, tracking=True)
    negara = fields.Many2one('res.country', string="Negara", tracking=True)
    provinsi = fields.Many2one('res.country.state', string="Provinsi", store=True, tracking=True)
    # kota = fields.Many2one('res.city', string="Kota", store=True)
    kota = fields.Char(
        string='Kota',
        required=False, tracking=True)
    bahan_id = fields.One2many(
        comodel_name='restaurant.bahan_makanan',
        inverse_name='supplier_id',
        string='Bahan_id',
        required=False, tracking=True)

    # bahan_id = fields.Many2one(
    #     comodel_name='restaurant.bahan_makanan',
    #     string='bahan_makanan_id',
    #     required=False)
    # harga = fields.Integer(
    #     string='Harga',
    #     required=False)
    # satuan_ids = fields.Many2one(
    #     comodel_name='restaurant.bahan_makanan',
    #     string='satuan_id',
    #     required=False)

    @api.onchange('negara', 'provinsi')
    def set_values_to(self):
        if self.negara:
            ids = self.env['res.country.state'].search([('country_id', '=', self.negara.id)])
            return {
                'domain': {'provinsi': [('id', 'in', ids.ids)], }
            }

    # @api.onchange('provinsi')
    # def set_values_to(self):
    #     if self.provinsi:
    #         ids = self.env['res.city'].search([('name', '=', self.provinsi.id)])
    #         return {
    #             'domain': {'kota': [('id', 'in', ids.ids)], }
    #         }
