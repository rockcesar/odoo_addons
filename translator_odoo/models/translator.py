# -*- coding: utf-8 -*-
from odoo import models, fields, api, SUPERUSER_ID
from odoo.tools.translate import _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

from py_translator import Translator
import sys

import base64

class Languages(models.Model):
    _name = "language"
    _description = "Languages"
    _order = "name asc"

    name = fields.Char("Language name")
    code = fields.Char("Language code")
    uses = fields.Integer("Number of uses")

class Translator_online(models.Model):
    _name = "translator"
    _description = "Translator"

    name = fields.Char("Your name")
    email = fields.Char("Your email")
    text = fields.Text("Text to be translated")
    term_translated = fields.Text("Term translated")
    name_of_file = fields.Binary("File to translate")
    language = fields.Many2one("language", string="Languages to translate")
    #language = fields.Selection([('es', 'spanish'), ('en', 'english'), ('af', 'afrikaans'), ('am', 'amharic'), ('ar', 'arabic'), ('az', 'azerbaijani'), ('be', 'belarusian'), ('bg', 'bulgarian'), ('bn', 'bengali'), ('bs', 'bosnian'), ('ca', 'catalan'), ('ceb', 'cebuano'), ('co', 'corsican'), ('cs', 'czech'), ('cy', 'welsh'), ('da', 'danish'), ('de', 'german'), ('el', 'greek'), ('eo', 'esperanto'), ('et', 'estonian'), ('eu', 'basque'), ('fa', 'persian'), ('fi', 'finnish'), ('fil', 'Filipino'), ('fr', 'french'), ('fy', 'frisian'), ('ga', 'irish'), ('gd', 'scots gaelic'), ('gl', 'galician'), ('gu', 'gujarati'), ('ha', 'hausa'), ('haw', 'hawaiian'), ('he', 'Hebrew'), ('hi', 'hindi'), ('hmn', 'hmong'), ('hr', 'croatian'), ('ht', 'haitian creole'), ('hu', 'hungarian'), ('hy', 'armenian'), ('id', 'indonesian'), ('ig', 'igbo'), ('is', 'icelandic'), ('it', 'italian'), ('iw', 'hebrew'), ('ja', 'japanese'), ('jw', 'javanese'), ('ka', 'georgian'), ('kk', 'kazakh'), ('km', 'khmer'), ('kn', 'kannada'), ('ko', 'korean'), ('ku', 'kurdish (kurmanji)'), ('ky', 'kyrgyz'), ('la', 'latin'), ('lb', 'luxembourgish'), ('lo', 'lao'), ('lt', 'lithuanian'), ('lv', 'latvian'), ('mg', 'malagasy'), ('mi', 'maori'), ('mk', 'macedonian'), ('ml', 'malayalam'), ('mn', 'mongolian'), ('mr', 'marathi'), ('ms', 'malay'), ('mt', 'maltese'), ('my', 'myanmar (burmese)'), ('ne', 'nepali'), ('nl', 'dutch'), ('no', 'norwegian'), ('ny', 'chichewa'), ('pa', 'punjabi'), ('pl', 'polish'), ('ps', 'pashto'), ('pt', 'portuguese'), ('ro', 'romanian'), ('ru', 'russian'), ('sd', 'sindhi'), ('si', 'sinhala'), ('sk', 'slovak'), ('sl', 'slovenian'), ('sm', 'samoan'), ('sn', 'shona'), ('so', 'somali'), ('sq', 'albanian'), ('sr', 'serbian'), ('st', 'sesotho'), ('su', 'sundanese'), ('sv', 'swedish'), ('sw', 'swahili'), ('ta', 'tamil'), ('te', 'telugu'), ('tg', 'tajik'), ('th', 'thai'), ('tl', 'filipino'), ('tr', 'turkish'), ('uk', 'ukrainian'), ('ur', 'urdu'), ('uz', 'uzbek'), ('vi', 'vietnamese'), ('xh', 'xhosa'), ('yi', 'yiddish'), ('yo', 'yoruba'), ('zh-cn', 'chinese (simplified)'), ('zh-tw', 'chinese (traditional)'), ('zu', 'zulu')], "Language to translate")
    type_of_input = fields.Selection([('using_text_field', 'Using Text Field'), ('using_file', 'Using File')], "Type of input")

    @api.one
    def translate(self):
        proxy = {
            'socks': 'socks://localhost:9050',
            'socks': 'socks://localhost:9050',
        }

        ROTATING_PROXY_LIST = {
            'socks': 'socks://localhost:9050'
        }

        text = ""

        if self.type_of_input == "using_file":
            text = str(base64.b64decode(self.name_of_file).decode("utf-8")).replace('\\ n', '\n').replace('\\n', '\n')
        else:
            text = self.text

        s = Translator(proxies=proxy).translate(text=text, dest=self.language.code).text

        self.term_translated = s
        
    @api.one
    def translate_to_website(self):
        proxy = {
            'socks': 'socks://localhost:9050',
            'socks': 'socks://localhost:9050',
        }

        ROTATING_PROXY_LIST = {
            'socks': 'socks://localhost:9050'
        }

        text = ""

        if self.type_of_input == "using_file":
            text = self.name_of_file.decode("utf-8").replace('\\ n', '\n').replace('\\n', '\n')
        else:
            text = self.text

        s = Translator(proxies=proxy).translate(text=text, dest=self.language.code).text

        self.term_translated = s
        
        return self.term_translated
