#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HAPI Smart Module v2.1.2
Release: April 2017 Beta Milestone

First attempt of implement small log functionality.
-> Standard option has memory leak when running multithreaded systems.
--> This is a testing!

This module is really simple and small. It should be improved if sticking to it.

Copyright 2016 Maya Culpa, LLC

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import print_function
import datetime

class Log(object):
    """Hold information about logging."""

    def __init__(self, log_file):
        """Initialize object with initial information such as file for writing."""
        self.log_file = log_file
        self.mask = "{date} - {name} - {log_type} - {string}"

    def build_string(self, log_type, information):
        """Build string with mask and return it."""
        string = self.mask.format(
            date=datetime.datetime.now(),
            name=self.log_file,
            log_type=log_type,
            string=str(information),
        )
        return str(string)

    def info(self, format, *values):
        """Append INFO in format % values to file."""
        string = self.build_string("INFO", format % values)
        with open(self.log_file, "a") as log:
            log.write(string + "\n")
        print(string)

    def exception(self, format, *values):
        """Append ERROR in format % values to file."""
        string = self.build_string("[!!] ERROR", format % values)
        with open(self.log_file, "a") as log:
            log.write(string + "\n")
        print(string)
