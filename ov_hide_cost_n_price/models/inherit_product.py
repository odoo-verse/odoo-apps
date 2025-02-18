from odoo import fields, models


class InheritProduct(models.Model):
    _inherit = 'product.template'

    is_cost_hide = fields.Boolean(
        string="Is Cost Hide", compute="_compute_is_cost_hide"
    )

    is_sale_price_hide = fields.Boolean(
        string="Is Sale Price Hide", compute="_compute_is_sale_price_hide"
    )

    def _compute_is_cost_hide(self):
        for record in self:
            record.is_cost_hide = False
            if self.env.user.has_group(
                "ov_hide_cost_n_price.hide_product_cost"
            ):
                record.is_cost_hide = True

    def _compute_is_sale_price_hide(self):
        for record in self:
            record.is_sale_price_hide = False
            if self.env.user.has_group(
                "ov_hide_cost_n_price.hide_sale_price"
            ):
                record.is_sale_price_hide = True
