###################################################################################
# 
#    Copyright (C) Cetmix OÜ
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU LESSER GENERAL PUBLIC LICENSE as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

{
    "name": "Quickbook Sync",
    "version": "16.0.1.0.0",
    "summary": """
    Sync Quickbook Data
""",
    "author": "Destiny Solutions",
    "category": "Productivity",
    "license": "LGPL-3",
    "depends": ["web", 'base', 'sale'],
    "data": [
        'views/quickbook_sync.xml',
        'views/sale_order.xml',
        'views/account_move.xml',
        'views/res_config_setting.xml',
    ],

    "installable": True,
    "application": False,
    "auto_install": False,
}
