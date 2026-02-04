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
        'views/menu.xml',
        'demo/demo.xml'
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}