# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'PiNetwork Hello World for Odoo',
    'category': 'Website/Website',
    'sequence': 54,
    'summary': 'PiNetwork Hello World',
    'version': '2.1',
    'description': """
PiNetwork Hello World for Odoo
-----------------

This simple application show a PiNetwork Hello World example in the root (/) of the Odoo Server.

Pi is a new digital currency developed by Stanford PhDs, with over 8 million members worldwide (at September 2020). To claim your Pi, follow this link https://minepi.com/rockcesar and use my username (rockcesar) as your invitation code.

I'm developing Pi Apps for the Pi Network Apps Platform, also, watch this video

https://youtu.be/zMUKTWLN5Uk

Referal link: https://minepi.com/rockcesar
Referal code: rockcesar

To put it work, use Odoo 13.

Test the app here: https://developers.minepi.com/about-app

Documentation: https://developers.minepi.com/doc/javascript

Pi Developers: https://developers.minepi.com/""",
    'depends': ['website'],
    'data': [
        'views/website_pinetwork_templates.xml',
    ],
    'qweb': [],
    'installable': True,
    'auto_install': True,
}
