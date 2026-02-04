from odoo import models, fields

class Marca(models.Model):
    _name = 'gestion.marca'
    _description = 'Marca de Vehículo'
    _rec_name = 'name'

    name = fields.Char(string='Nombre', required=True)
    pais_origen = fields.Char(string='País de Origen')
    descripcion = fields.Text(string='Descripción')
    logo = fields.Binary(string='Logo')
    
    # Relación con vehículos
    vehiculo_ids = fields.One2many('gestion.vehiculo', 'marca_id', string='Vehículos')
    vehiculo_count = fields.Integer(string='Total Vehículos', compute='_compute_vehiculo_count')

    def _compute_vehiculo_count(self):
        for record in self:
            record.vehiculo_count = len(record.vehiculo_ids)