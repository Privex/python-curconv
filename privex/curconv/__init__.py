"""
Python Currency Converter CLI
Official Repo: https://github.com/Privex/python-curconv
License: X11 / MIT


Copyright::

    +===================================================+
    |                 © 2021 Privex Inc.                |
    |               https://www.privex.io               |
    +===================================================+
    |                                                   |
    |        Python Currency Converter CLI              |
    |        License: X11/MIT                           |
    |                                                   |
    |        Core Developer(s):                         |
    |                                                   |
    |          (+)  Chris (@someguy123) [Privex]        |
    |                                                   |
    +===================================================+
    
    Python Currency Converter CLI - A small CLI tool for quick currency conversions on the command line
    Copyright (c) 2021    Privex Inc. ( https://www.privex.io )
    
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation
    files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy,
    modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of
    the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
    WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
    OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
    OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    
    Except as contained in this notice, the name(s) of the above copyright holders shall not be used in advertising or
    otherwise to promote the sale, use or other dealings in this Software without prior written authorization.

"""
import logging
# logging.basicConfig(level=logging.DEBUG, force=True)
name = 'curconv'
from privex.curconv.version import VERSION

VERSION = VERSION
from privex.curconv import settings
from privex.curconv.app import main, convert, str_convert, str_extract, conv_adapter
from privex.curconv.base import *
