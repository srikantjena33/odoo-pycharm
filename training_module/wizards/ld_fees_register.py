from odoo import models, fields


class LdFeesRegister(models.TransientModel):
    _name = 'ld.fees.register'

    amount = fields.Float('Fees')

    def register_fees(self):
        """import pdb; pdb.set_trace()
        n + enter > nextline
        l + enter > which line
        c + enter > cancel
        """
        ctx = self.env.context
        student_id = ctx['active_id']
        student_record = self.env['ld.classroom'].browse(student_id)
        student_record.state = '2'
