{
    'name': 'Custom DDT Report',
    'version': '18.0.1.0.0',
    'summary': 'Adds carrier and weight information to the delivery slip report',
    'category': 'Inventory/Delivery',
    'depends': ['stock', 'delivery'],
    'data': [
        'report/delivery_report_inherit.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
