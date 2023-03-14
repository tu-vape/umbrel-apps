# -*- coding: utf-8 -*-
{
    'name': "Vape",

    'summary': """
        "Mai Class""",

    'description': """
        "Vape
    """,

    'author': "NTU",
    'website': "https://ntu.io/",

    # Categories can be used to filter modules in modules listing
    'category': 'Extra',
    'version': '16.0.0',
    'license': 'LGPL-3',

    # "images": ["static/description/icon.png", ],
    # any module necessary for this one to work correctly
    'depends': ['point_of_sale', 'l10n_vn'],

    # always loaded
    'data': [
        'data/res_users_demo.xml',
        'data/demo_company.xml'
    ],

    "application": True,
    "installable": True,
    "auto_install": [],

}