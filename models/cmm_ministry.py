# -*- coding: utf-8 -*-

from odoo import models, fields # Import necessary Odoo modules

class CmmMinistry(models.Model):
    """
    Extends the res.partner model to add member-specific fields.
    """
    _name = "cmm.ministry"

    name = fields.Char()
    description = fields.Text()
    in_charge = fields.Many2one('res.partner')

    member_ids = fields.Many2many("res.partner", "cmm_partner_ministry_rel", "ministry_id", "partner_id")