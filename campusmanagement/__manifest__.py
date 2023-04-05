{
    'name': 'Campus',
    'author': 'Bowmika',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/teacher_views.xml',
        'views/subject_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False

}