# Copyright (c) 2013, firsterp and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	if not filters: filters = {}

	columns = get_columns()

	# data = get_bom_stock(filters)
	data = get_all_boms()
	
	return columns, data

def get_columns():
	"""return columns"""
	columns = [
		_("item") + ":Link/Item:150",
		_("name") +  ":Link/BOM:150"
	]

	return columns

def get_all_boms():
	return frappe.get_list("BOM",filters={'is_active':1,'docstatus':1},fields={"name","item"})
