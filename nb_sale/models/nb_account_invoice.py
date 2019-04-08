from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    

    nomor_kwitansi = fields.Char(string='No. Kwitansi')
    terbilang = fields.Char(string='Terbilang')
    untuk = fields.Char(string='Untuk Pembayaran')


# @api.multi
# def set_open(self):
#     # nama fungsi tidak boleh recompute, create, write dll
#     tombol_receipt = self.env['account.invoce']

    

