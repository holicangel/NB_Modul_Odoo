from datetime import datetime, date
from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError

class Wizard(models.TransientModel):


    _name = 'payment.receipt.wizard'
    _inherit ='account.invoice'
    
    name = fields.Char(string='Name')

      
    @api.multi
    def write_1(self):

        record_ids = self.env['payment.receipt.wizard'].search([('nomor_kwitansi', '=', 'Example')])
        for record in record_ids:
            record.write({
                'nomor_kwitansi': 'some_description'
            })
        return super(Wizard, self).write(vals)
        
    # def process_wizard(self):
    #     ids_to_change = self._context.get('active_ids')
    #     active_model = self._context.get('active_model')
    #     doc_ids = self.env[active_model].browse(ids_to_change)
        # 1. Run another function
        # doc_ids.set_open()

        # 2. Modify selected Document
        # doc_ids.write(
        #     {
        #         'state' : self.name
        #     }
        # )
