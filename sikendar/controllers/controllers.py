# -*- coding: utf-8 -*-
import base64

import werkzeug
from odoo import http
from odoo.http import request
from datetime import datetime
import re
class MyModule(http.Controller):

    @http.route('/hotel', type='http', auth='user', website=True)
    def sale_details(self, **kwargs):
        rooms = request.env['res.partner'].sudo().search([])
        return request.render('sikendar.sale_details_page', {'room': rooms,'description':rooms})

    @http.route('/order', type='http', methods=['POST'],auth="public", website=True, csrf=False)
    def test_path (self, **kw):

        name = request.env['sale.order'].search([])[0].name
        number = re.findall(r'\d+', name)
        if not number:
            number = 1
        else:
            number = int(number[-1]) + 1
        try:
            if kw['Super urgent let us know if your order is urgent'] == 'Yes':
                check = True
            else:
                check = False
        except:
            check = False
        partner = request.env['res.users'].search([('id', '=', request.session.uid)])
        sale = request.env['sale.order'].create({
            'name': "Order/" + str(number),
            'partner_id': partner.partner_id.id,
            'height':kw['height'] or 0,
            'width':kw['number'] or 0,
            'fabric':kw['pabric'] or '',
            'placement':kw['placement'] or '',
            'required_format': kw['Required Format'] or '',
            'numberofcolors': kw['colors'],
            'add_details': kw['Additional Details'] or '',
            'super_urgent': check,

        })

        # image upload start
        if sale:

            attached_files = request.httprequest.files.getlist('image_uploaded')
            if attached_files:
                for i in attached_files:
                    id = request.env['ir.attachment'].create({
                        'res_model': 'sale.order',
                        'type': 'binary',
                        'name': i.filename,
                        'res_id': sale.id,
                        'res_field': 'image_uploaded',
                        'store_fname': i.filename,
                        'datas': base64.encodestring(i.read())
                    })

                    sale.update({
                        'image_uploadedd': [(4, id.id)]
                    })
        return werkzeug.utils.redirect('/')