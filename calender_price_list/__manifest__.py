{
    'name': 'Calendar Pricelist',
    'version': '17.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Create and edit pricelist rules from a calendar in Sales and Point of Sale',
    'description': """
Calendar Pricelist for Odoo 17
=============================
View pricelist rule validity periods in a calendar and create new rules
directly by selecting a date. Choose the pricelist, configure the pricing
rule and validity period, then save using the standard Odoo rule form.

Features
--------
* Calendar view of dated pricelist rules, colored by pricelist.
* Create rules from the calendar using the full pricelist rule form.
* Open existing calendar entries to review and edit rules.
* Calender Price menus under Products in Sales and Point of Sale.
* Standard Odoo pricelist search and access permissions.

Requires Sales, Point of Sale and enabled Pricelists. Set start and end
dates for rules intended to appear with a validity period in the calendar.
""",
    'author': 'Mitchel Admin',
    'maintainer': 'Mitchel Admin',
    'support': 'erpmitchellodoo@gmail.com',
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'depends': ['sale_management', 'point_of_sale'],
    'data': ['views/product_pricelist_item_views.xml'],
    'installable': True,
    'application': False,
}
