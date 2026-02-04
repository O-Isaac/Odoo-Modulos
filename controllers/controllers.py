# from odoo import http


# class GestionVehiculos(http.Controller):
#     @http.route('/gestion_vehiculos/gestion_vehiculos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_vehiculos/gestion_vehiculos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_vehiculos.listing', {
#             'root': '/gestion_vehiculos/gestion_vehiculos',
#             'objects': http.request.env['gestion_vehiculos.gestion_vehiculos'].search([]),
#         })

#     @http.route('/gestion_vehiculos/gestion_vehiculos/objects/<model("gestion_vehiculos.gestion_vehiculos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_vehiculos.object', {
#             'object': obj
#         })

