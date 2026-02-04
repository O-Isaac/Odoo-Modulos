from odoo import models, fields, api

class VehiculoHistorial(models.Model):
    """
    Modelo para gestionar el historial de asignaciones de vehículos a empleados.
    Guarda quién condujo qué coche y en qué periodo.
    """
    _name = 'gestion.historial.vehiculo'
    _description = 'Historial de Asignación de Vehículos'
    _order = 'fecha_inicio desc'
    _rec_name = 'conductor_id'

    # Relación con el vehículo
    vehiculo_id = fields.Many2one('gestion.vehiculo', string='Vehículo', required=True, ondelete='cascade')
    # Relación con el empleado
    conductor_id = fields.Many2one('hr.employee', string='Empleado', required=True)
    # Rango de fechas de la asignación
    fecha_inicio = fields.Date(string='Fecha Inicio', default=fields.Date.context_today, required=True)
    fecha_fin = fields.Date(string='Fecha Fin')
    
    # Campo auxiliar para el calendario: si no ha terminado, mostramos hasta hoy
    # Nota: store=True es necesario para vistas como Calendario/Search, 
    # aunque implica que el valor "hoy" se congela al calcularse y no avanza automáticamente.
    fecha_fin_visual = fields.Date(compute='_compute_fecha_fin_visual', store=True)

    @api.depends('fecha_fin')
    def _compute_fecha_fin_visual(self):
        for rec in self:
            rec.fecha_fin_visual = rec.fecha_fin or fields.Date.context_today(self)

    def name_get(self):
        """ Personaliza el nombre mostrado en las vistas (ej. Calendario) """
        result = []
        for rec in self:
            name = f"{rec.vehiculo_id.matricula} - {rec.conductor_id.name}"
            result.append((rec.id, name))
        return result