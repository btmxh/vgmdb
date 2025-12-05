# -*- coding: UTF-8 -*-
import os
import unittest

from vgmdb.parsers import eventlist

base = os.path.dirname(__file__)


class TestEventList(unittest.TestCase):
    def setUp(self):
        pass

    def test_list(self):
        list_code = open(os.path.join(base, "eventlist.html"), "r").read()
        elist = eventlist.parse_page(list_code)

        self.assertEqual(25, len(list(elist["events"].keys())))
        self.assertEqual("event/92", elist["events"]["1998"][0]["link"])
        self.assertEqual(
            "Tokyo Game Show 1998 Spring", elist["events"]["1998"][0]["names"]["en"]
        )
        self.assertEqual(
            "コミックマーケット54", elist["events"]["1998"][1]["names"]["ja"]
        )
        self.assertEqual("C55", elist["events"]["1998"][2]["shortname"])
        self.assertEqual("1998-03-20", elist["events"]["1998"][0]["startdate"])
        self.assertEqual("1998-03-22", elist["events"]["1998"][0]["enddate"])
        self.assertEqual("2000-04-23", elist["events"]["2000"][0]["startdate"])
        self.assertEqual("2000-04-23", elist["events"]["2000"][0]["enddate"])
        self.assertFalse("shortname" in elist["events"]["2001"][1])


if __name__ == "__main__":
    unittest.main()
