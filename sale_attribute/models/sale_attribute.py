# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleAttribute(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('draft', 'Quotation'),
        ('approving_managers', 'Approving Manager'),
        ('accounts', 'Accounts'),
        ('approved', 'Approved'),
        ('sent', 'Quotation Sent'),
        ('cust_approve', 'Approved By Customer'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    def action_confirm(self):
        self.state = 'cust_approve'

