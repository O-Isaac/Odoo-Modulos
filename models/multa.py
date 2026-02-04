from odoo import models, fields

class Multa(models.Model):
    _name = 'gestion.multa'
    _description = 'Multas de Tráfico'
    _order = 'fecha desc'  # Ordenar por fecha, las más recientes primero

    name = fields.Char(string='Infracción', required=True, help="Ej: Exceso de velocidad")
    importe = fields.Float(string='Importe', digits=(10, 2))
    fecha = fields.Date(string='Fecha', default=fields.Date.context_today)
    
    # Campo de estado para gestionar el pago
    state = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('pagada', 'Pagada'),
        ('recurrida', 'Recurrida')
    ], string='Estado', default='pendiente', tracking=True)

    descripcion = fields.Text(string='Notas Adicionales')

    # Relación con el empleado
    empleado_id = fields.Many2one('hr.employee', string='Empleado', required=True)
    
    # Opción extra: Relación con el vehículo (si quisieras saber con qué coche fue)
    vehiculo_id = fields.Many2one('gestion.vehiculo', string='Vehículo Implicado')