from odoo import fields, models, api, _


class Delivery(models.Model):
    _name = 'restaurant.delivery'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Description'

    name = fields.Char('Nama Pemesan')
    driver_id = fields.Many2one(comodel_name='restaurant.pekerja',
                                string='Driver_id',
                                domain=[('role', '=', 'driver')],
                                required=False,
                                tracking=True)

    state = fields.Selection(string='Status',
                             selection=[('pesanan', 'Pesanan'),
                                        ('diantar', 'Diantar'),
                                        ('selesai', 'Selesai'),
                                        ('batal', 'Batal'),],
                             required=True, default='pesanan',
                             tracking=True)

    reference = fields.Char(string='Order ID', required=True, copy=False, readonly=True,
                            default=lambda self: _('Order ID :'),
                            tracking=True)


    # membuat sequence nomor antrian
    @api.model
    def create(self, vals):
        if vals.get('reference', _('Order ID :')) == _('Order ID :'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('restaurant.delivery') or _('Order ID :')
        res = super(Delivery, self).create(vals)
        return res

    def action_diantar(self):
        for rec in self:
            rec.state = 'diantar'

    def action_selesai(self):
        for rec in self:
            rec.state = 'selesai'


