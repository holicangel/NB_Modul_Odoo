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
                'views/nb_invoice_report.xml',
                'views/nb_payment_receipt.xml',
                'views/paperformat.xml',
                'views/dateformat.xml',
                'views/nb_header.xml',
                'views/nb_footer.xml',
             
       
      
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