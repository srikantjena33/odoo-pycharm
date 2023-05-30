from odoo import models, fields , api
from datetime import datetime, date


class ClassRoom(models.Model):
    _name = 'ld.classroom'
    _description = 'LD classroom model'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("Name")
    age = fields.Integer("Age")
    phone = fields.Char("Phone")
    email_id = fields.Char("Email ID")
    id_card_num = fields.Char("ID Number")
    course_id = fields.Many2one("ld.courses", string="Course Opted")
    state = fields.Selection([('1', 'Enquiry'), ('2', 'Joined'), ('3', 'Completed')],
                             string='State', default='1')
    date = fields.Date("Date", default=datetime.today())
    birth_date = fields.Date("BirthDate", default=datetime.today())
    age_calculated = fields.Text("Calculated Age")
    course_tags = fields.Text("Course Tags", compute='compute_course_tags')

    # def update_student_state(self):
    #     if self.state == '3':
    #         pass
    #     elif not self.state:
    #         self.state = '1'
    #     else:
    #         current_state = int(self.state)
    #         self.state = str(current_state + 1)



    def register_student_fees(self):
        title = f'Register fees of student name : {self.name}'
        return {
            'name': title,
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'ld.fees.register',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def compute_course_tags(self):
        course_name = self.course_id.course_name
        course_id = self.env['ld.courses'].search([('course_name', '=', course_name)])
        tag_ids = course_id.tag_ids
        tag_lst = list()
        for tag_id in tag_ids:
            tag_lst.append(tag_id.tag_name)
        self.course_tags = tag_lst


    def unlink(self):
        print(f"""\n\n
        -------------------------------------------------------------------------
            COURSE COMPLETION CERTIFICATE TO : {self.name}\n
            YOU HAVE SUCCESSFULLY COMPLETED THE COURSE : {self.course_id.course_name}\n
        -------------------------------------------------------------------------\n\n
        """)
        res = super().unlink()
        return res

    @api.onchange('birth_date')
    def calculateAge(self):
        today = date.today()
        age = today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        self.age_calculated = str(age) + " years"

    def action_send_mail(self):
        template = self.env.ref('training_module.mail_template_student_confirmation', False)
        compose_form = self.env.ref('mail.email_compose_message_wizard_form', False)
        ctx = dict(
            default_model='ld.classroom',
            default_res_id=self.id,
            default_use_template=bool(template),
            default_template_id=template.id,
        )
        return {
            'name': 'Send Confirmation to Student Via Email',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
            'context': ctx,
        }