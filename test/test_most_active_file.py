import unittest
from src.most_active_cookie import preprocess_log_file, get_active_cookie, LOG_FILE_COLUMNS

class TestMostActiveCookie(unittest.TestCase):

        def setUp(self):
            self.bad_timestamp_file = "cookie_log_bad_timestamp.csv"
            self.bad_header_format_file = "cookie_log_wrong_header_format.csv"
            self.test_date = "2018-12-08"
            self.wrong_test_file = "cookie.csv"
            self.cookie_list = ["AtY0laUfhglK3lC7", "SAZuXPGUrfbcn5UA", "5UAVanZf6UtGyKVS",
                                "AtY0laUfhglK3lC7","SAZuXPGUrfbcn5UA"]
            self.correct_cookie_list = ["SAZuXPGUrfbcn5UA", "AtY0laUfhglK3lC7",]

        def test_preprocess_log_file(self):

            # TestCase1
            with self.assertRaises(FileNotFoundError):
                preprocess_log_file(self.wrong_test_file, self.test_date)

            # TestCase2
            with self.assertRaises(Exception):
                preprocess_log_file(self.bad_timestamp_file, self.test_date)

            # TestCase3
            with self.assertRaises(Exception):
                preprocess_log_file(self.bad_header_format_file, self.test_date)

            # TestCase 4
            self.assertEqual(sorted(get_active_cookie(LOG_FILE_COLUMNS, self.cookie_list)),
                             sorted(self.correct_cookie_list))

