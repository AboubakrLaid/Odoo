# -*- coding: utf-8 -*-
# from odoo import http


# class Services-odoo-module(http.Controller):
#     @http.route('/services-odoo-module/services-odoo-module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/services-odoo-module/services-odoo-module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('services-odoo-module.listing', {
#             'root': '/services-odoo-module/services-odoo-module',
#             'objects': http.request.env['services-odoo-module.services-odoo-module'].search([]),
#         })

#     @http.route('/services-odoo-module/services-odoo-module/objects/<model("services-odoo-module.services-odoo-module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('services-odoo-module.object', {
#             'object': obj
#         })

