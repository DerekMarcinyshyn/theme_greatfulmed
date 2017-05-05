# -*- coding: utf-8 -*-

{
    'name': 'Greatful Med theme',
    'description': 'Greatful Med Cannabis Society, Vancouver, BC.',
    'version': '1.0',
    'author': 'Derek Marcinyshyn',
    'website': 'https://www.monasheemountainmultimedia.com',

    'data': [
        'views/theme_greatfulmed_templates.xml',
        'views/assets.xml'
    ],
    'qweb': [
        'static/src/xml/pos.xml'
    ],
    'category': 'Theme/Ecommerce',
    'depends': [
        'website',
        'sale',
        'point_of_sale'
    ],
    'application': True,
}
