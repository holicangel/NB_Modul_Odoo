from odoo import api, models, _

class SaleOrder(models.Model):

    _inherit = 'sale.order'


@api.model
def create(self, vals):

    record = super(SaleOrder, self).create(vals)

    record['name'] = self.env['ir.sequence'].next_by_code('new.sale.order') or _('New')

    return record