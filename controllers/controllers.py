# -*- coding: utf-8 -*-
from odoo import http

# class Gancedo(http.Controller):
#     @http.route('/gancedo/gancedo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gancedo/gancedo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gancedo.listing', {
#             'root': '/gancedo/gancedo',
#             'objects': http.request.env['gancedo.gancedo'].search([]),
#         })

#     @http.route('/gancedo/gancedo/objects/<model("gancedo.gancedo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gancedo.object', {
#             'object': obj
#         })