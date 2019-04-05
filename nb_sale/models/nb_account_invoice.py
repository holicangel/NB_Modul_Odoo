from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    nomor_kwitansi = fields.Char(string='No. Kwitansi')
    terbilang = fields.Char(string='Terbilang')
    nomor_po = fields.Char(string='Nomor Purchase Order')
    untuk = fields.Char(string='Untuk Pembayaran')
