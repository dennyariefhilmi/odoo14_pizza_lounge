from odoo import fields, models, api


class menu_makanan(models.Model):
    _name = 'restaurant.menu_makanan'
    _inherit =['mail.thread']
    _description = 'Description'

    name = fields.Char(string='Nama')
    kode_menu = fields.Char(
        string='Kode_menu', 
        required=False)
    tipe = fields.Selection(string='Tipe',
                            selection=[('pizza', 'Pizza'),
                                       ('minuman', 'Minuman'),
                                       ('dessert', 'Dessert'),
                                       ('pasta','Pasta'),],
                            required=False, )
    harga = fields.Integer(string='Harga',
                           required=False)
    deskripsi = fields.Text(string='Deskripsi',
                            required=False,
                            placeholder='Deskripsi...')
    img_makanan = fields.Binary(string="Gambar Makanan")

    # meja_id = fields.Many2one(
    #     comodel_name='restaurant.meja',
    #     string='Meja_id',
    #     required=False)