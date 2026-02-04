{
    'name': 'Gestión de Vehículos de Empresa',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Control de flota y multas de empleados',
    'description': """
        Módulo para gestionar la flota de vehículos de la empresa.
        - Asignación de vehículos a empleados.
        - Registro de características (Matrícula, marca, modelo).
        - Historial de multas asociado al empleado.
    """,
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/vehiculo_view.xml',
        'views/empleado_view.xml',
        'views/marca_view.xml',
        'views/historial_view.xml',
        'views/multa_view.xml',
        'views/menu.xml'
    ],
    'demo': [
        'demo/marcas.xml',      # 1º: Las marcas no dependen de nada
        'demo/vehiculos.xml',   # 2º: Depende de marcas
        'demo/empleado.xml',    # 3º: Depende de vehículos para la asignación inicial
        'demo/historial.xml',   # 4º: Depende de vehículos y empleados
        'demo/multas.xml',      # 5º: Depende de vehículos y empleados
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}