# Part of Calendar Booking. See LICENSE file for full copyright and licensing details.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


def _tz_get(self):
    """Return the canonical list of IANA timezones."""
    import pytz

    return [(tz, tz) for tz in sorted(pytz.all_timezones)]


class CalendarBookingType(models.Model):
    _name = "calendar.booking.type"
    _description = "Booking Type"
    _inherit = ["mail.thread", "mail.activity.mixin", "calendar.booking.mixin"]
    _order = "name, id"

    name = fields.Char(string="Name", required=True, translate=True)
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        default=lambda self: self.env.company,
    )
    appointment_duration = fields.Float(
        string="Duration",
        default=1.0,
        help="Default duration for each booking (in hours).",
    )
    appointment_tz = fields.Selection(
        _tz_get,
        string="Timezone",
        default="UTC",
        required=True,
    )
    slot_creation_interval = fields.Float(
        string="Slot Creation Interval",
        default=0.5,
        help="Interval between generated time slots (in hours).",
    )
    resource_calendar_id = fields.Many2one(
        "resource.calendar",
        string="Working Hours",
        help="Default calendar used to compute available time slots.",
    )
    resource_ids = fields.Many2many(
        "resource.resource",
        "calendar_booking_type_resource_rel",
        "booking_type_id",
        "resource_id",
        string="Resources",
    )
    location_id = fields.Many2one(
        "res.partner",
        string="Location",
        help="Location where this booking type takes place.",
    )
    slot_ids = fields.One2many(
        "calendar.booking.type.slot",
        "appointment_type_id",
        string="Schedule Slots",
        help="Recurring or single-slot availability for this booking type.",
    )
