# -*- coding: utf-8 -*-
{
    'name': "Account Invoice Description",

    'summary': """
        Add description to invoice form and report.
    """,

    'description': """
        Add description to invoice form and report.
    """,

    'author': "Mint System GmbH",
    'website': "https://www.mint-system.ch",
    'category': 'Accounting',
    'version': '14.0.1.0.0',

    'depends': ['base', 'account'],

    'data': [
        'views/report_invoice_document.xml',
        'views/view_move_form.xml',
    ],

    'installable': True,
    'application': False,
}