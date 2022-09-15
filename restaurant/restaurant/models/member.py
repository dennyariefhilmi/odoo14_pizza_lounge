from odoo import fields, models, api


class member(models.Model):
    _inherit = 'res.partner'
    _description = 'Description'

    name = fields.Char('Nama')
    member_id = fields.Char(
        string='Member ID',
        required=False)
    level = fields.Selection(
        string='Level',
        selection=[('bronze', 'Bronze'),
                   ('Silver', 'Silver'),
                   ('gold','Gold'),
                   ('platinum', 'Platinum')],
        required=False, )
    no_hp = fields.Char(
        string='No HP',
        required=False)
    tanggal_gabung = fields.Date(
        string='Tanggal Bergabung',
        required=False)
    tanggal_lahir = fields.Date(
        string='Tanggal Lahir',
        required=False)

