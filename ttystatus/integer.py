# Copyright 2011  Lars Wirzenius
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


import ttystatus


class Integer(ttystatus.Widget):

    '''Display a value as an integer.'''

    static_width = False

    def __init__(self, key):
        self._key = key
        self.value = None

    def render(self, width):
        try:
            return str(int(self.value))
        except (TypeError, ValueError):
            return '#'

    def update(self, master):
        self.value = master[self._key]
