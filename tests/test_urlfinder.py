import unittest

import urlfinder


class URLFinderTests(unittest.TestCase):
    def test_url_ends_at_whitespace_in_multiline_text(self):
        for whitespace in (" ", "\n", "\r\n", "\t", "\u00a0"):
            with self.subTest(whitespace=whitespace):
                self.assertEqual(
                    urlfinder.find_urls("Listen https://example.test/story" + whitespace + "next line"),
                    ["https://example.test/story"],
                )

    def test_separate_links_survive_multiline_text(self):
        self.assertEqual(
            urlfinder.find_urls("https://one.example.test/\nhttps://two.example.test/"),
            ["https://one.example.test/", "https://two.example.test/"],
        )

    def test_existing_punctuation_and_scheme_spelling_are_preserved(self):
        self.assertEqual(
            urlfinder.find_urls('(https://example.test/path?q=1#part), www.example.test; ftp://example.test/file'),
            ["https://example.test/path?q=1#part", "www.example.test", "ftp://example.test/file"],
        )


if __name__ == "__main__":
    unittest.main()
