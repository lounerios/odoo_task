# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import tools
from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)

class CustomSaleReport(models.Model):
    _inherit = 'sale.report'

    order_line_id = fields.Integer('Order Line', readonly=True)
    sales_person_id = fields.Integer('New Sale Person', readonly=True)

    def _select(self):
        _logger.debug("Select")
        select_str = """
            , l.id as order_line_id,
            rs.res_users_id as sales_person_id
        """
        return super()._select()+select_str

    def _from(self):
        _logger.debug("From")
        from_str = """
            left join res_users_sale_order_line_rel rs on (l.id = rs.sale_order_line_id)
        """
        return super()._from()+from_str

    def _group_by(self):
        _logger.debug("Group by")
        _group_by_str = """
            , l.id,
            rs.res_users_id
        """
        return super()._group_by()+_group_by_str
