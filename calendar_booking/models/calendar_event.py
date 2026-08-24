# Part of Calendar Booking. See LICENSE file for full copyright and licensing details.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    appointment_type_id = fields.Many2one(
        "calendar.booking.type",
        string="Appointment Type",
        index=True,
        tracking=True,
    )
    appointment_status = fields.Selection(
        [
            ("draft", "Draft"),
            ("requested", "Requested"),
            ("booked", "Booked"),
            ("attended", "Attended"),
            ("no_show", "No Show"),
            ("cancelled", "Cancelled"),
        ],
        string="Appointment Status",
        default="draft",
        index=True,
    )
    appointment_booker_id = fields.Many2one(
        "res.partner",
        string="Booker",
        index=True,
    )
    appointment_resource_ids = fields.Many2many(
        "resource.resource",
        "calendar_event_booking_resource_rel",
        "event_id",
        "resource_id",
        string="Resources",
    )
    appointment_resource_id = fields.Many2one(
        "resource.resource",
        string="Resource",
        index=True,
    )
    is_preference = fields.Boolean(
        string="Staff Preference",
        help="The customer selected a specific staff member.",
    )
