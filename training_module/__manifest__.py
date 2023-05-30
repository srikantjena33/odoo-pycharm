{
  'name': 'LD-Odoo training',
  'author': 'LD-Odoo training',
  'depends': ['base','mail', 'crm' , 'report_xlsx' ],
   'data': [
    'security/ir.model.access.csv',
    'security/groups.xml',
    'views/classroom.xml',
    'views/courses.xml',
    'views/course_tag.xml',
    'wizards/ld_fees_register.xml',
    'views/ld_crm_inhe.xml',
    'data/mail_template_data.xml',
    'report/student_idcard.xml',
    'report/student_id_xls.xml',
    ],
  'installable': True,
  'auto_install': False,
  'license': 'LGPL-3',
}