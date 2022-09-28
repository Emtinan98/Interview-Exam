from odoo import models, fields


class palette_tracking(models.Model):
    _name = 'palette.tracking'

    picking_id = fields.Many2one('stock.picking', required=True)
    partner_id = fields.Many2one('res.partner',  )
    license_plate = fields.Char()
    picking_partner_id = fields.Many2one('res.partner')
    picking_date_done = fields.Datetime()
    palette_count_plus = fields.Integer()
    palette_count_minus = fields.Integer()
    balance = fields.Integer(compute='palette_count_plus' - 'palette_count_minus')

    _defaults = {
        'partner_id': lambda self: self.env.context.get('partner_id', False),
    }
