from odoo import models, fields


class Courses(models.Model):
    _name = 'ld.courses'
    _description = 'LD course model'
    _rec_name = 'course_name'

    course_name = fields.Char("Course Name")
    trainer_name = fields.Char("Trainer Name")
    course_content = fields.Text("Course Content")
    duration = fields.Char("Course Duration")
    tag_ids = fields.Many2many("ld.courses.tag", "ld_courses_ld_tags_rel", string="Tags")
    course_level = fields.Selection([('1', 'Beginner'), ('2', 'Moderate'), ('3', 'Expert')])
    tag_count = fields.Integer("Tags Count", compute='compute_tag_count')

    def update_course_level(self):
        if self.course_level in (False, '3'):
            self.course_level = '1'
        else:
            current_level = int(self.course_level)
            new_level = current_level + 1
            self.course_level = str(new_level)

        # def update_course_level(self):
        #     if not self.course_level or self.course_level == '3':
        #         self.course_level = '1'
        #     else:
        #         self.course_level = str(int(self.course_level) + 1)

    def compute_tag_count(self):
        if self.tag_ids:
            self.tag_count = len(self.tag_ids)
        else:
            self.tag_count = 0