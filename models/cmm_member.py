# -*- coding: utf-8 -*-

from odoo import models, fields # Import necessary Odoo modules

class CmmMember(models.Model):
    """
    Extends the res.partner model to add member-specific fields.
    """
    _name = "cmm.member"
    _inherits = {"res.partner": "partner_id"}

    partner_id = fields.Many2one('res.partner', 'Partner', required=True, ondelete='cascade')

    # Seminar attendance fields
    # These are Boolean fields, True if attended, False otherwise.
    has_attended_gc = fields.Boolean("Attended Gospel Clarity")
    has_attended_ctoa = fields.Boolean("Attended Committing to One Another")

    # Application form field
    # This is a Binary field to store file uploads (e.g., PDF, Word document).
    # `attachment=True` is often used for better handling by Odoo's document management,
    # but for simplicity, a direct binary field is used here.
    # You might consider using `ir.attachment` for more robust file management.
    application_form = fields.Binary(string="Application Form", attachment=False)
    application_form_filename = fields.Char(string="Application Form Filename")

    # Status field
    # This is a Selection field to choose from a predefined list of statuses.
    status = fields.Selection([
        ('applicant', 'Applicant'),          # A regular attendee who has applied for membership
        ('regular_attendee', 'Regular Attendee'), # An attedee who regularly attends service but has not applied for membership (yet)
        ('member', 'Member'),                # An attendee who has completed the application process
        ('past_member', 'Past Member')       # A member who has left the church
    ], string="Status", default='member', tracking=True) # Default status is 'member', tracking adds to chatter

    designation = fields.Selection([
        ('member', 'Member'),                # A regular member of the church
        ('pastor', 'Pastor'),                # A pastor in the church
        ('deacon', 'Deacon'),                # A deacon in the church
        ('elder', 'Elder'),                  # An elder in the church
    ], string="Designation", default='member', tracking=True) # Default designation is 'member', tracking adds to chatter

    is_active = fields.Boolean(string="Is Active", default=True) # Indicates if the member/attendee is active

    date_of_baptism = fields.Date(string="Baptism Date")
    date_of_first_attendance = fields.Date(string="Date First Attended")
    # Date of Membership field
    # This is a Date field to store the date when the person became a member.
    date_of_membership = fields.Date(string="Right Hand Of Fellowship")

    # Reason for leaving field
    # This is a Text field for a multi-line explanation.
    reason_for_leaving = fields.Text(string="Reason for Leaving")

    # inherited from res.partner
    name = fields.Char(related="partner_id.name", inherited=True, readonly=False)
    email = fields.Char(related="partner_id.email", inherited=True, readonly=False)
    phone = fields.Char(related="partner_id.phone", inherited=True, readonly=False)
    mobile = fields.Char(related="partner_id.mobile", inherited=True, readonly=False)