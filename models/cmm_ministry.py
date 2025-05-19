# -*- coding: utf-8 -*-

from odoo import models, fields # Import necessary Odoo modules

class CmmMinistry(models.Model):
    """
    Extends the res.partner model to add member-specific fields.
    """
    _name = "cmm.member"

    name = fields.Char()
    description = fields.Text()
    in_charge = fields.Many2one('res.partner')