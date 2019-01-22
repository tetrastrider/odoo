# -*- coding: utf-8 -*-
{
    'name': "gancedo",
    'sequence': 1,
    'summary': """
        Formulario de control de clientes""",

    'description': """
        aplicacion para la gestion de clientes dentro de la compañia
    """,

    'author': "Alexander Jose Brache Gancedo",
    'website': "http://www.overclocktech.com",

    'category': 'informacion',
    'version': '1.0',

    'depends': ['base'],

    'data': [
         'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'css':'static/src/css/estilos.css',
}