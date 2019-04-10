from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PaymentReceipt(models.Model):
    _inherit ='account.invoice'
    

    nomor_kwitansi = fields.Char(string='No. Kwitansi')
    terbilang = fields.Char(string='Terbilang')
    untuk = fields.Char(string='Untuk Pembayaran')

  
        
        
  