from odoo import fields, models, api


class Jadwal(models.Model):
    _name = 'restaurant.jadwal'
    _description = 'Description'

    name = fields.Many2one(comodel_name='restaurant.pekerja',
                           string='Name',
                           required=False)

    role = fields.Many2one(comodel_name='restaurant.pekerja',
                           string='Role',
                           required=False)

    senin = fields.Selection(string='Senin',
                             selection=[('shift_1', 'Shift 1'),
                                        ('shift_2', 'Shift 2'),
                                        ('libur', 'Libur')],
                             required=False)
    selasa = fields.Selection(string='Selasa',
                              selection=[('shift_1', 'Shift 1'),
                                         ('shift_2', 'Shift 2'),
                                         ('libur', 'Libur')],
                              required=False)
    rabu = fields.Selection(string='Rabu',
                            selection=[('shift_1', 'Shift 1'),
                                       ('shift_2', 'Shift 2'),
                                       ('libur', 'Libur')],
                            required=False)
    kamis = fields.Selection(string='Kamis',
                             selection=[('shift_1', 'Shift 1'),
                                        ('shift_2', 'Shift 2'),
                                        ('libur', 'Libur')],
                             required=False)
    jumat = fields.Selection(string='Jumat',
                             selection=[('shift_1', 'Shift 1'),
                                        ('shift_2', 'Shift 2'),
                                        ('libur', 'Libur')],
                             required=False)
    sabtu = fields.Selection(string='Sabtu',
                             selection=[('shift_1', 'Shift 1'),
                                        ('shift_2', 'Shift 2'),
                                        ('libur', 'Libur')],
                             required=False)
    minggu = fields.Selection(string='Minggu',
                              selection=[('shift_1', 'Shift 1'),
                                         ('shift_2', 'Shift 2'),
                                         ('libur', 'Libur')],
                              required=False)
    jadwal_shift = fields.Many2one(
        comodel_name='restaurant.pekerja',
        string='Jadwal_shift',
        required=False)
