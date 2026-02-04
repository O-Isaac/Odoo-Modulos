from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # Simulamos un campo One2one usando compute e inverse
    vehiculo_id = fields.Many2one(
        'gestion.vehiculo', 
        string='Vehículo Actual',
        compute='_compute_vehiculo', 
        inverse='_inverse_vehiculo',
        store=False # No se guarda en bbdd hr_employee, se lee de gestion_vehiculo
    )

    # Historial de multas (One2many)
    multa_ids = fields.One2many('gestion.multa', 'empleado_id', string='Historial de Multas')
    
    # Campo computado auxiliar para la vista (opcional en v19, pero útil para lógica compleja)
    tiene_multas = fields.Boolean(compute='_compute_tiene_multas', store=False)

    @api.depends('multa_ids')
    def _compute_tiene_multas(self):
        for record in self:
            record.tiene_multas = len(record.multa_ids) > 0

    # --- LÓGICA DE SINCRONIZACIÓN AUTOMÁTICA ---
    def _compute_vehiculo(self):
        """ Busca en la tabla de vehículos si este empleado es conductor """
        for employee in self:
            # Buscamos el vehículo donde conductor_id sea este empleado
            employee.vehiculo_id = self.env['gestion.vehiculo'].search(
                [('conductor_id', '=', employee.id)], limit=1
            )

    def _inverse_vehiculo(self):
        """ Cuando asignas un vehículo desde la ficha del empleado """
        for employee in self:
            # 1. Si el empleado ya tenía un vehículo anterior, lo liberamos
            vehiculo_anterior = self.env['gestion.vehiculo'].search([('conductor_id', '=', employee.id)], limit=1)
            
            # Verificamos si existe un vehículo anterior Y que no sea el mismo que estamos asignando ahora
            if vehiculo_anterior and (not employee.vehiculo_id or vehiculo_anterior.id != employee.vehiculo_id.id):
                vehiculo_anterior.conductor_id = False
            
            # 2. Si se ha seleccionado un nuevo vehículo, lo asignamos
            if employee.vehiculo_id:
                # Opcional: Si el nuevo vehículo ya tenía otro conductor,
                # el SQL Constraint saltará, o podemos forzar la reasignación:
                employee.vehiculo_id.conductor_id = employee.id