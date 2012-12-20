# coding: utf-8
#
# Copyright YEAR Foo Bar
# Powered by cyclone
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import cyclone.escape
import cyclone.locale
import cyclone.web

from twisted.internet import defer
from twisted.python import log

from ThereBeDocs.utils import BaseHandler
from ThereBeDocs.utils import TemplateFields


class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html", hello='world', awesome='bacon')
        # another option would be
        # fields = {'hello': 'world', 'awesome': 'bacon'}
        # self.render('index.html', **fields)

    def post(self):
        tpl_fields = TemplateFields()
        tpl_fields['post'] = True
        tpl_fields['ip'] = self.request.remote_ip
        # you can also fetch your own config variables defined in
        # ThereBeDocs.conf using
        # self.settings.raw.get('section', 'parameter')
        tpl_fields['mysql_host'] = self.settings.raw.get('mysql', 'host')
        self.render("post.html", fields=tpl_fields)


class LangHandler(BaseHandler):
    def get(self, lang_code):
        if lang_code in cyclone.locale.get_supported_locales():
            self.set_secure_cookie("lang", lang_code)

        self.redirect(self.request.headers.get("Referer",
                                               self.get_argument("next", "/")))

