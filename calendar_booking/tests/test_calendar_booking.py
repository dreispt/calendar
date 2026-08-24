# Part of Calendar Booking. See LICENSE file for full copyright and licensing details.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo.tests.common import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestCalendarBooking(TransactionCase):
    def test_create_booking_type(self):
        booking_type = self.env["calendar.booking.type"].create(
            {
                "name": "Test Booking",
                "appointment_duration": 1.0,
                "appointment_tz": "UTC",
            }
        )
        self.assertTrue(booking_type)
        self.assertEqual(booking_type.appointment_duration, 1.0)
