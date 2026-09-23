from odoo import models


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    def _get_aggregated_properties(self, move_line=False, move=False):
        # Expose the destination package so the delivery report can print its gross weight.
        res = super()._get_aggregated_properties(move_line=move_line, move=move)
        res['result_package_id'] = move_line.result_package_id if move_line else self.env['stock.quant.package']
        return res
