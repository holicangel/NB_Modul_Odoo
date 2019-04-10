from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    perihal = fields.Char(string='Subject')
    

    kepada = fields.Many2one(comodel_name='res.partner', string='Receiver Name')
    
    @api.multi
    def print_nb(self):
        self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
        return self.env['report'].get_action(self, 'nb_sale.nb_sale_order_print_template')
    # tanggal_order = fields.Date(string="Tanggal Dibuat")
    # tanggal_validasi = fields.Date(string="Tanggal Validasi")
    # pembayaran = fields.Selection([
    #         ('satu', 'Satu Bulan'),
    #         ('dua', 'Dua Bulan'),
    #     ], string='Jangka Pembayaran')

  

    # tanggal_order = fields.Date(string='Tanggal Penawaran', default=fields.Date.today())
    # tanggal_validasi = fields.Date(string='Masa Berlaku')
    # tanggal_konfirmasi = fields.Date(string='Tanggal Validasi SO', default=fields.Date.today())

    