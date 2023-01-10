# -*- coding: utf-8 -*-
from odoo import api, fields, models, http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleInherit(WebsiteSale):
    
    @http.route(['/shop/checkout'], type='http', auth="public", website=True, sitemap=False)
    def checkout(self, **post):
        order = request.website.sale_get_order()
        oos = [] # list of out of stock product_ids
        for line in order.order_line:
            if line.product_id.qty_available < 1:
                 oos.append(line.product_id)
        if not oos: 
            return super(WebsiteSaleInherit, self).checkout(**post)
        else:
            # show product config with items in oos 
            return request.redirect('/shop/cart')