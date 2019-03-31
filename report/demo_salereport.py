# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import tools
from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)

class CustomSaleReport(models.Model):
    _inherit = 'sale.report'

    order_line_id = fields.Integer('Order Line', readonly=True)

    def _select(self):
        _logger.debug("Select")
        return super()._select()+', l.id as order_line_id'

    def _group_by(self):
        _logger.debug("Group by")
        return super()._group_by()+', l.id'
