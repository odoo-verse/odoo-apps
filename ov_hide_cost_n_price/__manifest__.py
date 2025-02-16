# -*- coding: utf-8 -*-
{
    'name': "Hide Product Cost And Sale Price",

    'summary': "Hide Product Cost And Sale Price To Specific User",

    'description': """Hide Product Cost And Sale Price To Specific User""",

    'author': "Odoo VERSE",
    'category': 'Inventory',
    'version': '17.0.1.0.0',
    'depends': ['base','stock'],
    'data': [
        'security/security.xml',
        'views/inherit_product.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
    "images": [
        "static/description/banner.png",
    ],
}

