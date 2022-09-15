from odoo import fields, models, api, _


class order(models.Model):
    _name = 'restaurant.order'
    _description = 'Description'

    name = fields.Selection(
        string='Name',
        selection=[('table_1', 'Table 1'),
                   ('table_2', 'Table 2'),
                   ('table_3', 'Table 3'),
                   ('table_4', 'Table 4'),
                   ('table_5', 'Table 5'),
                   ('table_6', 'Table 6'),
                   ('table_7', 'Table 7'),
                   ('table_8', 'Table 8'),
                   ('table_9', 'Table 9'),
                   ('table_10', 'Table 10'),
                   ],
        required=False, )

    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('Order ID :'))


    kapasitas = fields.Selection(string='Kapasitas',
                                 selection=[('2', '2'),
                                            ('4', '4'),
                                            ('8', '8'),],
                                 required=False,)
    status = fields.Selection(string='Status',
                              selection=[('kosong', 'Kosong'),
                                         ('terisi', 'Terisi'),
                                         ('reservasi','Reservasi')],
                              required=False,)
    jam_mulai = fields.Datetime(string='Jam Mulai',
                                required=False,
                                default=fields.Datetime.now())
    # menu_id = fields.One2many(
    #     comodel_name='restaurant.menu_makanan',
    #     inverse_name='meja_id',
    #     string='Order_id',
    #     required=False)

    menu_id = fields.Many2one(
        comodel_name='restaurant.menu_makanan',
        string='Menu_',
        required=False)

    #membuat sequence nomor order
    @api.model
    def create(self, vals):
        if vals.get('reference', _('Order ID :')) == _('Order ID :'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('restaurant.order') or _('Order ID :')
        res = super(order, self).create(vals)
        return res


