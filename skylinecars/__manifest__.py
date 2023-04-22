{
    'name': 'skylinecars',
    'author': 'Bowmika',
    'version': '0.1',
    'depends': ['base','purchase'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/payment_views.xml',
        'views/customerdetails_views.xml',
        'views/billingdetails_views.xml',
        'views/vehicledetails_views.xml',
        'views/purchase_views.xml',
        'views/driverdetails_views.xml',
        'views/discount_views.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False
}