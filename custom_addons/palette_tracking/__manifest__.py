# -*- coding: utf-8 -*-
{
    'name': "palette_tracking",

    'summary': """Odoo Module Deneme""",

    'description': """
        pt module for managing tracking
    """,

    'author': "Emtinan",
    'website': "http://www.ugurcanusta.me",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

   # always loaded
    'data': [
        'view/palette_tracking.xml',
        # 'security/ir.model.access.csv',

    ],
   # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'installable':True,
    'application':False,
    'auto_install':False
}