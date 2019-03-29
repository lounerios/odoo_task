# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.addons import decimal_precision as dp
from odoo import api, fields, models

class SalesMarginProduct(models.Model):
    _inherit = 'product.template'

    sales_margin = fields.Float(string='Sales Margin',digits=(1,2), default='1.00')

    @api.onchange('sales_margin', 'standard_price')
    def _compute_price(self):
        if self.sales_margin <= 0:
            return {
                'warning': {
                     'title': "Not valid sales margin",
                     'message': "The sales margin does have a valid value"
                },
            }

        self.list_price = self.standard_price / self.sales_margin
        print(self.list_price)


class SalesMarginOrderLine(models.Model):
    _inherit = 'sale.order.line'

    sales_margin = fields.Float(string='Sales Margin',digits=(1,2), default='1.00')
