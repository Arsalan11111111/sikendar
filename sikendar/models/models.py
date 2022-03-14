# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'res.partner'

    card_number = fields.Char("Card Number")
    exp_card = fields.Char("Card Expiry")
    cvv = fields.Char("CVV Card")
    attachment = fields.Binary(string='attachment', attachment=True)



class SaleOrder(models.Model):
    _inherit = "sale.order"

    image_uploadedd = fields.Many2many('ir.attachment', string="Image", attachment=True,store=True)
    required_format = fields.Char("Required Format")
    numberofcolors = fields.Integer("Number of colors")
    placement = fields.Char("Placement")
    add_details = fields.Text("Additional Details")
    super_urgent = fields.Boolean("Super Urgent")
    width = fields.Float("Width")
    height = fields.Float("Height")
    fabric = fields.Selection([('Twill', 'Twill'),
                               ('Polyster', 'Polyster'),
                               ('Cotton', 'Cotton'),
                               ('Canvas', 'Canvas')],
                              string="Fabric",
                              default="Twill")


    # fields.Many2many('ir.attachment', string="Image")