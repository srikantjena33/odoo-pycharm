# -*- coding: utf-8 -*-
from odoo import models, fields, api


class StudentIdReportXlsx(models.AbstractModel):
    _name = 'report.training_module.report_student_id_xls'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Student ID Card Report Xlsx'

    def generate_xlsx_report(self, workbook, data, recs):
        sheet = workbook.add_worksheet(f'Student ID Card')
        row, col = 0, 0
        sheet.write(row, col, 'Date')
        sheet.write(row, col + 1, 'ID Card #')
        sheet.write(row, col + 2, 'Phone #')
        sheet.write(row, col + 3, 'Email')
        sheet.write(row, col + 4, 'Course Opted')
        row += 2
        for rec in recs:
            sheet.write(row, col, rec.date.strftime('%b %d %Y'))
            sheet.write(row, col + 1, rec.id_card_num)
            sheet.write(row, col + 2, rec.phone)
            sheet.write(row, col + 3, rec.email_id)
            sheet.write(row, col + 4, rec.course_id.course_name)
            row += 1
