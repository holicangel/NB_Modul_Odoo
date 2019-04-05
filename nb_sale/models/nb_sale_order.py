from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    perihal = fields.Char(string='Subject')
    kepada = fields.Char(string='Receiver Name')
    # tanggal_order = fields.Date(string="Tanggal Dibuat")
    # tanggal_validasi = fields.Date(string="Tanggal Validasi")
    # pembayaran = fields.Selection([
    #         ('satu', 'Satu Bulan'),
    #         ('dua', 'Dua Bulan'),
    #     ], string='Jangka Pembayaran')

  

    tanggal_order = fields.Date(string='Tanggal Penawaran', default=fields.Date.today())
    tanggal_validasi = fields.Date(string='Masa Berlaku')
    tanggal_konfirmasi = fields.Date(string='Tanggal Validasi SO', default=fields.Date.today())

    