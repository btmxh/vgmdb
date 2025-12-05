# -*- coding: UTF-8 -*-
import os
import unittest

from vgmdb.parsers import orglist

base = os.path.dirname(__file__)


class TestOrgList(unittest.TestCase):
    def setUp(self):
        pass

    def test_list(self):
        list_code = open(os.path.join(base, "orglist.html"), "r").read()
        olist = orglist.parse_page(list_code)

        self.assertEqual(27, len(list(olist["orgs"].keys())))
        self.assertEqual("org/442", olist["orgs"]["#"][0]["link"])
        self.assertEqual("<echo>PROJECT", olist["orgs"]["#"][0]["names"]["en"])
        self.assertEqual(16, len(olist["orgs"]["#"]))
        self.assertEqual("org/860", olist["orgs"]["#"][-1]["link"])
        self.assertEqual(1, len(olist["orgs"]["W"][1]["formerly"]))
        self.assertEqual(
            "Disneyland Records", olist["orgs"]["W"][1]["formerly"][0]["names"]["en"]
        )
        self.assertEqual("Warner Music Japan", olist["orgs"]["W"][3]["names"]["en"])
        self.assertEqual(3, len(olist["orgs"]["W"][3]["imprints"]))
        self.assertEqual(
            "A'zip Music", olist["orgs"]["W"][3]["imprints"][0]["names"]["en"]
        )
        self.assertEqual("org/95", olist["orgs"]["W"][3]["subsidiaries"][0]["link"])
        self.assertEqual("org/13", olist["orgs"]["W"][3]["formerly"][0]["link"])


if __name__ == "__main__":
    unittest.main()
