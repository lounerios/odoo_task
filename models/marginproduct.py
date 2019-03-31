# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.addons import decimal_precision as dp
from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)

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


class SalesMarginOrderLine(models.Model):
    _inherit = 'sale.order.line'

    sales_margin = fields.Float(string='Sales Margin',digits=(1,2), default='1.00')
    cost = fields.Float(string='Cost', related='product_id.product_tmpl_id.standard_price', readonly=True)
    salespersons_ids = fields.Many2many('res.users', string='Sales Persons')

    @api.onchange('product_id')
    def product_is_changed(self):
        if(self.product_id):
            _logger.debug('Product is changed')
            product_template = self.env['product.template'].browse([self.product_id.product_tmpl_id.id])
            self.sales_margin = product_template.sales_margin

    @api.onchange('price_unit')
    def price_unit_is_changed(self):
        _logger.debug('Price unit is changed')
        if(self.price_unit > 0):
            product_template = self.env['product.template'].browse([self.product_id.product_tmpl_id.id])
            self.sales_margin = product_template.standard_price / self.price_unit
