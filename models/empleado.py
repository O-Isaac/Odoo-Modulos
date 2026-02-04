from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # Campo para saber qué vehículo tiene asignado actualmente
    vehiculo_id = fields.Many2one('gestion.vehiculo', string='Vehículo Actual')

    # Historial de multas (One2many)
    multa_ids = fields.One2many('gestion.multa', 'empleado_id', string='Historial de Multas')
    
    # Campo computado auxiliar para la vista (opcional en v19, pero útil para lógica compleja)
    tiene_multas = fields.Boolean(compute='_compute_tiene_multas', store=False)

    @api.depends('multa_ids')
    def _compute_tiene_multas(self):
        for record in self:
            record.tiene_multas = len(record.multa_ids) > 0