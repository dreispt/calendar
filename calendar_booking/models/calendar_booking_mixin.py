# Part of Calendar Booking. See LICENSE file for full copyright and licensing details.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import models


class CalendarBookingMixin(models.AbstractModel):
    _name = "calendar.booking.mixin"
    _description = "Calendar Booking Mixin"
