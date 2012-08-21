# -*- coding: utf-8  -*-
#
# Copyright (C) 2012 Ben Kurtovic <ben.kurtovic@verizon.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import unicode_literals

"""
`mwparserfromhell <https://github.com/earwig/mwparserfromhell>`_ (the MediaWiki
Parser from Hell) is a Python package that provides an easy-to-use and
outrageously powerful parser for `MediaWiki <http://mediawiki.org>`_ wikicode.
"""

__author__ = "Ben Kurtovic"
__copyright__ = "Copyright (C) 2012 Ben Kurtovic"
__license__ = "MIT License"
__version__ = "0.1.dev"
__email__ = "ben.kurtovic@verizon.net"

from . import nodes, parser, smart_list, string_mixin, wikicode

parse = lambda text: parser.Parser(text).parse()
parse.__doc__ = """Short for mwparserfromhell.parser.Parser(text).parse()."""
