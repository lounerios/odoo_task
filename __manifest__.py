# -*- coding: utf-8 -*-
{
    'name': "DemoTask",
    'summary': "A demo task from Lucas",
    'description': "Long description of module's purpose",
    'author': "Lucas Simopoulos",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.2',
    'depends': ['base','sale'],
    'data': [
          'views/product_sales_margin_view.xml',
          'views/orderline_sales_margin_view.xml',          
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
