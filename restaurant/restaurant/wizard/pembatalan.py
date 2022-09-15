from odoo import fields, models, api


class pembatalan(models.TransientModel):
    _name = 'restaurant.pembatalan'
    _description = 'Description'

    name = fields.Selection(
        string='Name',
        selection=[('Pesanan_salah', 'Pesanan Salah'),
                   ('lama_menunggu', 'Terlalu Lama Menunggu'),
                   ('driver', 'Driver tidak Merespon'),
                   ('lain_lain', 'Lain-lain'), ],
        required=False, )

    keterangan = fields.Text(string="Keterangan",
                             required=False)


    def action_pembatalan(self):
        for rec in self:
            self.env['restaurant.delivery'].write({'state': 'batal'})
