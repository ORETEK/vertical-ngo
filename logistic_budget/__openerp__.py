# -*- coding: utf-8 -*-
#
#    Author: Joël Grand-Guillaume, Jacques-Etienne Baudoux, Guewen Baconnier
#    Copyright 2013-2014 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
{"name": "Logistics Budget",
 "version": "1.0",
 "author": "Camptocamp",
 "license": "AGPL-3",
 "category": "Purchase Management",
 'complexity': "normal",
 "images": [],
 "website": "http://www.camptocamp.com",
 "description": """
Logisitic budget
================

XXX rewrite this

This module adds a notion of budget on logistic requisition.
Each requisition lines have now a budget holder and a budget Value.

Requisiton must be approves by budget manager.

If budget is exceeded requisition flow is block unitl adaptation of price
or budget.

""",
 "depends": ["logistic_requisition",
             "sale_exceptions",
             "sale_stock",
             ],
 "demo": [],
 "data": ["view/logistic_requisition.xml",
          "view/sale_order.xml",
          "view/report_logistic_requisition.xml",
          "data/exceptions.xml",
          ],
 "auto_install": False,
 'installable': True,
 }
