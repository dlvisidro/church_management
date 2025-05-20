# -*- coding: utf-8 -*-
{
    'name': "Church Management",

    'summary': """
        Manage members, seminar attendance, and application details.""",

    'description': """
        This module extends the contact application to add features for managing members, 
        including seminar attendance, application forms, membership status, membership dates, 
        and reasons for leaving.
    """,

    'author': "ID Labs",
    'website': "https://theinfinitescroll.net",

    'category': 'Customer Relationship Management',
    'version': '18.0.1.0.0',

    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cmm_member_views.xml',
        'views/cmm_ministry.xml',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml', # If you have demo data
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
