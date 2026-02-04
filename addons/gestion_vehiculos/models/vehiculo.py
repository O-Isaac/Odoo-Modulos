from odoo import models, fields, api
from odoo.exceptions import UserError

class Vehiculo(models.Model):
    _name = 'gestion.vehiculo'
    _description = 'Vehículo de Empresa'
    _rec_name = 'matricula'

    matricula = fields.Char(string='Matrícula', required=True)
    kilometros = fields.Integer(string='Kilómetros al préstamo')
    marca_id = fields.Many2one('gestion.marca', string='Marca', required=True)
    modelo = fields.Char(string='Modelo')
    
    # Campo estándar de Odoo para "Dar de baja" (Archivar)
    # Si active es False, el vehículo desaparece de las búsquedas por defecto.
    active = fields.Boolean(string='Activo', default=True)

    # Conductor actual
    conductor_id = fields.Many2one('hr.employee', string='Empleado Asignado')

    # Relación con el historial
    historial_ids = fields.One2many('gestion.historial.vehiculo', 'vehiculo_id', string='Historial de Uso')

    # Campo computado para la "Etiqueta Verde" o estado visual
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('asignado', 'Asignado'),
        ('baja', 'De Baja')
    ], string='Estado', compute='_compute_estado', store=True)

    _sql_constraints = [
        ('conductor_uniq', 'unique(conductor_id)', 'Este empleado ya tiene un vehículo asignado.')
    ]

    # --- LÓGICA DE ESTADOS Y ETIQUETAS ---
    @api.depends('conductor_id', 'active')
    def _compute_estado(self):
        for rec in self:
            if not rec.active:
                rec.estado = 'baja'
            elif rec.conductor_id:
                rec.estado = 'asignado'
            else:
                rec.estado = 'disponible'

    # --- LÓGICA DE PROTECCIÓN DE BORRADO ---
    def unlink(self):
        """ Impide borrar vehículos. Solo permite archivarlos. """
        for rec in self:
            if rec.active:
                raise UserError("No se pueden eliminar vehículos. Por favor, utiliza la opción 'Archivar' o dalo de baja desmarcando la casilla 'Activo'.")
        return super(Vehiculo, self).unlink()

    # --- LÓGICA DE HISTORIAL AUTOMÁTICO ---
    @api.model
    def create(self, vals):
        # Creamos el vehículo
        vehiculo = super(Vehiculo, self).create(vals)
        
        # Si nace con conductor, creamos la primera línea de historial
        if vehiculo.conductor_id:
            self.env['gestion.historial.vehiculo'].create({
                'vehiculo_id': vehiculo.id,
                'conductor_id': vehiculo.conductor_id.id,
                'fecha_inicio': fields.Date.context_today(self),
            })
            
        return vehiculo

    def write(self, vals):
        # Detectamos si se va a cambiar el conductor o si se va a archivar
        cambio_conductor = 'conductor_id' in vals
        archivar = 'active' in vals and not vals['active']

        for vehiculo in self:
            # 1. Si se quita el conductor o se cambia por otro, cerramos el historial abierto
            if (cambio_conductor and vehiculo.conductor_id) or archivar:
                # Buscamos el historial abierto (sin fecha fin)
                historial_abierto = self.env['gestion.historial.vehiculo'].search([
                    ('vehiculo_id', '=', vehiculo.id),
                    ('fecha_fin', '=', False)
                ], limit=1)
                
                if historial_abierto:
                    historial_abierto.fecha_fin = fields.Date.context_today(self)

            # 2. Si asignamos un NUEVO conductor
            if cambio_conductor:
                nuevo_conductor_id = vals.get('conductor_id')
                if nuevo_conductor_id:
                    # Verificar si intentamos asignar a un coche dado de baja
                    if not vehiculo.active and not vals.get('active', False):
                         raise UserError("No puedes asignar un conductor a un vehículo dado de baja.")

                    self.env['gestion.historial.vehiculo'].create({
                        'vehiculo_id': vehiculo.id,
                        'conductor_id': nuevo_conductor_id,
                        'fecha_inicio': fields.Date.context_today(self),
                    })

        # Ejecutamos la escritura normal
        res = super(Vehiculo, self).write(vals)

        return res