# -*- coding: utf-8 -*-
# Copyright (C) 2013  Fabio Falcinelli
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import logging
from logging import handlers
import os

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

__author__ = 'fabio'

#monkey patch scheme to support ws and wss
ws_scheme = ["ws", "wss"]
for scheme in (urlparse.uses_relative,
               urlparse.uses_netloc,
               urlparse.non_hierarchical,
               urlparse.uses_params,
               urlparse.uses_query,
               urlparse.uses_fragment):
    scheme.extend(ws_scheme)
