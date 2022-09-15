from odoo import fields, models, api, _


class antrian(models.Model):
    _name = 'restaurant.antrian'
    _description = 'Description'

    name = fields.Char('Atas Nama')
    qty = fields.Integer(string='Jumlah Orang',
                         required=False)

    jam_datang = fields.Datetime(string='Jam Datang',
                                 required=False,
                                 default=fields.Datetime.now())

    no_hp = fields.Char(
        string='No HP',
        required=False)

    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('Antrian'))

    # membuat sequence nomor antrian
    @api.model
    def create(self, vals):
        if vals.get('reference', _('Antrian')) == _('Antrian'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('restaurant.antrian') or _('Antrian')
        res = super(antrian, self).create(vals)
        return res

