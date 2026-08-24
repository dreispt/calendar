# Part of Calendar Booking. See LICENSE file for full copyright and licensing details.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "Calendar Booking",
    "version": "19.0.1.0.0",
    "category": "Calendar",
    "license": "LGPL-3",
    "summary": "Minimal LGPL booking platform for calendar appointments and resource booking",
    "author": "OSI",
    "website": "https://github.com/OSI-SH/barberhood",
    "depends": [
        "calendar",
        "resource",
        "hr",
        "product",
        "mail",
        "portal",
        "web",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/calendar_booking_security.xml",
        "views/calendar_booking_type_views.xml",
        "views/calendar_booking_menus.xml",
        "data/calendar_booking_data.xml",
    ],
    "demo": [
        "demo/calendar_booking_demo.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
