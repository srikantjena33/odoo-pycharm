from odoo import models, fields


class CoursesTag(models.Model):

    _name = 'ld.courses.tag'
    _description = 'LD course tag'
    _rec_name = 'tag_name'

    tag_name = fields.Char("Tag Name")

