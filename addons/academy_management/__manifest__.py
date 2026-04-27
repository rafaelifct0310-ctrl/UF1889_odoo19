{
    'name': 'Academy Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestión de academia',
    'description': '''
        Módulo para gestionar estudiantes, cursos y matrículas
    ''',
    'author': 'Tu Nombre',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/tutoring_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}