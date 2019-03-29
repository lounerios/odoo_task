# -*- coding: utf-8 -*-
from odoo import http

# class MyTask(http.Controller):
#     @http.route('/my_task/my_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_task/my_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_task.listing', {
#             'root': '/my_task/my_task',
#             'objects': http.request.env['my_task.my_task'].search([]),
#         })

#     @http.route('/my_task/my_task/objects/<model("my_task.my_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_task.object', {
#             'object': obj
#         })