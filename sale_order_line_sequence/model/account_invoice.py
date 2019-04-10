# -*- coding: utf-8 -*-
# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# Copyright 2017 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    @api.depends('invoice_line_ids')
    def _compute_max_line_sequence(self):
        """Allow to know the highest sequence entered in sale order lines.
        Then we add 1 to this value for the next sequence.
        This value is given to the context of the o2m field in the view.
        So when we create new sale order lines, the sequence is automatically
        added as :  max_sequence + 1
        """
        for account in self:
            account.max_line_sequence = (
                max(sale.mapped('order_line.sequence') or [0]) + 1)

    max_line_sequence_1 = fields.Integer(string='Max sequence in lines',
                                       compute='_compute_max_line_sequence_1',
                                       store=True)

    @api.multi
    def _reset_sequence(self):
        for rec in self:
            current_sequence = 1
            for line in rec.invoice_line_ids:
                line.sequence = current_sequence
                current_sequence += 1

    @api.multi
    def write(self, line_values):
        res = super(AccountInvoice, self).write(line_values)
        self._reset_sequence()
        return res

    @api.multi
    def copy(self, default=None):
        return super(AccountInvoice,
                     self.with_context(keep_line_sequence=True)).copy(default)


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line' 

    # re-defines the field to change the default
    sequence_inv = fields.Integer(help="Gives the sequence of this line when "
                                   "displaying the sale order.",
                              default=9999)

    # displays sequence on the order line
    sequence2_inv = fields.Integer(help="Shows the sequence of this line in "
                               "the sale order.",
                               related='sequence', readonly=True,
                               store=True)

    @api.model
    def create(self, values):
        line = super(AccountAnalyticLine, self).create(values)
        # We do not reset the sequence if we are copying a complete sale order
        if self.env.context.get('keep_line_sequence'):
            line.invoice_line_ids._reset_sequence()
        return line
