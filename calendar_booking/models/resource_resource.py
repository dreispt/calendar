# Part of Calendar Booking. See LICENSE file for full copyright and licensing details.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ResourceResource(models.Model):
    _inherit = "resource.resource"

    booking_type_ids = fields.Many2many(
        "calendar.booking.type",
        "calendar_booking_type_resource_rel",
        "resource_id",
        "booking_type_id",
        string="Booking Types",
    )
