# -*- coding: utf-8 -*-
{
    'name': "DemoTask",
    'summary': "A demo task from Lucas",
    'description': "Long description of module's purpose",
    'author': "Lucas Simopoulos",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','sale'],
    'data': [
        # 'security/ir.model.access.csv',
          'views/sales_margin_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
