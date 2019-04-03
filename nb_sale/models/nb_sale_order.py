from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    perihal = fields.Char(string='Perihal')
    kepada = fields.Char(string='Nama Penerima')
    
