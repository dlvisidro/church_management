# -*- coding: utf-8 -*-

from odoo import models, fields # Import necessary Odoo modules

class CmmPastoralDuty(models.Model):
    """
    Extends the res.partner model to add member-specific fields.
    """
    _name = "cmm.pastoral.duty"

    pastor_id = fields.Many2one('cmm.member', 'Officiating Pastor', domain=[('designation', '=', 'pastor')])

    type = fields.Selection([
        ('wedding', 'Wedding'),
        ('wakes', 'Wakes'),
        ('baptism', 'Baptism'),
        ('dedication', 'Child Dedication'),
        ('counselling', 'Counselling')
    ], string='Type')

    date = fields.Date()
    venue = fields.Char()

    # Temporary fields
    groom = fields.Char()
    bride = fields.Char()
