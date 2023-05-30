from odoo import models, fields, api


class CrmInhe(models.Model):
    _inherit = 'crm.lead'

    fax_number = fields.Char(string="Customer Fax Number")

    @api.model
    def create(self, vals):
        print("================>>>>>>>OLD VALS\n")
        print(vals)
        old_fax_num = vals['fax_number']
        new_fax_num = 'PUNE-' + old_fax_num
        vals['fax_number'] = new_fax_num
        print("================>>>>>>>NEW VALS\n")
        print(vals)
        return super(CrmInhe, self).create(vals)

    def write(self, vals):
        print("================>>>>>>>WRITE METHOD OLD VALS\n")
        print(vals)
        old_fax_num = vals['fax_number']
        new_fax_num = 'PUNE-' + old_fax_num
        vals['fax_number'] = new_fax_num
        print("================>>>>>>>WRITE METHOD NEW VALS\n")
        print(vals)
        return super(CrmInhe, self).write(vals)