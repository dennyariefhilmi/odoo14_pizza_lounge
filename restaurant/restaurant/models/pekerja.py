from odoo import fields, models, api


class pekerja(models.Model):
    _name = 'restaurant.pekerja'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Description'

    name = fields.Char("Nama")
    mulai_bekerja = fields.Date(string='Mulai Bekerja',
                                required=False, tracking=True)
    no_hp = fields.Char(string='No HP',
                           required=False, tracking=True)
    alamat = fields.Char(
        string='Alamat',
        required=False, tracking=True)
    role = fields.Selection(
        string='Role',
        selection=[('manajer', 'Manajer'),
                   ('supervisor','Supervisor'),
                   ('kitchen_staff', 'Kitchen Staff'),
                   ('pramusaji','Pramusaji'),
                   ('kasir','Kasir'),
                   ('driver','Driver')],
        required=False, tracking=True)
    usia = fields.Integer(
        string='Usia',
        required=False, tracking=True)
    jadwal_ids = fields.One2many(
        comodel_name='restaurant.jadwal',
        inverse_name='jadwal_shift',
        string='Jadwal_ids',
        required=False, tracking=True)
    shift = fields.Selection(string='Shift',
                             selection=[('shift_1', 'Shift 1'),
                                        ('shift_2', 'Shift 2'),
                                        ('libur', 'Libur')],
                             required=False, tracking=True)



