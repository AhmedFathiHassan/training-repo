# Copyright (c) 2024, Ahmed Fathi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class LearnFrappe(Document):
	def before_save(self):
		self.total_cost = int(self.article_cost) + int(self.delivery_cost)