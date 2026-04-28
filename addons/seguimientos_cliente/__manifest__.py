{
    'name': 'Seguimientos Cliente',
    'version': '1.0',
    'category': 'Generic',
    'summary': 'Campo calculado de seguimientos por cliente',
    'description': """Módulo que añade campo calculado de seguimientos por cliente.
Extiende res.partner con campo computed que cuenta seguimientos.""",
    'author': 'UF1889',
    'license': 'LGPL-3',
    'depends': ['mail'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}