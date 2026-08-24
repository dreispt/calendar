# Part of Calendar Booking. See LICENSE file for full copyright and licensing details.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_booking_location = fields.Boolean(
        string="Is Booking Location",
        default=False,
        help="This partner can be selected as a booking location.",
    )
