from odoo import models, fields

from odoo import models, fields, api

class Vehiculo(models.Model):
    _name = 'gestion.vehiculo'
    _description = 'Vehículo de Empresa'
    _rec_name = 'matricula'

    matricula = fields.Char(string='Matrícula', required=True)
    kilometros = fields.Integer(string='Kilómetros al préstamo')
    marca_id = fields.Many2one('gestion.marca', string='Marca', required=True)
    modelo = fields.Char(string='Modelo')
    
    # Añadimos lógica para limpiar el vehículo anterior del empleado
    conductor_id = fields.Many2one('hr.employee', string='Empleado Asignado')

    @api.model
    def create(self, vals):
        res = super(Vehiculo, self).create(vals)
        if res.conductor_id:
            res.conductor_id.vehiculo_id = res.id
        return res

    def write(self, vals):
        # Si se cambia el conductor, sincronizamos
        res = super(Vehiculo, self).write(vals)
        if 'conductor_id' in vals:
            for record in self:
                if record.conductor_id:
                    record.conductor_id.vehiculo_id = record.id
        return res