"""LICENSE
Copyright 2019 Hermann Krumrey <hermann@krumreyh.com>

This file is part of fe3h-checklist.

fe3h-checklist is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

fe3h-checklist is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with fe3h-checklist.  If not, see <http://www.gnu.org/licenses/>.
LICENSE"""

from enum import Enum


class Factions(Enum):
    """
    Enumeration modelling the different factions
    """
    BLACK_EAGLE = "Black Eagle House"
    BLUE_LION = "Blue Lion House"
    GOLDEN_DEER = "Golden Deer House"
    CHURCH_OF_SEIROS = "Church of Seiros"
    NONE = "None"
