# -*- coding: utf-8 -*-
import base64

import werkzeug
from odoo import http
from odoo.http import request
from datetime import datetime
import re

class MyModule(http.Controller):
    @http.route('/place_quotation', type='http', auth='public', website=True)
    def sale_detailss(self, **kwargs):
        rooms = request.env['res.partner'].sudo().search([])
        return request.render('sikendar.place_quotation_page', {'room': rooms,'description':rooms})

    @http.route('/place_vector', type='http', auth='public', website=True)
    def vector_detailss(self, **kwargs):
        rooms = request.env['res.partner'].sudo().search([])
        return request.render('sikendar.place_vector_page', {'room': rooms,'description':rooms})


    @http.route('/place_quotation1', type='http', methods=['POST'],auth="public", website=True, csrf=False)
    def test_patha (self, **kw):
        now = datetime.now()
        Attachments = request.env['ir.attachment']
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
            check = True
        sale = request.env['sale.order'].create({
            'name': "Quotation/" + str(number),
            'partner_id': 1,
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

    @http.route('/place_vector1', type='http', methods=['POST'],auth="public", website=True, csrf=False)
    def test_pathaa (self, **kw):
        now = datetime.now()
        Attachments = request.env['ir.attachment']
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
            check = True
        sale = request.env['sale.order'].create({
            'name': "Vector/"+str(number),
            'partner_id': 1,
            'required_format': kw['Required Format'] or '',
            'numberofcolors':kw['colors'],
            'add_details':kw['Additional Details'] or '',
            'super_urgent': check,

        })

        #image upload start
        if sale:

            attached_files = request.httprequest.files.getlist('image_uploaded')
            if attached_files:
                for i in attached_files:
                    id = request.env['ir.attachment'].create({
                        'res_model':'sale.order',
                        'type': 'binary',
                        'name': i.filename,
                        'res_id': sale.id,
                        'res_field': 'image_uploaded',
                        'store_fname': i.filename,
                        'datas':base64.encodestring(i.read())
                    })

                    sale.update({
                        'image_uploadedd':[(4,id.id)]
                    })
        return werkzeug.utils.redirect('/')

        #image upload end


        #############neechay wala uncomment karna hai

        # name = request.env['sale.order'].search([])[0].name
        # number = re.findall(r'\d+', name)
        # if not number:
        #     number = 1
        # else:
        #     number = int(number[-1]) + 1
        # try:
        #     if kw['Super urgent let us know if your order is urgent'] == 'Yes':
        #         check = True
        #     else:
        #         check = False
        # except:
        #     check = True
        # request.env['sale.order'].create({
        #     'name': "Vector/"+str(number),
        #     'image_uploadedd': base64.encodestring(upload_file.read()),
        #     'partner_id': 1,
        #     'required_format': kw['Required Format'] or '',
        #     'numberofcolors':kw['colors'],
        #     'add_details':kw['Additional Details'] or '',
        #     'super_urgent': check,
        #
        # })
