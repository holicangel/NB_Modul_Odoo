{
    'name': 'Nusatama Sales Modul',
    'author': 'Handy',
    'version': '0.1',
    'depends': [
            'sale',
            'account',
            'sale_order_line_sequence',
            'num_to_words',
            'account_invoice_line_number',
            
        
    ],
    'data': [
                'views/wizard.xml',
                'views/button.xml',
                'views/nb_ir_sequence_data.xml',
                'views/quotation_form.xml', # selalu gunakan koma
                'views/paperformat.xml',
                'views/paperformat_invoice.xml',
                'views/paperformat_empat.xml',
                'views/nb_sale_order_report.xml',
                'views/nb_invoice_report.xml',
                'views/nb_payment_receipt.xml',               
                'views/dateformat.xml',
                'views/nb_header.xml',
                'views/nb_footer.xml',
                # 'views/nb_payment_receipt_form.xml',
                'views/nb_invoice_form.xml',
             
       
      
        # selalu gunakan koma
            
    ],
    'qweb': [
        #     'views/sale_order_report.xml',
    ],
    'sequence': 1,
    'auto_install': False,
    'installable': True,
    'application': True,
    'category': 'Custom Module',
    'summary': 'Aplikasi Untuk Nusatama Untuk Modifikasi Sales dan Report Odoo',
    'license': 'OPL-1',
    'website': 'https://www.nusatama.com',
    'description': """
'Nusatama Sales Module'
=============

Modul ini digunakan untuk :

Modifikasi untuk modul Sales pada Odoo dan Custom Report Quotation,SO,Invoice & Payment Receipt Untuk PT. Nusatama Berkah


""",

}