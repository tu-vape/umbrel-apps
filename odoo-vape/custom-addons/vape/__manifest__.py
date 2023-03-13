# -*- coding: utf-8 -*-
{
    'name': "Mai Class",

    'summary': """
        "Mai Class""",

    'description': """
        "Mai Class
    """,

    'author': "NTU",
    'website': "https://ntu.io/",

    # Categories can be used to filter modules in modules listing
    'category': 'Extra',
    'version': '16.0.0',
    'license': 'LGPL-3',

    # "images": ["static/description/icon.png", ],
    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'data/res_config_data.xml'
    ],

    "application": True,
    "installable": True,
    "auto_install": [],

}