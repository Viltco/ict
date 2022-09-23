# -*- coding: utf-8 -*-
{
    'name': "Sale Attribute",

    'summary': """
        Make Many2one Field Non-Creatable in Sale Order""",

    'description': """
        Make Many2one Field Non-Creatable in Sale Order
    """,

    'author': "Viltco",
    'website': "http://www.viltco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '14.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/sale_attribute_views.xml',
    ],

}
