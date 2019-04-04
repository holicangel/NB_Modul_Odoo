{
    'name': 'Nusatama Sale Modul',
    'author': 'Handy',
    'version': '0.1',
    'depends': [
            'sale',
        
    ],
    'data': [
                'views/quotation_form.xml', # selalu gunakan koma
                'views/nb_sale_order_report.xml',
                'views/paperformat.xml',
        #     'views/kg_invoice_report.xml', # selalu gunakan koma
        #     'views/sale_order_report.xml', # selalu gunakan koma
        #     'views/invoice_report.xml', # selalu gunakan koma
        #     'views/report_invoice_document.xml', # selalu gunakan koma
        # selalu gunakan koma
            
    ],
    'qweb': [
        #     'views/sale_order_report.xml',
    ],
    'sequence': 1,
    'auto_install': False,
    'installable': True,
    'application': True,
    'category': 'Academy Day 1',
    'summary': 'Catat penjualan sederhana',
    'license': 'OPL-1',
    'website': 'https://www.arkana.co.id/',
    'description': """
'Nusatama Sale Modul'
=============

Modul ini digunakan untuk :

1. ...

2. ...

# Deskripsi ini hanya akan terlihat jika application = False

""",

}