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

from typing import List
from fe3h_checklist.data.Names import Names
from fe3h_checklist.data.Factions import Factions


class CharacterInfo:
    """
    Class that stores information about a character
    """

    def __init__(
            self,
            name: Names,
            faction: Factions,
            b_rank_supports: List[Names],
            a_rank_supports: List[Names],
            s_rank_supports: List[Names]
    ):
        """
        Initializes the CharacterInfo class
        :param name: The name of the character
        :param faction: The character's faction
        :param b_rank_supports: The list of B-rank supports or the character
        :param a_rank_supports: The list of A-rank supports or the character
        :param s_rank_supports: The list of S-rank supports or the character
        """
        self.name = name
        self.faction = faction
        self.b_rank_supports = b_rank_supports
        self.a_rank_supports = a_rank_supports
        self.s_rank_supports = s_rank_supports

    def __repr__(self):
        """
        :return: A string representation of the class
        """
        return "CharacterInfo(Names.{}, Factions.{}, {}, {}, {})".format(
            self.name.name,
            self.faction.name,
            self._stringify_names(self.b_rank_supports),
            self._stringify_names(self.a_rank_supports),
            self._stringify_names(self.s_rank_supports)
        )

    @staticmethod
    def _stringify_names(names: List[Names]) -> str:
        """
        Generates a string representing a list of names
        :param names: The names to turn into a string
        :return: The generated string
        """
        name_list = ""
        for name in names:
            name_list += "Names.{}, ".format(name.name)
        name_list = name_list[0:-2]  # Remove last ', '
        return "[{}]".format(name_list)
