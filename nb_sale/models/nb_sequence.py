from odoo import api, models, _

class AccountInvoice(models.Model):

    _inherit = 'account.invoice'


@api.model
def create(self, vals):

    record = super(AccountInvoice, self).create(vals)

    record['name'] = self.env['ir.sequence'].next_by_code('payment.receipt') or _('New')

    return record