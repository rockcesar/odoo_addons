# -*- coding: utf-8 -*-
from odoo import models, fields, api, SUPERUSER_ID
from odoo.tools.translate import _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

from py_translator import Translator
import sys

import base64

class Translator_online(models.Model):
    _name = "translator"
    _description = "Translator"

    name = fields.Char("Name of term to translate")
    text = fields.Text("Text to be translated")
    term_translated = fields.Text("Term translated")
    name_of_file = fields.Binary("File to translate")
    language = fields.Char("Language to translate")
    type_of_input = fields.Char("Type of input")

    @api.one
    def translate(self):
        #_logger.info("1234567890")

        proxy = {
            'socks': 'socks://localhost:9050',
            'socks': 'socks://localhost:9050',
        }

        ROTATING_PROXY_LIST = {
            'socks': 'socks://localhost:9050'
        }

        text = ""

        if self.type_of_input == "using_file":
            #translator_file = base64.decode(self.name_of_file)
            text = str(base64.b64decode(self.name_of_file).decode("utf-8")).replace('\\ n', '\n').replace('\\n', '\n')
            #file = open(translator_file, "r")
            #text = file.read()
        else:
            text = self.text

        s = Translator(proxies=proxy).translate(text=text, dest=self.language).text

        self.term_translated = s
