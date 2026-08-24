# Part of Calendar Booking. See LICENSE file for full copyright and licensing details.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class CalendarBookingTypeSlot(models.Model):
    _name = "calendar.booking.type.slot"
    _description = "Booking Type Schedule Slot"
    _order = "weekday, start_hour, id"

    appointment_type_id = fields.Many2one(
        "calendar.booking.type",
        string="Booking Type",
        required=True,
        ondelete="cascade",
        index=True,
    )
    weekday = fields.Selection(
        [
            ("1", "Monday"),
            ("2", "Tuesday"),
            ("3", "Wednesday"),
            ("4", "Thursday"),
            ("5", "Friday"),
            ("6", "Saturday"),
            ("7", "Sunday"),
        ],
        string="Weekday",
        required=True,
    )
    slot_type = fields.Selection(
        [
            ("recurring", "Recurring"),
            ("single", "Single"),
        ],
        string="Slot Type",
        default="recurring",
        required=True,
    )
    start_hour = fields.Float(string="Start Hour", required=True)
    end_hour = fields.Float(string="End Hour", required=True)
