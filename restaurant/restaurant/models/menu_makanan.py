from odoo import fields, models, api


class menu_makanan(models.Model):
    _name = 'restaurant.menu_makanan'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Description'

    name = fields.Char(string='Nama', tracking=True)
    kode_menu = fields.Char(
        string='Kode_menu',
        required=False, tracking=True)
    tipe = fields.Selection(string='Tipe',
                            selection=[('pizza', 'Pizza'),
                                       ('minuman', 'Minuman'),
                                       ('dessert', 'Dessert'),
                                       ('pasta', 'Pasta'), ],
                            required=False, tracking=True)
    harga = fields.Integer(string='Harga',
                           required=False, tracking=True)
    deskripsi = fields.Text(string='Deskripsi',
                            required=False,
                            placeholder='Deskripsi...',
                            tracking=True)
    img_makanan = fields.Binary(string="Gambar Makanan", tracking=True)

    # meja_id = fields.Many2one(
    #     comodel_name='restaurant.meja',
    #     string='Meja_id',
    #     required=False)
