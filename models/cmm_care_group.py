# -*- coding: utf-8 -*-

from odoo import models, fields # Import necessary Odoo modules

class CmmMinistry(models.Model):
    """
    Extends the res.partner model to add member-specific fields.
    """
    _name = "cmm.care.group"

    name = fields.Char()
    in_charge_id = fields.Many2one("cmm.member", "In-Charge")
    member_ids = fields.One2many("cmm.member", "care_group_id", string="Members")
    # member_details_id = fields.One2many("cmm.member", "partner_id", string="Member Details")