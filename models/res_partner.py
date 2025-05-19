# -*- coding: utf-8 -*-

from odoo import models, fields, api # Import necessary Odoo modules

class ResPartner(models.Model):
    """
    Extends the res.partner model to add member-specific fields.
    """
    _inherit = 'res.partner'  # Inherit from the existing res.partner model

    is_church_member = fields.Boolean(string="Church Member")

    member_details_id = fields.Many2one("cmm.member", "Member Details")

    status = fields.Selection(related="member_details_id.status", default="member", readonly=False, store=True)
    date_of_membership = fields.Date(related="member_details_id.date_of_membership", readonly=False, store=True)
    reason_for_leaving = fields.Text(related="member_details_id.reason_for_leaving", readonly=False, store=True)
    designation = fields.Selection(related="member_details_id.designation", default="member", readonly=False, store=True)
    is_member_active = fields.Boolean(related="member_details_id.is_active")
    # --- You could add computed fields or onchange methods here if needed ---
    # Example:
    # @api.onchange('member_status')
    # def _onchange_member_status(self):
    #     if self.member_status != 'past_member':
    #         self.reason_for_leaving = False # Clear reason if not a past member
    #     if self.member_status == 'member' and not self.date_of_membership:
    #         self.date_of_membership = fields.Date.today() # Set membership date if status becomes member
