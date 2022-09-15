# -*- coding: utf-8 -*-
{
    'name': "restaurant",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Denny",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/pembatalan_view.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/menu_view.xml',
        'views/order_view.xml',
        'views/inventory_view.xml',
        'views/bahan_makanan_view.xml',
        'views/menu_makanan_view.xml',
        'views/pekerja_view.xml',
        'views/member_view.xml',
        'views/supplier_view.xml',
        'views/antrian_view.xml',
        'views/delivery_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
